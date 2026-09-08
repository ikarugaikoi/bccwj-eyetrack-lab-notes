"""DELL publication extract: retained function implementations are unchanged."""
from ui import find


def descendants(s, root):
    ids = {root}
    for e in s['elements']:
        if e['id'] in ids or e['parent'] in ids:
            ids.add(e['id'])
            yield e


def verify_container_ui(u):
    p=find(u.s, automation_id='ContainerPropertiesTool')['id']
    es=list(descendants(u.s,p))
    aoi=[e for e in es if e['parent']==p and e['type']=='Button' and e['automation_id']=='' and 'toggle' in e]
    if len(aoi)!=1 or aoi[0]['toggle']!=0:
        raise AssertionError('Container AOI is not verified off')
    if find(u.s,automation_id='ContainerScaleOriginal').get('selected')!=1:
        raise AssertionError('Original scale is not selected')
    return {'name':find(u.s,automation_id='NameProperty')['value'],'aoi_off':True,'original':True}


def set_panel(u, aid, expanded):
    p=find(u.s,automation_id=aid)['id']
    e=find(u.s,parent=p,automation_id='HeaderSite')
    if e.get('toggle') != int(expanded):
        u.act('set_toggle',{'id':e['id']},value=int(expanded))


def open_editor(u, name):
    u.act('select',{'automation_id':name,'type':'Custom'})
    p=find(u.s,automation_id=name,type='Custom')['id']
    e=next(e for e in descendants(u.s,p) if e['automation_id']=='openEditorButton')
    u.act('invoke',{'id':e['id']})
    return u
