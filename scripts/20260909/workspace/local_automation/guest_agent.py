'Guest-side UI executor. File IPC only; no cloud, shell, or native-project writes.'
import ctypes
import json
import os
import sys
import time
import traceback
import uuid
from pathlib import Path

sys.coinit_flags = 0
import win32api
import win32con
import win32gui
import win32process
from PIL import ImageGrab
from pywinauto import Desktop, keyboard, mouse
from pywinauto.uia_defines import IUIA
from pywinauto.uia_element_info import UIAElementInfo
from pywinauto.controls.uiawrapper import UIAWrapper

ctypes.windll.shcore.SetProcessDpiAwareness(2)
BASE = Path(sys.executable).resolve().parent.parent if getattr(sys, 'frozen', False) else Path(__file__).resolve().parent / 'bridge'
REQ, RESP = BASE / 'requests', BASE / 'responses'
ELEMENTS = {}
LAST = {}


def read_scope():
    #  VMware shared folders can briefly expose an in-place host write.
    for attempt in range(20):
        try:
            return json.loads((BASE / 'scope.json').read_text(encoding='utf-8'))
        except (PermissionError, json.JSONDecodeError):
            if attempt == 19:
                raise
            time.sleep(.1)


def write_json(path, data):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    os.replace(tmp, path)


def process_path(hwnd):
    try:
        pid = win32process.GetWindowThreadProcessId(hwnd)[1]
        h = win32api.OpenProcess(0x1000, False, pid)
        try:
            size = ctypes.c_ulong(32768)
            buf = ctypes.create_unicode_buffer(size.value)
            ctypes.windll.kernel32.QueryFullProcessImageNameW(int(h), 0, buf, ctypes.byref(size))
            return buf.value
        finally:
            h.Close()
    except Exception:
        return ''


def allowed_window(hwnd):
    exe = Path(process_path(hwnd)).name.lower()
    return 'tobii' in exe and win32gui.IsWindowVisible(hwnd)


def project_window(hwnd):
    root = win32gui.GetAncestor(hwnd, 3)
    if win32gui.GetWindowText(root)=='Tobii Pro Lab':return root
    pid=win32process.GetWindowThreadProcessId(hwnd)[1]
    mains=[w['hwnd'] for w in windows() if w['title']=='Tobii Pro Lab' and win32process.GetWindowThreadProcessId(w['hwnd'])[1]==pid]
    return mains[0] if len(mains)==1 else None


def current_project(hwnd):
    root=project_window(hwnd)
    if root is None:return ''
    try:
        uia=IUIA()
        element=uia.iuia.ElementFromHandle(root)
        condition=uia.iuia.CreatePropertyCondition(uia.UIA_dll.UIA_AutomationIdPropertyId,'DashboardRadioButton')
        match=element.FindFirst(uia.UIA_dll.TreeScope_Descendants,condition)
        return match.CurrentName if match else ''
    except Exception:
        return ''


def windows():
    out = []
    def visit(hwnd, _):
        if allowed_window(hwnd):
            out.append({'hwnd': hwnd, 'title': win32gui.GetWindowText(hwnd), 'process': process_path(hwnd), 'rect': win32gui.GetWindowRect(hwnd)})
    win32gui.EnumWindows(visit, None)
    return out


