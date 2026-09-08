'Stage byte-exact copies of the 42 newly verified Chinese native exports.'
import json,zipfile
from pathlib import Path
from build import ROOT,BRIDGE,queue,sha
q=queue();assert all(j['status']=='static_verified' for j in q['jobs'] if j['language']=='ZH')
target=BRIDGE/'dell1080_japanese_transfer'
assert not target.exists()
target.mkdir()
for job in q['jobs']:
    if job['language']!='JA':continue
    source=job['actual'][:-3]+'_ZH'
    source_job=next(j for j in q['jobs'] if j['actual']==source)
    archive=ROOT/'backups'/(source+'.zip');assert sha(archive)==source_job['backup_sha256']
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for entry in z.infolist():
            parts=Path(entry.filename).parts;assert parts[0]==source
            dest=target/job['planned']/Path(*parts[1:]);assert dest.resolve().is_relative_to(target.resolve())
            if entry.is_dir():dest.mkdir(parents=True,exist_ok=True)
            else:dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(entry))
    job['source_backup_sha256']=source_job['backup_sha256']
(ROOT/'queue.json').write_text(json.dumps(q,ensure_ascii=False,indent=2),encoding='utf-8')
print('42 verified Chinese copies prepared for Japanese instruction replacement:',target)
