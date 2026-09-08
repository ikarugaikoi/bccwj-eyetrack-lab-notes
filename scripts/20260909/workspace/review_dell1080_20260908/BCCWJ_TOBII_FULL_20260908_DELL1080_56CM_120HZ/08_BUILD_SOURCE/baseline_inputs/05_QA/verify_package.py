# !__MASKED_LOCAL_PATH_0917__
'Read-only portable asset/blueprint audit. Python 3.8+, standard library only.\n\nRun from any directory. This does NOT inspect or certify native Pro Lab projects.\nDo not use --preflight for the final transferred package: it skips hash checking.\n'
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import posixpath
import re
import struct
import sys
import xml.etree.ElementTree as ET
import zipfile
import zlib

ROOT = Path(__file__).resolve().parents[1]
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
FIRST11 = ['article_block', 'row_type', 'media_name', 'DOT_W', 'DOT_H',
           'DOT_X', 'DOT_Y', 'MAIN_W', 'MAIN_H', 'MAIN_X', 'MAIN_Y']
LAYOUT = {'MAIN': dict(zip('WHXY', [1, .9, 0, .05])),
          'DOT': dict(zip('WHXY', [.05, .07, .01, .11]))}
TYPES = ['fixation', 'reading', 'question']
PRESET = dict(zip(TYPES, ['FIX', 'READ', 'QUESTION']))
TEMPLATE = dict(zip(TYPES, ['FIXATION_CHECK', 'READ_TEMPLATE', 'QUESTION_TEMPLATE']))
CATEGORY = dict(zip(TYPES, ['fixation', 'reading', 'questions']))
TABLE_NAMES = {o: 'order%02d_%s_P_TRUE_Q_FALSE.xlsx' % (i, o)
               for i, o in enumerate(['AB', 'BA', 'CD', 'DC'], 1)}
CHECKS = 0


