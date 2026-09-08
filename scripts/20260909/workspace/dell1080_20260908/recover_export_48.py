'Finish the existing successful export; never repeat the export action.'
from build import *
job=queue()['jobs'][47]
assert job['actual']=='D1080_BA_H2_JA' and job['stage']=='reopened'
target=BRIDGE/'native_backups'/(job['actual']+'.zip')
destination=ROOT/'backups'/target.name
assert target.exists() and not destination.exists()
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    assert not any('/Recordings/' in n for n in z.namelist() if not n.endswith('/'))
d=exact_dialog('ExportProjectDialogWindowCaption')
assert any(e['automation_id']=='ExportDoneShowInFolderButton' and e['visible'] for e in d.s['elements'])
assert any(e.get('name')==job['actual'] for e in d.s['elements'])
u=submit_dialog(d,8913096,'DialogCancelButton')
shutil.copy2(target,destination)
subprocess.run([sys.executable,str(ROOT/'audit_full_backup.py'),str(target),'--package',str(PACKAGE),'--expected',job['planned'],'--actual',job['actual'],'--report',str(ROOT/'qa'/(job['actual']+'_full_backup.json')),'--accept-record',str(RECORD)],check=True)
audit=json.loads((ROOT/'qa'/(job['actual']+'_native_accepted.json')).read_text(encoding='utf-8'))
assert audit['failure_count']==0
write(ROOT/'logs/export_48_recovery.json',dict(project=job['actual'],reason='Export completion appeared before Close was available; fresh observation confirmed completed export and enabled Close',backup_sha256=sha(target),zip_crc='PASS',export_repeated=False))
stage(job,'verified',backup=str(destination),backup_sha256=sha(target),checks=audit['check_count'])
log(job,'Existing export verified; resumed without repeating export',status='project_verified',completed=queue()['static_verified'])