def observe(hwnd, screenshot=True, max_depth=10, max_elements=1800):
    if read_scope().get('cached_uia_observation',False):
        return observe_cached(hwnd,screenshot,max_depth,max_elements)
    if not allowed_window(hwnd):
        raise RuntimeError('Target is not a visible Tobii window')
    w = Desktop(backend='uia').window(handle=hwnd).wrapper_object()
    snap = uuid.uuid4().hex
    items, cache = [], {}
    deadline = time.monotonic() + 20
    def visit(e, parent, depth):
        if len(items) >= max_elements or depth > max_depth or time.monotonic() > deadline:
            return
        try:
            info = e.element_info
            idx = len(items)
            rect = e.rectangle()
            item = {'id': idx, 'parent': parent, 'depth': depth, 'name': info.name, 'type': info.control_type, 'automation_id': info.automation_id, 'class': info.class_name, 'rect': [rect.left, rect.top, rect.right, rect.bottom], 'enabled': e.is_enabled(), 'visible': e.is_visible()}
            methods = []
            if info.control_type == 'Edit':
                methods.append(('value', 'get_value'))
            if info.control_type in ('CheckBox', 'Button'):
                methods.append(('toggle', 'get_toggle_state'))
            if info.control_type in ('RadioButton', 'ListItem', 'TabItem', 'Custom', 'TreeItem'):
                methods.append(('selected', 'is_selected'))
            if info.control_type == 'ComboBox':
                methods.append(('selected_text', 'selected_text'))
            for key, method in methods:
                try:
                    item[key] = getattr(e, method)()
                except Exception:
                    pass
            items.append(item)
            cache[idx] = e
            if not item['visible'] or info.control_type=='DataGrid':
                #  Read full tables from the native read-only snapshot for QA.
                return
            for child in e.children():
                visit(child, idx, depth + 1)
        except Exception:
            return
    visit(w, None, 0)
    bounds = list(win32gui.GetWindowRect(hwnd))
    out = {'snapshot_id': snap, 'hwnd': hwnd, 'title': win32gui.GetWindowText(hwnd), 'project': current_project(hwnd), 'foreground': win32gui.GetForegroundWindow(), 'rect': bounds, 'elements': items, 'time': time.time()}
    if screenshot:
        name = snap + '.png'
        ImageGrab.grab(bbox=tuple(bounds), all_screens=True).save(BASE / 'screenshots' / name)
        out['screenshot'] = 'screenshots/' + name
    ELEMENTS.clear()
    ELEMENTS.update(cache)
    LAST.clear()
    LAST.update(out)
    return out


def observe_cached(hwnd, screenshot=True, max_depth=10, max_elements=1800):
    "Fetch each sibling set's UIA properties in one provider call.\n\n    The cache exists for this observation only. Actions retain live element\n    references and all foreground/project/freshness checks remain unchanged.\n    "
    if not allowed_window(hwnd):raise RuntimeError('Target is not a visible Tobii window')
    uia=IUIA(); api=uia.UIA_dll
    request=uia.iuia.CreateCacheRequest()
    request.TreeScope=api.TreeScope_Element
    properties=['Name','ControlType','AutomationId','ClassName','BoundingRectangle','IsEnabled','IsOffscreen',
                'IsValuePatternAvailable','ValueValue','IsTogglePatternAvailable','ToggleToggleState',
                'IsSelectionItemPatternAvailable','SelectionItemIsSelected']
    for name in properties:request.AddProperty(getattr(api,'UIA_'+name+'PropertyId'))
    root=uia.iuia.ElementFromHandle(hwnd).BuildUpdatedCache(request)
    items=[]; cache={}; deadline=time.monotonic()+20
    def prop(e,name):return e.GetCachedPropertyValue(getattr(api,'UIA_'+name+'PropertyId'))
    def visit(e,parent,depth):
        if len(items)>=max_elements or depth>max_depth or time.monotonic()>deadline:return
        idx=len(items); r=e.CachedBoundingRectangle
        kind=uia.known_control_type_ids[int(prop(e,'ControlType'))]
        item={'id':idx,'parent':parent,'depth':depth,'name':prop(e,'Name'),'type':kind,
              'automation_id':prop(e,'AutomationId'),'class':prop(e,'ClassName'),
              'rect':[r.left,r.top,r.right,r.bottom],'enabled':bool(prop(e,'IsEnabled')),'visible':not bool(prop(e,'IsOffscreen'))}
        if kind=='Edit' and prop(e,'IsValuePatternAvailable'):item['value']=prop(e,'ValueValue')
        if kind in ('CheckBox','Button') and prop(e,'IsTogglePatternAvailable'):item['toggle']=int(prop(e,'ToggleToggleState'))
        if kind in ('RadioButton','ListItem','TabItem','Custom','TreeItem') and prop(e,'IsSelectionItemPatternAvailable'):item['selected']=int(bool(prop(e,'SelectionItemIsSelected')))
        if kind=='ComboBox':
            try:item['selected_text']=UIAWrapper(UIAElementInfo(e)).selected_text()
            except Exception:pass
        items.append(item);cache[idx]=e
        if not item['visible'] or kind=='DataGrid' or depth>=max_depth:return
        children=e.FindAllBuildCache(api.TreeScope_Children,uia.true_condition,request)
        for i in range(children.Length):visit(children.GetElement(i),idx,depth+1)
    visit(root,None,0)
    snap=uuid.uuid4().hex;bounds=list(win32gui.GetWindowRect(hwnd))
    out={'snapshot_id':snap,'hwnd':hwnd,'title':win32gui.GetWindowText(hwnd),'project':current_project(hwnd),
         'foreground':win32gui.GetForegroundWindow(),'rect':bounds,'elements':items,'time':time.time(),'observation_method':'uia_property_cache'}
    if screenshot:
        name=snap+'.png';ImageGrab.grab(bbox=tuple(bounds),all_screens=True).save(BASE/'screenshots'/name)
        out['screenshot']='screenshots/'+name
    ELEMENTS.clear();ELEMENTS.update(cache);LAST.clear();LAST.update(out)
    return out


