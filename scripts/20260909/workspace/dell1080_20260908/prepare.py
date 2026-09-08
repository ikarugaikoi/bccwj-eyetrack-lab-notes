import json, hashlib, zipfile, shutil, xml.etree.ElementTree as ET
from pathlib import Path, PurePosixPath
ROOT=Path(__file__).resolve().parent
AUTO=ROOT.parent/'local_automation'
BRIDGE=AUTO/'bridge'
PACKAGE=ROOT.parent/'review_dell1080_20260908/BCCWJ_TOBII_FULL_20260908_DELL1080_56CM_120HZ'
TRANSFER=BRIDGE/'dell1080_transfer/DELL1080_20260908'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
assert not (ROOT/'queue.json').exists()
plan=read(PACKAGE/'04_PROJECT_BLUEPRINTS/SELECTED_BUILD_PLAN.json')
old=read(AUTO/'recipes/production_queue.json')
oldmap={x['project']:x for x in old['jobs']}
jobs=[]
for p in plan['jobs']:
    name=p['project_name']
    short=name.replace('BCCWJ_EyeTrack_PRACTICE_','D1080_PR_').replace('BCCWJ_EyeTrack_FORMAL_','D1080_').replace('_FROM_','_')
    job=dict(sequence=p['build_sequence'],planned=name,actual=short,language=p['language'],status='pending',guest_path='__MASKED_LOCAL_PATH_0385__'+short,source_path='__MASKED_LOCAL_PATH_0385__'+name,blueprint=p,source_backup_sha256=None)
    if p['language']=='ZH':
        archive=BRIDGE/'native_backups'/(name+'.zip')
        digest=sha(archive)
        assert digest==oldmap[name]['backup_sha256'] and oldmap[name]['status']=='static_verified'
        with zipfile.ZipFile(archive) as z:
            assert z.testzip() is None
            assert not any('/Recordings/' in n for n in z.namelist() if not n.endswith('/'))
            for n in z.namelist():
                if '/Participants/' in n and not n.endswith('/'):
                    participant=ET.fromstring(z.read(n))
                    assert participant.findtext('Name')=='Participant1' and len(participant.find('Properties'))==0
            rootnames={PurePosixPath(n).parts[0] for n in z.namelist()}
            assert rootnames=={name}
            for n in z.namelist():
                target=TRANSFER/'Projects'/n
                assert target.resolve().is_relative_to((TRANSFER/'Projects').resolve())
            z.extractall(TRANSFER/'Projects')
        job['source_backup_sha256']=digest
    jobs.append(job)
assert len(jobs)==84 and len({j['actual'] for j in jobs})==84
shutil.copytree(PACKAGE,TRANSFER/'Materials')
for d in ['logs','qa','backups','snapshots']: (ROOT/d).mkdir(exist_ok=True)
dump(ROOT/'queue.json',{'total':84,'static_verified':0,'remaining':84,'guest_root':'__MASKED_LOCAL_PATH_0386__','jobs':jobs})
dump(ROOT/'name_mapping.json',[{k:j[k] for k in ('sequence','planned','actual','language','guest_path')} for j in jobs])
scope=read(BRIDGE/'scope.json')
shutil.copy2(BRIDGE/'scope.json',ROOT/'scope_before.json')
scope['allowed_project_names']=sorted(set(scope['allowed_project_names']+[j['actual'] for j in jobs]))
scope['test_project_paths']=sorted(set(scope['test_project_paths']+[p for j in jobs for p in (j['guest_path'],j['source_path'])]))
dump(BRIDGE/'scope.json',scope)
print(json.dumps({'jobs':84,'max_name_length':max(len(j['actual']) for j in jobs),'staged_zh':42,'transfer':str(TRANSFER),'bytes':sum(p.stat().st_size for p in TRANSFER.rglob('*') if p.is_file())}))
