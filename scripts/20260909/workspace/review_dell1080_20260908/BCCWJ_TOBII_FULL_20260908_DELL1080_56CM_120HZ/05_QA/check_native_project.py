# !__MASKED_LOCAL_PATH_0917__
'Read an exported/extracted Pro Lab 25.7-style project. NEVER writes its input.\n\nChecks source bindings, effective table-driven geometry, flow, timing and keys.\nNot a Pro Lab editor, hardware test, or certificate of calibration/data quality.\n'
import argparse
import collections
import json
import math
from pathlib import Path
import re


def read_json(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))


def inspect(project_root, expected_name, spec, version='Current', geometry=None):
    project_root=Path(project_root)
    expectations=[p for p in spec['projects'] if p['project']==expected_name]
    if len(expectations)!=1: raise ValueError('Select one exact expected project name from PROJECT_SCOPE.csv')
    expected=expectations[0]; geo=geometry or spec['geometry']
    files=list((project_root/'Data/Design'/version/'Design').glob('*.json'))
    designs=[(p,read_json(p)) for p in files]
    designs=[(p,v['Data']) for p,v in designs if isinstance(v.get('Data'),dict) and 'StructureItems' in v['Data']]
    if len(designs)!=1: raise ValueError('Unsupported/ambiguous design snapshot; no automatic pass')
    design_path,d=designs[0]
    names={}
    for p in (project_root/'Data/Names').glob('*.json'):
        for item in read_json(p).get('Data',[]):
            names[str(item['Key']['data'])]=item['Value']
    checks=[]
    def ck(obj,test,got,want):
        if isinstance(want,(int,float)) and not isinstance(want,bool):
            try: ok=math.isclose(float(got),want,abs_tol=1e-7)
            except (ValueError,TypeError): ok=False
        else: ok=got==want
        checks.append(dict(object=obj,test=test,passed=ok,observed=got,expected=want))
    def nm(i): return names.get(str(i),'<missing-name:'+str(i)+'>')
    nodes=d['StructureItems']; hierarchy=d['HierarchyInfo']
    root=d['RootGroupId']; order=hierarchy[root]['ChildrenIdentities']
    resolution_values=[v for v in d['Settings'].values() if isinstance(v,str) and re.fullmatch('\\d+,\\d+',v)]
    ck(expected_name,'presentation_resolution',resolution_values,['1920,1200'] if geometry else ['1920,1080'])
    expected_order=[e.get('group_name',e.get('stimulus_name',e.get('name'))) for e in expected['elements']]
    #  Calibration may not be renameable; compare it as a native calibration token.
    actual_order=['<CALIBRATION>' if nodes[i]['kind']==3 else nm(i) for i in order]
    exp_order=['<CALIBRATION>' if e['kind']=='calibration' else n for n,e in zip(expected_order,expected['elements'])]
    ck(expected_name,'root_flow_order',actual_order,exp_order)
    ck(expected_name,'calibration_count',sum(nodes[i]['kind']==3 for i in order),1)
    tables={}
    for tid,t in d['Tables'].items():
        cols=[nm(i) for i in t['Columns']]; width=len(cols)
        if not width or len(t['Cells'])%width: raise ValueError('Malformed imported table')
        rows=[dict(zip(cols,t['Cells'][i:i+width])) for i in range(0,len(t['Cells']),width)]
        tables[tid]=(cols,rows)
        ck(nm(tid),'first_11_columns',cols[:11],['article_block','row_type','media_name','DOT_W','DOT_H','DOT_X','DOT_Y','MAIN_W','MAIN_H','MAIN_X','MAIN_Y'])
        for cname,g in geo.items():
            for k,want in g.items():
                col=cname+'_'+k
                bad=[]
                for ri,r in enumerate(rows,2):
                    try: ok=math.isclose(float(r.get(col)),want,abs_tol=1e-7)
                    except (TypeError,ValueError): ok=False
                    if not ok: bad.append(ri)
                ck(nm(tid),col+'_nonmatching_excel_rows',bad,[])
        bad_score=[ri for ri,r in enumerate(rows,2) if r['row_type']=='question' and r['correct_key']!={'__MASKED_TEXT_0054__':'P','__MASKED_TEXT_0058__':'Q'}.get(r['truth_value_ja'])]
        ck(nm(tid),'bad_PQ_mapping_rows',bad_score,[])
    name_index=collections.defaultdict(list)
    for i in order: name_index[nm(i)].append(i)
    seen_containers=[]; total_stim=0
    for e in expected['elements']:
        if e['kind']=='calibration':
            ids=[i for i in order if nodes[i]['kind']==3]
            if len(ids)==1:
                c=nodes[ids[0]]['data']
                for k,want in {'UseValidation':True,'RandomizeTargetOrder':True,'NumberOfTargets':9,'TargetType':0,'Background':-1}.items(): ck(e['name'],k,c.get(k),want)
                for k,want in {'CalibrationType':0,'TargetColor':-16777216}.items(): ck(e['name'],k,c.get('PointCalibrationSettings',{}).get(k),want)
            continue
        ename=e.get('group_name',e.get('stimulus_name')); matches=name_index[ename]
        ck(ename,'unique_active_element',len(matches),1)
        if len(matches)!=1: continue
        eid=matches[0]; active_rows=None
        if e['kind']=='group':
            children=hierarchy[eid]['ChildrenIdentities']; ck(ename,'one_template',len(children),1)
            if len(children)!=1: continue
            sid=children[0]; ck(ename,'template_name',nm(sid),e['stimulus_name'])
            ops=[d['DataFlowOperations'][x] for x in d['DataFlows'][eid]['OperationIdentities']]
            ck(ename,'table_operation_kinds',sorted(x['kind'] for x in ops),[1,2,2])
            refs=[x['data']['TableReference'] for x in ops if x['kind']==1]
            ck(ename,'table_reference_count',len(refs),1)
            if len(refs)!=1 or refs[0] not in tables: continue
            tid=refs[0]; ck(ename,'table_name',nm(tid),'Tobii_Design')
            subsets=[{'column':nm(o['data']['ColumnId']),'values':o['data']['SelectedValues'],'set_at_recording_start':o['data']['SelectPerRecording']} for o in ops if o['kind']==2]
            ck(ename,'subsets',sorted(subsets,key=lambda x:x['column']),sorted(e['subsets'],key=lambda x:x['column']))
            cols,rows=tables[tid]
            active_rows=[r for r in rows if all(r.get(s['column']) in s['values'] for s in subsets)]
            for key in ['event_id','media_name','row_type','article_block','correct_key']:
                ck(ename,'expanded_'+key,[r[key] for r in active_rows],[r[key] for r in e['expected_events']])
        else: sid=eid
        ck(ename,'native_stimulus_kind',nodes[sid]['kind'],2)
        st=nodes[sid]['data']; preset=expected['presets'][e['preset']]; total_stim+=1
        ck(ename,'time_mode',st.get('TimeTrigger',{}).get('Mode'),0)
        ck(ename,'min_time_enabled',st.get('MinPresentationTime',{}).get('Enabled'),True)
        ck(ename,'min_time_100ms',st.get('MinPresentationTime',{}).get('Duration',{}).get('FixedValue'),'00:00:00.1000000')
        ck(ename,'keyboard_enabled',st.get('KeyboardTrigger',{}).get('IsEnabled'),preset['key_press_enabled'])
        keys=st.get('KeyboardTrigger',{}).get('Pattern','')
        #  Inspect known serialized delimiters; live testing still required, especially Q/P and operator 7.
        keys=sorted(k.lower() for k in re.split('[|,;\\s]+',keys.strip()) if k)
        ck(ename,'keyboard_keys',keys,sorted(k.lower() for k in preset['keys']))
        for key,want in [('ShowCursor',False),('StimulusAdvanceOnMouseMode',0),('Background',-16777216)]: ck(ename,key,st.get(key),want)
        ck(ename,'lookaway_disabled',st.get('LookAwayTrigger',{}).get('IsEnabled'),False)
        ck(ename,'media_end_disabled',st.get('MediaEndTrigger',{}).get('IsDisabled'),True)
        ck(ename,'ttl_disabled',st.get('TtlOutMarker',{}).get('Enabled'),False)
        cids=hierarchy[sid]['ChildrenIdentities']; ck(ename,'container_count',len(cids),len(e['containers']))
        seen_containers.extend(cids)
        for c in e['containers']:
            matches=[i for i in cids if nm(i).split('_')[0]==c['name']]
            ck(ename,c['name']+'_container_unique',len(matches),1)
            if len(matches)!=1: continue
            ci=matches[0]; cd=nodes[ci]['data']; obj=ename+'/'+nm(ci)
            ck(obj,'kind',nodes[ci]['kind'],5)
            ck(obj,'Original_MediaScaleBehavior',cd.get('MediaScaleBehavior'),1)
            ck(obj,'mouse_none',cd.get('AdvanceOnMouseMode'),0)
            gaze=cd.get('GazeTrigger',{}); ck(obj,'gaze_mode',gaze.get('Mode'),1 if c['name']=='DOT' else 0)
            if c['name']=='DOT':
                ck(obj,'continuous_threshold_us',gaze.get('ContinuousGazeTriggerSetup',{}).get('Threshold'),300000)
                ck(obj,'continuous_data_loss_reset_us',gaze.get('ContinuousGazeTriggerSetup',{}).get('ResetTime'),34000)
            for field,key in [('Width','W'),('Height','H'),('X','X'),('Y','Y')]:
                prop=cd[field]; bind=d['Bindings'].get(prop['Id'])
                wanted_binding=c['layout_bindings'].get(key)
                ck(obj,field+'_bound_column',nm(bind['ColumnId']) if bind else None,wanted_binding)
                if bind:
                    bcols,brows=tables[bind['TableId']]; col=nm(bind['ColumnId'])
                    vals=[r[col] for r in brows]
                    ok=all(v is not None and math.isclose(float(v),geo[c['name']][key],abs_tol=1e-7) for v in vals)
                    ck(obj,field+'_effective_all_table_values',ok,True)
                else: ck(obj,field+'_effective_fixed',prop.get('FixedValue'),geo[c['name']][key])
            prop=cd['MediaId']; bind=d['Bindings'].get(prop['Id'])
            ck(obj,'source_bound_column',nm(bind['ColumnId']) if bind else None,'media_name' if c['source_mode']=='bind_column' else None)
            if c['source_mode']=='fixed_media': ck(obj,'fixed_media_source',nm(prop.get('FixedValue')),c['source_value'])
            else:
                library={nm(i) for i in d['MediaLibrary']}
                ck(obj,'missing_active_media',sorted({r['media_name'] for r in (active_rows or [])}-library),[])
    #  Names/size/timing cannot verify actual render order, effective AOI switches in every schema, live gaze, or registration geometry.
    failed=[c for c in checks if not c['passed']]
    return {'expected_project':expected_name,'design_snapshot':str(design_path),'static_scope':'Known 25.7 serialized fields; no private writes',
            'status':'STATIC_CHECKS_PASSED_NOT_HARDWARE_VERIFIED' if not failed else 'STATIC_CHECKS_FAILED',
            'checked_stimuli':total_stim,'checked_containers':len(set(seen_containers)),
            'check_count':len(checks),'failure_count':len(failed),'failures':failed,'checks':checks,
            'not_verified':['actual Windows presentation monitor/scaling/native signal','screen physical dimensions and tracker mounting geometry',
                            'real rendering, image order and alpha behavior','Use as AOI toggle for all schema versions',
                            'calibration quality and local accuracy','actual trigger/keyboard behavior','sampling and display timing','recording completeness']}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project-root',required=True,type=Path)
    ap.add_argument('--expected-project',required=True)
    ap.add_argument('--expectations',type=Path,default=Path(__file__).with_name('EXPECTED_PROJECTS_QA_ONLY.json'))
    ap.add_argument('--version',default='Current',choices=['Current','0'])
    ap.add_argument('--output',required=True,type=Path)
    a=ap.parse_args()
    root=a.project_root.resolve(); out=a.output.resolve()
    if out==root or root in out.parents: raise ValueError('Output must be outside input project directory')
    result=inspect(root,a.expected_project,read_json(a.expectations),a.version)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','check_count','failure_count','checked_stimuli','checked_containers']},ensure_ascii=False))
    raise SystemExit(0 if not result['failure_count'] else 2)


if __name__=='__main__': main()