def assert_snapshot(cmd):
    if cmd.get('snapshot_id') != LAST.get('snapshot_id') or time.time() - LAST.get('time', 0) > 120:
        raise RuntimeError('Missing or stale observation')
    hwnd = LAST['hwnd']
    if not allowed_window(hwnd) or list(win32gui.GetWindowRect(hwnd)) != LAST['rect']:
        raise RuntimeError('Target window changed')
    scope = read_scope()
    allowed = scope.get('allowed_project_names', [])
    normalize = lambda s: s.replace('_', '').casefold()
    active = current_project(hwnd)
    if normalize(active)!=normalize(LAST.get('project','')):
        raise RuntimeError('Active project changed after the last observation; mutation refused')
    if normalize(active) not in [normalize(name) for name in allowed]:
        raise RuntimeError('Expected authorized project is not visible in UIA; mutation refused')
    if win32gui.GetForegroundWindow() != hwnd:
        raise RuntimeError('Tobii target is not foreground')
    return hwnd


def execute(cmd):
    op = cmd['op']
    if op == 'ping':
        return {'version':7, 'computer': os.environ.get('COMPUTERNAME'), 'user': os.environ.get('USERNAME'), 'bridge': str(BASE), 'screen': [win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)]}
    if op == 'windows':
        return windows()
    if op == 'list_build_projects':
        return [{'directory':str(p), 'native_project':(p/'tobii.project').is_file()} for p in Path('__MASKED_LOCAL_PATH_0734__').iterdir() if p.is_dir()]
    if op == 'restore_native_backup':
        #  Restore an approved native UI export byte-for-byte to a NEW directory.
        #  No native field is generated or changed here; naming stays in Pro Lab UI.
        import hashlib
        import zipfile
        from pathlib import PurePosixPath
        archive = (BASE / 'native_backups' / str(cmd['archive'])).resolve()
        backup_root = (BASE / 'native_backups').resolve()
        destination = Path(cmd['destination']).resolve()
        scope = read_scope()
        if archive.parent != backup_root or archive.suffix.lower() != '.zip':
            raise RuntimeError('Backup must be a direct file in the native backup exchange folder')
        if destination not in [Path(p).resolve() for p in scope.get('restore_target_paths', [])] or destination.parent != Path('__MASKED_LOCAL_PATH_0734__').resolve():
            raise RuntimeError('Restore target is outside the exact configured new target paths')
        if destination.exists():
            raise RuntimeError('Restore target already exists; never overwrite a project')
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        if digest != cmd['sha256'] or scope.get('approved_native_backups', {}).get(archive.name) != digest:
            raise RuntimeError('Native backup hash is not approved')
        with zipfile.ZipFile(archive) as z:
            if z.testzip() is not None:
                raise RuntimeError('Native backup CRC failed')
            entries = z.infolist()
            roots = {PurePosixPath(e.filename).parts[0] for e in entries if PurePosixPath(e.filename).parts}
            if len(roots) != 1 or str(next(iter(roots)))+'/tobii.project' not in z.namelist():
                raise RuntimeError('Expected one native project root')
            if len(entries)>10000 or sum(e.file_size for e in entries)>2_000_000_000:
                raise RuntimeError('Unexpected archive size')
            checked=[]
            for e in entries:
                parts=PurePosixPath(e.filename).parts
                if not parts or any(x in ('..','.') or ':' in x or '\\' in x for x in parts) or e.filename.startswith('/') or (e.external_attr >> 16) & 0o170000 == 0o120000:
                    raise RuntimeError('Unsafe archive member')
                target=destination.joinpath(*parts[1:]).resolve()
                if target != destination and destination not in target.parents:
                    raise RuntimeError('Archive member escapes restore directory')
                checked.append((e,target))
            destination.mkdir()
            for e,target in checked:
                if e.is_dir():
                    target.mkdir(parents=True,exist_ok=True)
                else:
                    target.parent.mkdir(parents=True,exist_ok=True)
                    with z.open(e) as source, target.open('xb') as output:
                        import shutil
                        shutil.copyfileobj(source,output)
        return {'restored_path':str(destination), 'backup_sha256':digest, 'files':len(entries), 'native_fields_modified':False}
    if op == 'observe':
        return observe(int(cmd['hwnd']), cmd.get('screenshot', True), cmd.get('max_depth', 10), cmd.get('max_elements', 1800))
    if op == 'activate':
        hwnd = int(cmd['hwnd'])
        if not allowed_window(hwnd):
            raise RuntimeError('Not an allowed target')
        Desktop(backend='uia').window(handle=hwnd).set_focus()
        time.sleep(.25)
        return observe(hwnd)
    if op == 'read_test_project':
        import zipfile
        path = Path(cmd['path']).resolve()
        scope = read_scope()
        allowed = [Path(p).resolve() for p in scope.get('test_project_paths', [])]
        if path not in allowed or not (path / 'tobii.project').is_file():
            raise RuntimeError('Only exact configured test project paths may be read')
        dest = BASE / 'responses' / (cmd['id'] + '.zip')
        with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as z:
            for f in path.rglob('*'):
                if f.is_file() and f.suffix.lower() in ('.json', '.project', '.xml'):
                    z.write(f, path.name + '/' + str(f.relative_to(path)).replace('\\', '/'))
        return {'readonly_snapshot': str(dest.name)}
    hwnd = assert_snapshot(cmd)
    main_hwnd=project_window(hwnd)
    e = ELEMENTS.get(cmd.get('element_id'))
    if e is not None and not isinstance(e,UIAWrapper):
        e=UIAWrapper(UIAElementInfo(e))
    if op == 'set_value':
        if e is None or e.element_info.control_type != 'Edit':
            raise RuntimeError('Expected an observed Edit element')
        value = str(cmd['value'])
        if len(value) > 300:
            raise RuntimeError('Text too long')
        e.set_edit_text(value)
    elif op == 'invoke':
        if e is None:
            raise RuntimeError('Unknown element')
        e.invoke()
    elif op == 'select':
        if e is None:
            raise RuntimeError('Unknown element')
        e.select()
    elif op == 'expand':
        if e is None:
            raise RuntimeError('Unknown element')
        e.expand()
    elif op == 'select_combo':
        if e is None or e.element_info.control_type != 'ComboBox':
            raise RuntimeError('Expected observed ComboBox')
        e.select(str(cmd['value']))
        if e.selected_text() != str(cmd['value']):
            raise RuntimeError('ComboBox did not reach requested value')
    elif op == 'focus':
        if e is None:
            raise RuntimeError('Unknown element')
        e.set_focus()
    elif op == 'set_toggle':
        if e is None:
            raise RuntimeError('Unknown element')
        wanted = int(cmd['value'])
        if wanted not in (0, 1):
            raise RuntimeError('Invalid toggle state')
        if e.get_toggle_state() != wanted:
            e.toggle()
        if e.get_toggle_state() != wanted:
            raise RuntimeError('Toggle did not reach requested state')
    elif op == 'click':
        if e is not None:
            e.click_input(double=bool(cmd.get('double')),button='right' if cmd.get('right') else 'left')
        else:
            x, y = int(cmd['x']), int(cmd['y'])
            left, top, right, bottom = LAST['rect']
            if not (0 <= x < right-left and 0 <= y < bottom-top):
                raise RuntimeError('Coordinate outside observed target')
            mouse.double_click(coords=(left+x, top+y)) if cmd.get('double') else mouse.click(coords=(left+x, top+y))
    elif op == 'key':
        keys = {'TAB': '{TAB}', 'ENTER': '{ENTER}', 'ESC': '{ESC}', 'CTRL_A': '^a', 'CTRL_C': '^c', 'CTRL_V': '^v', 'CTRL_S':'^s', 'SPACE': '{SPACE}', 'DELETE': '{DELETE}', 'DOWN': '{DOWN}', 'UP': '{UP}', 'P':'p','Q':'q','7':'7'}
        keyboard.send_keys(keys[cmd['key']], pause=.04)
    elif op == 'type_text':
        value = str(cmd['value'])
        if len(value) > 300:
            raise RuntimeError('Text too long')
        import win32clipboard
        win32clipboard.OpenClipboard()
        try:
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(value, win32con.CF_UNICODETEXT)
        finally:
            win32clipboard.CloseClipboard()
        keyboard.send_keys('^v', pause=.05)
    elif op == 'scroll':
        n = max(-8, min(8, int(cmd['notches'])))
        left, top, right, bottom = LAST['rect']
        if not (0 <= int(cmd['x']) < right-left and 0 <= int(cmd['y']) < bottom-top):
            raise RuntimeError('Scroll point outside target')
        mouse.scroll(coords=(left+int(cmd['x']), top+int(cmd['y'])), wheel_dist=n)
    else:
        raise RuntimeError('Unsupported action: ' + op)
    time.sleep(.35)
    return observe(hwnd if allowed_window(hwnd) else main_hwnd, screenshot=cmd.get('screenshot',False))


