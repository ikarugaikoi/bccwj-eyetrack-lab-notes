'Deterministic UIA client: each action uses a fresh observed element.'
import argparse
import json
import time
from controller import command, ROOT

STATE = ROOT/'logs'/'current_uia.json'

def save(s):
    STATE.write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')
    return s

def compact(s):
    return {'snapshot_id':s['snapshot_id'], 'hwnd':s['hwnd'],
            'controls':[{k:e[k] for k in ('id','parent','type','automation_id','name','value','selected','toggle') if k in e}
                        for e in s['elements'] if e['visible'] and
                        (e['type'] in ('Edit','ComboBox','CheckBox','MenuItem','RadioButton','Button','TreeItem')
                         or e['name'] and e['depth']<7)]}

def find(s, **selector):
    matches=[e for e in s['elements'] if e['visible'] and e['enabled'] and all(e.get(k)==v for k,v in selector.items())]
    if len(matches)!=1:
        raise RuntimeError(f'Selector {selector}: expected one control, found {len(matches)}')
    return matches[0]

class UI:
    def __init__(self, hwnd=None):
        self.hwnd=hwnd or json.loads(STATE.read_text(encoding='utf-8'))['hwnd']
        self.s=save(command('observe',hwnd=self.hwnd,screenshot=False))
    def act(self, op, selector=None, **kwargs):
        if selector:
            kwargs['element_id']=find(self.s,**selector)['id']
        self.s=save(command(op,snapshot_id=self.s['snapshot_id'],**kwargs))
        return self.s
    def observe(self):
        self.s=save(command('observe',hwnd=self.hwnd,screenshot=False))
        return self.s

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('op',nargs='?',default='observe')
    p.add_argument('--selector',default='{}');p.add_argument('--args',default='{}')
    a=p.parse_args();u=UI()
    if a.op!='observe':u.act(a.op,json.loads(a.selector) or None,**json.loads(a.args))
    print(json.dumps(compact(u.s),ensure_ascii=False))
