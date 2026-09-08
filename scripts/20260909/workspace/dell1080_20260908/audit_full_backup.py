'Read-only audit of Pro Lab UI-exported backups against the sealed rebuild blueprints.\n\nNever edits, creates, or serializes a native Pro Lab project. Writes an audit report only.\n'
import argparse
import collections
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

import openpyxl
from acceptance import policy,permitted


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('backup', type=Path)
    ap.add_argument('--package', type=Path, default=Path('__MASKED_LOCAL_PATH_0290__'))
    ap.add_argument('--report', type=Path, required=True)
    ap.add_argument('--expected', required=True)
    ap.add_argument('--actual', required=True)
    ap.add_argument('--accept-record',type=Path)
    a = ap.parse_args()
    checks = []
    def check(label, actual, expected):
        checks.append({'check': label, 'passed': actual == expected, 'actual': actual, 'expected': expected})
    with zipfile.ZipFile(a.backup, 'r') as z:
        check('backup ZIP CRC', z.testzip(), None)
        info_path = next(n for n in z.namelist() if n.endswith('/tobii.project'))
        prefix = info_path.rsplit('/', 1)[0] + '/'
        info = ET.fromstring(z.read(info_path))
        project = info.findtext('Name')
        check('actual short project name', project, a.actual)
        lang = a.expected.rsplit('_', 1)[-1]
        catalog = json.loads((a.package / '04_PROJECT_BLUEPRINTS' / f'PROJECTS_{lang}.json').read_text(encoding='utf-8'))
        blueprint = next(p for p in catalog['projects'] if p['bilingual_project_name'] == a.expected)
        check('project type', next(e.findtext('{*}Value') for e in info.findall('.//{*}KeyValueOfstringstring') if e.findtext('{*}Key') == 'ProjectType'), 'AdvancedScreen')
        d = json.loads(z.read(next(n for n in z.namelist() if '/Data/Design/Current/Design/' in n)))['Data']
        names = {}
        for names_path in z.namelist():
            if '/Data/Names/' in names_path and names_path.endswith('.json'):
                for e in json.loads(z.read(names_path))['Data']:
                    names[e['Key']['data']] = e['Value']
        si, hi, binds = d['StructureItems'], d['HierarchyInfo'], d['Bindings']
        def name(i): return names.get(i, i)
        def children(i): return hi[i]['ChildrenIdentities']
        def binding(prop): return binds.get(prop['Id'])
        top = children(d['RootGroupId'])
        expected_top = [e.get('group_name') or e.get('stimulus_name') or e['name'] for e in blueprint['elements']]
        check('top-level order', list(map(name, top)), expected_top)
        check('reachable object count', len(si), len(hi))
        reachable = set()
        def walk(i):
            reachable.add(i)
            for c in children(i): walk(c)
        walk(d['RootGroupId'])
        check('no unattached structure items', sorted(reachable), sorted(si))
        check('one native calibration', sum(i['kind'] == 3 for i in si.values()), 1)
        check('presentation resolution', d['Settings'].get('s4910a7ec-9a65-4868-b50f-34a6cce6a34f'), '1920,1080')
        check('one full design table', len(d['Tables']), 1)
        tid, table = next(iter(d['Tables'].items()))
        columns = list(map(name, table['Columns']))
        check('design table name', name(tid), blueprint['design_table_name'])
        rows = [dict(zip(columns, table['Cells'][i:i+len(columns)])) for i in range(0, len(table['Cells']), len(columns))]
        workbook = a.package / blueprint['workbook_path']
        check('sealed workbook SHA256', hashlib.sha256(workbook.read_bytes()).hexdigest(), blueprint['workbook_sha256'])
        wb = openpyxl.load_workbook(workbook, data_only=True, read_only=True)
        wr = list(wb[blueprint['design_table_name']].values)
        check('all original table columns', columns, list(wr[0]))
        check('all original table rows', len(rows), len(wr)-1)
        table_diffs = []
        def normalize(v): return None if v is None else str(v)
        for r, expected in enumerate(wr[1:]):
            for col, v in zip(columns, expected):
                if r >= len(rows) or normalize(rows[r][col]) != normalize(v):
                    table_diffs.append({'excel_row': r+2, 'column': col, 'actual': rows[r].get(col) if r<len(rows) else None, 'expected': v})
        check('full table cell equality', table_diffs, [])
        wb.close()
        media = {}
        media_errors = []
        for n in z.namelist():
            if n.startswith(prefix+'Data/Media/') and n.endswith('.xml'):
                x = ET.fromstring(z.read(n))
                mid = x.findtext('Key')
                target = prefix+'Data/Media/'+x.findtext('TargetFileName')
                original = x.findtext('OriginalFileName')
                candidates = list((a.package/'01_MEDIA').rglob(original))
                payload = z.read(target)
                digest = hashlib.sha256(payload).hexdigest()
                expected_digest = hashlib.sha256(candidates[0].read_bytes()).hexdigest() if len(candidates)==1 else None
                if digest != expected_digest or x.findtext('IsReady') != 'true':
                    media_errors.append({'name': original, 'ready': x.findtext('IsReady'), 'sha256': digest, 'expected': expected_digest})
                media[mid] = {'name': original, 'sha256': digest, 'size': len(payload)}
        check('all library media present and sealed bytes identical', media_errors, [])
        check('media metadata matches library', sorted(media), sorted(d['MediaLibrary']))
        check('media library count', len(media), 112 if lang=='ZH' else 131)
        all_expected_bound = set()
        event_report = []
        for item_id, e in zip(top, blueprint['elements']):
            label = name(item_id)
            item = si[item_id]['data']
            if e['kind'] == 'calibration':
                for k,v in {'UseValidation':True,'RandomizeTargetOrder':True,'NumberOfTargets':9,'TargetType':0,'Background':-1}.items():
                    check(f'{label}: {k}', item.get(k), v)
                check(f'{label}: timed black point', item['PointCalibrationSettings'], {'CalibrationType':0,'TargetColor':-16777216})
                continue
            if e['kind'] == 'group':
                check(f'{label}: exactly one stimulus', list(map(name,children(item_id))), [e['stimulus_name']])
                operations = [d['DataFlowOperations'][i] for i in d['DataFlows'][item_id]['OperationIdentities']]
                check(f'{label}: table plus two subsets only', [o['kind'] for o in operations], [1,2,2])
                check(f'{label}: correct full table', operations[0]['data']['TableReference'], tid)
                subsets = [{'column':name(o['data']['ColumnId']), 'values':o['data']['SelectedValues'], 'set_at_recording_start':o['data']['SelectPerRecording']} for o in operations[1:]]
                check(f'{label}: fixed subsets', subsets, e['subsets'])
                selected = [r for r in rows if all(r[s['column']] in s['values'] for s in subsets)]
                expected_events = e['expected_events']
                for col in ['event_id','media_name','article_block','row_type','presentation_index']:
                    check(f'{label}: expanded {col}', [normalize(r[col]) for r in selected], [normalize(r[col]) for r in expected_events])
                event_report += [{'group': label, 'event_id':r['event_id'], 'media_name':r['media_name']} for r in selected]
                item_id = children(item_id)[0]
                item = si[item_id]['data']
                label = name(item_id)
            preset = catalog['presets'][e['preset']]
            check(f'{label}: stimulus name', name(item_id), e['stimulus_name'])
            check(f'{label}: min presentation', (item['MinPresentationTime']['Enabled'], item['MinPresentationTime']['Duration']['FixedValue']), (True,'00:00:00.1000000'))
            check(f'{label}: Time=None', item['TimeTrigger']['Mode'], 0)
            check(f'{label}: keyboard enabled', item['KeyboardTrigger']['IsEnabled'], preset['key_press_enabled'])
            check(f'{label}: allowed keys', sorted(k.lower() for k in item['KeyboardTrigger']['Pattern'].split('|') if k), sorted(k.lower() for k in preset['keys']))
            check(f'{label}: black background', item['Background'], -16777216)
            check(f'{label}: cursor off', item['ShowCursor'], False)
            check(f'{label}: TTL off', item['TtlOutMarker']['Enabled'], False)
            check(f'{label}: mouse none', item['StimulusAdvanceOnMouseMode'], 0)
            check(f'{label}: look away off', item['LookAwayTrigger']['IsEnabled'], False)
            check(f'{label}: media end off', item['MediaEndTrigger']['IsDisabled'], True)
            cids = children(item_id)
            check(f'{label}: container order back to front', [name(c).split('_')[0] for c in cids], [c['name'] for c in e['containers']])
            for cid, ec in zip(cids, e['containers']):
                c = si[cid]['data']
                cl = f'{label}/{name(cid)}'
                check(f'{cl}: Original scale', c['MediaScaleBehavior'], 1)
                check(f'{cl}: Mouse=None', c['AdvanceOnMouseMode'], 0)
                check(f'{cl}: Gaze mode', c['GazeTrigger']['Mode'], 1 if ec['gaze_mode']=='Continuous' else 0)
                if ec['gaze_mode']=='Continuous':
                    check(f'{cl}: continuous threshold/reset microseconds', c['GazeTrigger']['ContinuousGazeTriggerSetup'], {'ResetTime':34000,'Threshold':300000})
                for native, key in [('Width','W'),('Height','H'),('X','X'),('Y','Y'),('MediaId','Source')]:
                    prop = c[native]
                    b = binding(prop)
                    bound_to = ec['source_value'] if key=='Source' and ec['source_mode']=='bind_column' else ec['layout_bindings'].get(key)
                    if bound_to:
                        all_expected_bound.add(prop['Id'])
                        check(f'{cl}: {key} binding', {'table':b['TableId'],'column':name(b['ColumnId'])} if b else None, {'table':tid,'column':bound_to})
                    else:
                        check(f'{cl}: {key} no binding', b, None)
                        actual = name(prop['FixedValue']) if key=='Source' else prop['FixedValue']
                        expected = ec['source_value'] if key=='Source' else ec['layout'][key]
                        check(f'{cl}: {key} fixed value', actual, expected)
        check('no unexpected bindings', sorted(binds), sorted(all_expected_bound))
        #  Default false AOI properties may be omitted by the native serializer; retain the
        #  explicit visual AOI checks in the build log rather than assuming absent fields.
        report = {'project':project, 'backup':str(a.backup.resolve()), 'backup_sha256':hashlib.sha256(a.backup.read_bytes()).hexdigest(), 'native_design_member':next(n for n in z.namelist() if '/Data/Design/Current/Design/' in n), 'counts':{'top_level':len(top),'objects':len(si),'media':len(media),'table_rows':len(rows),'article_events':len(event_report)}, 'passed':all(c['passed'] for c in checks), 'checks_total':len(checks),'failed':[c for c in checks if not c['passed']], 'checks':checks,'expanded_events':event_report,'media':media,'limitations':['Read-only saved configuration audit; AOI=false verified separately in native UI.','Save/reopen UI checks recorded separately.','Fusion, physical monitor, calibration quality and hardware recording/export remain pending_hardware.']}
    a.report.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    accepted_passed=report['passed']
    if a.accept_record:
        approval=policy(a.accept_record)
        remaining=[c for c in report['failed'] if not (c['check']=='full table cell equality' and permitted(c['actual']))]
        accepted_passed=not remaining
        accepted={'project':project,'backup_sha256':report['backup_sha256'],'acceptance':approval,'strict_report':str(a.report),'strict_passed':report['passed'],'passed':accepted_passed,'checks_total':len(checks),'remaining_failures':remaining,'accepted_table_differences':table_diffs}
        a.report.with_name(a.report.stem+'_accepted.json').write_text(json.dumps(accepted,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'project':project,'counts':report['counts'],'strict_passed':report['passed'],'accepted_passed':accepted_passed,'checks_total':len(checks),'strict_failed_checks':[c['check'] for c in report['failed']]},ensure_ascii=True))
    raise SystemExit(0 if accepted_passed else 1)


if __name__ == '__main__':
    main()