def main():
    #  File handle is held for process lifetime: prevents two agents from clicking.
    import msvcrt
    lock = open(BASE / 'agent.lock', 'a+b')
    lock.seek(0)
    if lock.read(1) == b'':
        lock.write(b'0')
        lock.flush()
    lock.seek(0)
    msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
    for p in (REQ, RESP, BASE / 'screenshots'):
        p.mkdir(exist_ok=True)
    heartbeat = 0
    handled = {p.stem for p in RESP.glob('*.json')}
    while not (BASE / 'STOP').exists():
        if time.time() - heartbeat > 2:
            write_json(BASE / 'guest_status.json', {'status': 'ready', 'time': time.time(), 'pid': os.getpid(), 'computer': os.environ.get('COMPUTERNAME')})
            heartbeat = time.time()
        for path in sorted(REQ.glob('*.json')):
            target = RESP / path.name
            if path.stem in handled:
                continue
            started = time.time()
            try:
                cmd = json.loads(path.read_text(encoding='utf-8'))
                if cmd['id'] != path.stem or started > cmd['expires_at']:
                    raise RuntimeError('Invalid or expired command')
                result = {'ok': True, 'result': execute(cmd)}
            except Exception as exc:
                result = {'ok': False, 'error': str(exc), 'trace': traceback.format_exc(limit=3)}
            result.update({'id': path.stem, 'started': started, 'seconds': time.time()-started})
            write_json(target, result)
            handled.add(path.stem)
        time.sleep(.15)
    write_json(BASE / 'guest_status.json', {'status': 'stopped', 'time': time.time()})


if __name__ == '__main__':
    try:
        main()
    except Exception:
        (BASE / 'agent_error.log').write_text(traceback.format_exc(), encoding='utf-8')
