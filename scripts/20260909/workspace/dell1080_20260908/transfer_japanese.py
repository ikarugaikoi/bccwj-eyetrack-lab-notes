'Copy 42 new native ZH exports into guest JA staging folders via native picker.\n\nUses the existing authorized UI executor; no private project edits.\nRun only after prepare_japanese.py and all 42 ZH jobs pass.\n'
import argparse,json
import build
ap=argparse.ArgumentParser();ap.add_argument('--selection-ready',action='store_true');args=ap.parse_args()

q=build.queue()
assert all(j['status']=='static_verified' for j in q['jobs'] if j['language']=='ZH')
jobs=[j for j in q['jobs'] if j['language']=='JA'];assert len(jobs)==42
expected={j['planned'] for j in jobs}
transfer=build.BRIDGE/'dell1080_japanese_transfer'
assert {p.name for p in transfer.iterdir()}==expected
assert not (build.ROOT/'logs/japanese_transfer_complete.json').exists()
if args.selection_ready:
    main_hwnd=next(w['hwnd'] for w in build.command('windows') if w['title']=='Tobii Pro Lab')
    d=build.exact_dialog('Import media into Media Library')
else:
    u=build.main_ui();main_hwnd=u.hwnd
    u.act('click',{'automation_id':'designerNavigationButton'})
    build.set_panel(u,'MediaLibrary',True)
    u.act('invoke',{'automation_id':'SwitchableViewListBoxImportButton','type':'Button'})
    d=build.exact_dialog('Import media into Media Library')
    d.act('set_value',{'automation_id':'1148','type':'Edit'},value='__MASKED_LOCAL_PATH_0556__')
    d.act('invoke',{'automation_id':'1','type':'Button'})
    visible=[e for e in d.s['elements'] if e['type']=='ListItem' and e['visible'] and e['name'] in expected]
    assert visible,'No staged JA folders observed'
    d.act('click',{'id':visible[0]['id']});d.act('key',key='CTRL_A')
selected=set();selection_views=[]
for attempt in range(8):
    current={e['name'] for e in d.s['elements'] if e['type']=='ListItem' and e.get('selected')==1}
    assert current<=expected
    selected|=current;selection_views.append(d.s)
    if selected==expected:break
    view=build.find(d.s,type='List',**{'class':'UIItemsView'})['rect']
    d.act('scroll',x=int((view[0]+view[2])/2-d.s['rect'][0]),y=int((view[1]+view[3])/2-d.s['rect'][1]),notches=-4)
build.write(build.ROOT/'logs/japanese_copy_selection.json',selection_views)
assert selected==expected,('Unexpected copy selection',sorted(selected))
d.act('key',key='CTRL_C')
d.act('set_value',{'automation_id':'1148','type':'Edit'},value=build.GUEST+'\\Projects')
d.act('invoke',{'automation_id':'1','type':'Button'})
build.write(build.ROOT/'logs/japanese_copy_destination.json',d.s)
assert not any(e['type']=='ListItem' and e['name'] in expected for e in d.s['elements']),'JA destination folders already exist; inspect before retrying'
d.act('focus',{'type':'List','class':'UIItemsView'})
print('Copying 42 new Japanese source folders into independent guest Projects directory',flush=True)
d.act('key',key='CTRL_V',timeout=600)
u=build.submit_dialog(d,main_hwnd,'2')
build.set_panel(u,'MediaLibrary',False)
evidence=[]
for j in jobs:
    d,n,p=build.read_design(j['source_path'])
    assert d==build.read_backup_design(build.source_for_job(j))
    evidence.append(dict(project=j['actual'],source_path=j['source_path'],native_snapshot=p,source_sha256=build.sha(build.source_for_job(j))))
build.write(build.ROOT/'logs/japanese_transfer_complete.json',evidence)
print('All 42 guest Japanese source designs are readable and exactly match their newly verified Chinese sources',flush=True)