def require(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise ValueError(label)


def read_json(relative):
    return json.loads((ROOT / relative).read_text(encoding='utf-8'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local(relative):
    p = Path(relative)
    require(not p.is_absolute() and '..' not in p.parts, 'Unsafe path: ' + relative)
    require((ROOT / p).is_file(), 'Missing file: ' + relative)
    return ROOT / p


def png(path):
    data = path.read_bytes()
    require(data[:8] == b'\x89PNG\r\n\x1a\n', 'PNG signature: ' + str(path))
    offset, sizes, ended = 8, None, False
    while offset < len(data):
        length = struct.unpack('>I', data[offset:offset + 4])[0]
        kind = data[offset + 4:offset + 8]
        payload = data[offset + 8:offset + 8 + length]
        expected = struct.unpack('>I', data[offset + 8 + length:offset + 12 + length])[0]
        require(zlib.crc32(kind + payload) & 0xffffffff == expected,
                'PNG chunk CRC: ' + str(path))
        if kind == b'IHDR':
            w, h, depth, color, _, _, _ = struct.unpack('>IIBBBBB', payload)
            sizes = (w, h, depth, color)
        offset += length + 12
        if kind == b'IEND':
            ended = True
            break
    require(ended and offset == len(data), 'PNG ending: ' + str(path))
    expected = (96, 84, 8, 6) if path.name == 'FIXATION_DOT_96x84_TOBII.png' else (1920, 1080, 8, 2)
    require(sizes == expected, 'PNG dimensions/format: ' + str(path))


def column_index(cell_ref):
    index = 0
    for char in re.match('[A-Z]+', cell_ref).group():
        index = index * 26 + ord(char) - 64
    return index - 1


def workbook(path):
    #  Parse the actual XLSX XML independently of the builder's openpyxl reader.
    with zipfile.ZipFile(path) as archive:
        require(archive.testzip() is None, 'XLSX CRC: ' + path.name)
        strings = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            strings = [''.join(si.itertext()) for si in
                       ET.fromstring(archive.read('xl/sharedStrings.xml'))]
        relationships = ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))
        targets = {e.attrib['Id']: e.attrib['Target'] for e in relationships}
        sheets = ET.fromstring(archive.read('xl/workbook.xml')).find('s:sheets', NS)
        require([s.attrib['name'] for s in sheets] == ['Tobii_Design', 'Group_Map', 'Codebook'],
                'Workbook sheets: ' + path.name)
        result = {}
        for sheet in sheets:
            rid = sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
            target = targets[rid]
            target = target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/' + target)
            rows = []
            for row in ET.fromstring(archive.read(target)).findall('s:sheetData/s:row', NS):
                values = []
                for cell in row.findall('s:c', NS):
                    require(cell.find('s:f', NS) is None, 'Unexpected formula: ' + path.name)
                    idx = column_index(cell.attrib['r'])
                    while len(values) <= idx:
                        values.append(None)
                    typ = cell.attrib.get('t', 'n')
                    value = cell.find('s:v', NS)
                    if typ == 'inlineStr':
                        value = ''.join(t.text or '' for t in cell.findall('.//s:t', NS))
                    elif value is not None:
                        value = value.text
                        if typ == 's':
                            value = strings[int(value)]
                        elif typ == 'n':
                            value = float(value)
                            if value.is_integer():
                                value = int(value)
                    values[idx] = value
                if any(v is not None for v in values):
                    rows.append((int(row.attrib['r']), values))
            headers = rows[0][1]
            result[sheet.attrib['name']] = (headers, [dict(zip(headers, vals + [None] * (len(headers) - len(vals))),
                                                            excel_row=n) for n, vals in rows[1:]])
        return result


def check_container(c, group_type=None, instruction_source=None):
    name = c['name']
    require(name in LAYOUT and c['layout'] == LAYOUT[name], 'Container layout')
    require(c['media_scale'] == 'Original' and c['use_as_aoi'] is False and c['mouse_click'] == 'None',
            'Container scale/AOI/mouse')
    gaze = name == 'DOT' and group_type == 'fixation'
    require(c['gaze_mode'] == ('Continuous' if gaze else 'None'), 'Container gaze mode')
    require(c['gaze_threshold_ms'] == (300 if gaze else None) and
            c['data_loss_reset_ms'] == (34 if gaze else None), 'Container gaze timing')
    bound = group_type in ['reading', 'question']
    expected_source = ('media_name' if bound else instruction_source if instruction_source else
                       'FIXATION_DOT_96x84_TOBII' if name == 'DOT' else 'FIXATION_BG_1920x1080_WHITE')
    require(c['source_mode'] == ('bind_column' if bound else 'fixed_media') and
            c['source_value'] == expected_source, 'Container media source')
    require(c['layout_bindings'] == ({k: name + '_' + k for k in 'WHXY'} if group_type else {}),
            'Container layout bindings')


def audit(preflight):
    if not preflight:
        manifest = read_json('HASHES_SHA256.json')
        for relative, info in manifest['files'].items():
            path = local(relative)
            require(path.stat().st_size == info['bytes'] and digest(path) == info['sha256'],
                    'SHA256 mismatch: ' + relative)
    media = list((ROOT / '01_MEDIA').rglob('*.png'))
    require(Counter(p.parent.name for p in media) ==
            Counter(reading=71, questions=20, fixation=2, instructions_ZH=19, instructions_JA=19),
            'Media file counts')
    require(len({p.stem.casefold() for p in media}) == 131, 'Duplicate media names')
    for path in media:
        png(path)
    tables, gold = {}, {}
    require({p.name for p in (ROOT / '02_DESIGN_TABLES').iterdir()} == set(TABLE_NAMES.values()),
            'Exactly four current workbooks; no historical versions')
    for order, name in TABLE_NAMES.items():
        book = workbook(local('02_DESIGN_TABLES/' + name))
        heads, rows = book['Tobii_Design']
        require(heads[:11] == FIRST11 and len(heads) == 34, 'Table column order: ' + order)
        require(len(rows) == (73 if order in ['AB', 'BA'] else 64), 'Table row count: ' + order)
        require(len(book['Group_Map'][1]) == 39, 'Group map length: ' + order)
        require([r['presentation_index'] for r in rows] == list(range(1, len(rows) + 1)), 'Event index')
        for r in rows:
            for prefix, coords in LAYOUT.items():
                require(all(r[prefix + '_' + k] == v for k, v in coords.items()), 'Table coordinates')
            require(r['media_filename'] == r['media_name'] + '.png', 'Media filename mapping')
            local('01_MEDIA/' + CATEGORY[r['row_type']] + '/' + r['media_filename'])
            if r['row_type'] == 'question':
                require(r['correct_key'] == {'__MASKED_TEXT_0054__': 'P', '__MASKED_TEXT_0058__': 'Q'}[r['truth_value_ja']],
                        'Question P/Q mapping')
                require(r['allowed_keys'] == 'Q|P', 'Question accepts both keys')
                value = (r['correct_key'], r['truth_value_ja'], r['media_name'], r['article_block'])
                require(gold.get(r['question_no'], value) == value, 'Question consistency across tables')
                gold[r['question_no']] = value
            elif r['row_type'] == 'reading':
                require(r['allowed_keys'] == 'SPACE', 'Reading key')
        tables[order] = book
    scoring = read_json('03_SPEC/QUESTION_SCORING_P_TRUE_Q_FALSE.json')['questions']
    require(len(gold) == len(scoring) == 20, 'Unique question count')
    for q in scoring:
        require(gold[q['question_no']] == (q['correct_key'], q['truth_value_ja'], q['media_name'], q['article_block']),
                'Offline scoring JSON disagrees with table')
    params = read_json('03_SPEC/BUILD_PARAMETERS.json')
    expected_keys = {'INSTRUCTION_SPACE': ['Space'], 'KEY_CHECK_P': ['P'], 'KEY_CHECK_Q': ['Q'],
                     'END_OPERATOR_7': ['7'], 'FIX': [], 'READ': ['Space'], 'QUESTION': ['Q', 'P']}
    for preset, keys in expected_keys.items():
        p = params['presets'][preset]
        require(p['keys'] == keys and p['key_press_enabled'] == bool(keys), 'Enabled keys: ' + preset)
        require(p['time_mode'] == p['mouse_click'] == p['media_end'] == 'None' and
                not p['look_away_enabled'] and not p['show_mouse_cursor'] and not p['send_ttl_markers'],
                'Automatic advance disabled: ' + preset)
        require(p['min_presentation_time_enabled'] and p['min_presentation_time_ms'] == 100 and
                p['background'] == '#000000', 'Minimum/background: ' + preset)
    require(params['presets']['QUESTION']['only_correct_key_advances'] is False, 'Wrong answers advance')
    instructions = read_json('03_SPEC/INSTRUCTION_TEXTS.json')['languages']
    catalogs, all_projects = {}, {}
    for lang in ['ZH', 'JA']:
        pages = {p['relative_path']: p for p in instructions[lang]['pages']}
        require(len(pages) == 19, 'Instruction manifest length')
        for rel, p in pages.items():
            require(digest(local(rel)) == p['sha256'], 'Instruction manifest hash')
        spec = read_json('04_PROJECT_BLUEPRINTS/PROJECTS_' + lang + '.json')
        projects = spec['projects']
        all_projects[lang] = projects
        require(spec['presets'] == params['presets'], 'Blueprint presets')
        require(len(projects) == 42 and Counter(p['kind'] for p in projects) ==
                Counter(practice=2, formal=8, recovery=32), 'Project counts: ' + lang)
        require(len({p['base_project_name'] for p in projects}) == 42, 'Unique project names')
        require(sum(p['group_count'] for p in projects) == 378, 'Total groups')
        for index, p in enumerate(projects, 1):
            label = p['base_project_name']
            order, half, kind = p['order'], p['half'], p['kind']
            if kind == 'practice':
                expected_blocks = ['C05', 'D03', 'C01'] if order == 'AB' else ['B05', 'A05', 'B03']
                require(order in ['AB', 'CD'] and half is None, 'Practice condition')
                require(label == 'BCCWJ_EyeTrack_PRACTICE_' + ('A' if order == 'AB' else 'B'), 'Practice name')
                first = 'PRACTICE_00_WELCOME'
                ending = 'PRACTICE_10_END'
                intro_count = 11
            else:
                require(order in TABLE_NAMES and half in [1, 2], 'Formal condition/half')
                start = int(p['resume_from'][1:]) if kind == 'recovery' else 1
                require(start in ([2, 3, 4, 5] if kind == 'recovery' else [1]), 'Recovery start')
                expected_blocks = [order[half - 1] + '%02d' % n for n in range(start, 6)]
                normal = 'BCCWJ_EyeTrack_FORMAL_%s_H%d' % (order, half)
                require(label == normal + ('_FROM_' + expected_blocks[0] if kind == 'recovery' else ''), 'Formal name')
                if kind == 'recovery':
                    require(p['normal_parent'] == normal, 'Recovery parent')
                first = ('RECOVERY_00_RECALIBRATION_INTRO' if kind == 'recovery' else
                         'FORMAL_00_INTRO' if half == 1 else 'FORMAL_03_RECALIBRATION_INTRO')
                ending = 'FORMAL_02_BREAK' if half == 1 else 'FORMAL_05_END'
                intro_count = 3
            require(p['article_blocks'] == expected_blocks, 'Article scope: ' + label)
            require(p['language'] == lang and p['single_language_project_name'] == label and
                    p['bilingual_project_name'] == label + '_' + lang, 'Language/name: ' + label)
            require(p['presentation_resolution'] == [1920, 1200] and p['project_type'] == 'Advanced Screen', 'Project display')
            require(p['workbook_path'] == '02_DESIGN_TABLES/' + TABLE_NAMES[order] and
                    digest(local(p['workbook_path'])) == p['workbook_sha256'], 'Project table')
            elems = p['elements']
            require(elems[0]['stimulus_name'] == first and elems[-1]['stimulus_name'] == ending and
                    elems[-1]['preset'] == 'END_OPERATOR_7', 'Opening/ending: ' + label)
            expected_intros = (['PRACTICE_00_WELCOME', 'PRACTICE_01_READING_TASK',
                                'PRACTICE_02_QUESTION_KEYS_P_TRUE_Q_FALSE', 'PRACTICE_03_KEY_CHECK_INTRO',
                                'PRACTICE_04_KEY_CHECK_P', 'PRACTICE_05_KEY_CHECK_Q', 'PRACTICE_06_PRACTICE_INTRO',
                                'PRACTICE_07_CALIBRATION_INTRO', 'PRACTICE_08_FIXATION_INTRO', 'PRACTICE_09_START']
                               if kind == 'practice' else [first, 'RECOVERY_01_CONTINUE' if kind == 'recovery'
                                                          else 'FORMAL_01_START_AND_BREAK_NOTICE' if half == 1
                                                          else 'FORMAL_04_SECOND_HALF_START'])
            require([e['stimulus_name'] for e in elems[:intro_count] if e['kind'] == 'image_stimulus'] == expected_intros,
                    'Every opening instruction exactly once: ' + label)
            require([e['kind'] for e in elems] ==
                    (['image_stimulus'] * 8 + ['calibration'] + ['image_stimulus'] * 2 if kind == 'practice'
                     else ['image_stimulus', 'calibration', 'image_stimulus']) +
                    ['group'] * (3 * len(expected_blocks)) + ['image_stimulus'], 'Full element order: ' + label)
            calibration = [e for e in elems if e['kind'] == 'calibration']
            require(len(calibration) == 1 and calibration[0]['settings'] == params['calibration_build_configuration'], 'Calibration')
            groups = elems[intro_count:-1]
            require(p['group_count'] == len(groups) == 3 * len(expected_blocks), 'Project group count')
            source_rows = tables[order]['Tobii_Design'][1]
            wanted = [r for r in source_rows if r['article_block'] in expected_blocks]
            require(p['expected_article_event_ids'] == [r['event_id'] for r in wanted], 'Whole-project events')
            require(p['article_event_count'] == len(wanted) and p['total_presented_image_instances'] ==
                    len(wanted) + sum(e['kind'] == 'image_stimulus' for e in elems), 'Presentation counts')
            for i, g in enumerate(groups):
                block, typ = expected_blocks[i // 3], TYPES[i % 3]
                pos = expected_blocks.index(block) + 1 if kind == 'practice' else int(block[1:]) + 5 * (half - 1)
                gn = 3 * (pos - 1) + (1 if kind == 'practice' else 10) + i % 3
                tag = ('P' if kind == 'practice' else 'F') + '%02d' % pos
                require(g['group_name'] == 'G%02d_%s_%s_%s' % (gn, tag, block, PRESET[typ]), 'Original Group name')
                require(g['stimulus_name'] == TEMPLATE[typ] + '_' + tag + '_' + block, 'Original Stimulus name')
                require(g['subsets'] == [{'column': 'article_block', 'values': [block], 'set_at_recording_start': False},
                                         {'column': 'row_type', 'values': [typ], 'set_at_recording_start': False}] and
                        g['other_table_operators'] == [] and g['design_table'] == 'Tobii_Design', 'Group operators')
                require(g['preset'] == PRESET[typ], 'Group preset')
                selected = [r for r in source_rows if r['article_block'] == block and r['row_type'] == typ]
                events = g['expected_events']
                require(len(events) == len(selected) and bool(selected), 'Group expansion count')
                for ev, r in zip(events, selected):
                    require(all(ev[k] == r[k] for k in ev if k != 'media_path'), 'Group event differs from Excel')
                    require(ev['media_path'] == '01_MEDIA/' + CATEGORY[typ] + '/' + r['media_filename'], 'Event path')
                    local(ev['media_path'])
                require([c['name'] for c in g['containers']] == (['MAIN', 'DOT'] if typ == 'fixation' else ['MAIN']), 'Container count/layers')
                for c in g['containers']:
                    check_container(c, typ)
            for e in elems:
                if e['kind'] != 'image_stimulus':
                    continue
                page = pages[e['media_path']]
                expected_key = params['presets'][e['preset']]['keys']
                require(len(expected_key) == 1 and page['expected_advance'].startswith(expected_key[0] + ' only'), 'Instruction key agreement')
                stem = Path(e['media_path']).stem
                require(e['stimulus_name'] == stem[:-3].upper(), 'Instruction naming')
                require(len(e['containers']) == 1, 'Instruction container count')
                check_container(e['containers'][0], instruction_source=stem)
            local('04_PROJECT_BLUEPRINTS/%s/%02d_%s.md' % (lang, index, label))
        catalogs[lang] = [(p['base_project_name'], p['expected_article_event_ids']) for p in projects]
    require(catalogs['ZH'] == catalogs['JA'], 'Languages change no article events')
    selection = read_json('BUILD_SELECTION.json')
    require(selection['logical_projects_per_language'] == 42 and
            selection['selected_languages'] in [None, ['ZH'], ['JA'], ['ZH', 'JA']], 'Build selection')
    require(selection['selected_languages'] == ['ZH', 'JA'] and
            selection['selection_status'] == 'confirmed_by_user_2026-09-05' and
            selection['total_native_projects_required'] == 84, 'Latest user confirmed both languages')
    plan = read_json('04_PROJECT_BLUEPRINTS/SELECTED_BUILD_PLAN.json')
    jobs = plan['jobs']
    require(len(jobs) == plan['total_jobs'] == 84 and plan['user_confirmed'], 'Selected build plan count')
    require([j['build_sequence'] for j in jobs] == list(range(1, 85)), 'Build sequence')
    require([j['language'] for j in jobs] == ['ZH'] * 42 + ['JA'] * 42, 'Chinese first, then Japanese')
    require(len({j['project_name'] for j in jobs}) == 84, 'Unique bilingual project names')
    for idx, job in enumerate(jobs):
        lang, project_idx = job['language'], idx % 42
        p = all_projects[lang][project_idx]
        source = all_projects['ZH'][project_idx]
        require(job['project_name'] == p['bilingual_project_name'] and job['base_project_name'] == p['base_project_name'], 'Planned name')
        require(job['workbook_path'] == p['workbook_path'] and job['article_blocks'] == p['article_blocks'] and
                job['expected_article_event_ids'] == p['expected_article_event_ids'], 'Planned scope unchanged')
        local(job['blueprint_path'])
        local(job['blueprint_json_path'])
        require(job['clone_from_project_name'] == (source['bilingual_project_name'] if lang == 'JA' else None), 'Exact clone source')
        replacements = job['instruction_replacements']
        instructions_only = [e for e in p['elements'] if e['kind'] == 'image_stimulus'] if lang == 'JA' else []
        require(len(replacements) == len(instructions_only), 'All clone instructions replaced')
        for change, e in zip(replacements, instructions_only):
            require(change['stimulus_name'] == e['stimulus_name'] and change['container_name'] == 'MAIN' and
                    change['keep_preset'] == e['preset'], 'Replacement target and preserved parameters')
            require(change['to_media_path'] == e['media_path'] and
                    change['from_media_path'] == e['media_path'].replace('instructions_JA/', 'instructions_ZH/').replace('_JA.png', '_ZH.png'),
                    'Exact language media replacement')
            for key in ['from', 'to']:
                require(change[key + '_source'] == local(change[key + '_media_path']).stem, 'Replacement Source name')
    require(sum(len(j['instruction_replacements']) for j in jobs) == 142, '142 explicit Japanese replacements')
    progress = read_json('05_QA/BUILD_PROGRESS_TEMPLATE.json')
    require(progress['template_only'] and len(progress['projects']) == 84, '84 blank progress records')
    require([p['planned_project_name'] for p in progress['projects']] == [j['project_name'] for j in jobs], 'Progress order')
    require(len(list((ROOT / '06_REFERENCE_DO_NOT_IMPORT/AOI/per_screen').glob('*.csv'))) == 71, 'AOI references')
    return {'status': 'PASS', 'sha256_checked': not preflight, 'checks': CHECKS,
            'png_files': len(media), 'workbooks': 4, 'unique_questions': len(gold),
            'blueprints_per_language': 42, 'groups_per_language': 378, 'selected_native_jobs': 84,
            'build_order': 'Chinese 42, then Japanese 42 clones', 'japanese_instruction_replacements': 142,
            'native_projects_verified': False, 'hardware_verified': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preflight', action='store_true', help='Authoring only: skip final SHA256 manifest')
    args = parser.parse_args()
    try:
        print(json.dumps(audit(args.preflight), indent=2, ensure_ascii=True))
    except Exception as exc:
        print(json.dumps({'status': 'FAIL', 'error': str(exc)}, ensure_ascii=True), file=sys.stderr)
        sys.exit(1)
