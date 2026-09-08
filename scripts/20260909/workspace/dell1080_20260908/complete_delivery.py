'Verify the repaired delivery helper and seal the final package.'
import hashlib,json,shutil,subprocess,time,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
folder=ROOT/'delivery/BCCWJ_DELL1080_84'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report_path=ROOT/'DELIVERY_VERIFICATION.json'
result=json.loads(report_path.read_text(encoding='utf-8'))
out=Path(result['path']);assert sha(out)==result['sha256']
old_result=dict(result)
base=['powershell.exe','-NoProfile','-NonInteractive','-ExecutionPolicy','Bypass','-File',str(folder/'Restore-Projects.ps1')]
target=ROOT/'restore_test';assert not target.exists()
log=ROOT/'logs/restore_verify_final.txt'
with log.open('w',encoding='utf-8') as f:
    subprocess.run([*base,'-VerifyOnly'],check=True,stdout=f,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
    subprocess.run([*base,'-ProjectName','D1080_PR_A_ZH','-Destination',str(target)],check=True,stdout=f,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
with zipfile.ZipFile(folder/'NATIVE_BACKUPS/D1080_PR_A_ZH.zip') as z:
    members=[n for n in z.namelist() if not n.endswith('/')]
    for n in members:
        p=(target/n).resolve();assert p.is_relative_to(target.resolve())
        assert hashlib.sha256(p.read_bytes()).digest()==hashlib.sha256(z.read(n)).digest()
verification=dict(native_project_count=84,restore_script_verify_all='PASS',restore_smoke_test_byte_equality='PASS',restored_file_count=len(members),helper_revision='SHA256 via .NET stream, avoiding optional Get-FileHash command dependency')
(folder/'RESTORE_VERIFICATION.json').write_text(json.dumps(verification,indent=2),encoding='utf-8')
shutil.copy2(log,folder/'QA/restore_verify_final.txt')
shutil.copy2(folder/'BUILD_STATUS.md',ROOT/'BUILD_STATUS.md')
files=sorted(p for p in folder.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt')
(folder/'SHA256SUMS.txt').write_text(''.join(sha(p)+'  '+p.relative_to(folder).as_posix()+'\n' for p in files),encoding='utf-8')
temporary=ROOT/'delivery/BCCWJ_DELL1080_84_20260908.sealed.zip';assert not temporary.exists()
with zipfile.ZipFile(temporary,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
    for p in sorted(folder.rglob('*')):
        if p.is_file():z.write(p,arcname=folder.name+'/'+p.relative_to(folder).as_posix(),compress_type=zipfile.ZIP_STORED if p.suffix=='.zip' else zipfile.ZIP_DEFLATED)
with zipfile.ZipFile(temporary) as z:
    assert z.testzip() is None
    root=folder.name+'/'
    listed=set()
    for line in z.read(root+'SHA256SUMS.txt').decode('utf-8').splitlines():
        expected,name=line.split('  ',1);listed.add(root+name)
        assert hashlib.sha256(z.read(root+name)).hexdigest()==expected,name
    assert listed|{root+'SHA256SUMS.txt'}==set(z.namelist())
    manifest=json.loads(z.read(root+'MANIFEST.json'))
    assert len(manifest['projects'])==84 and len({p['project'] for p in manifest['projects']})==84
history=ROOT/'delivery_history';history.mkdir(exist_ok=True)
previous=history/'BCCWJ_DELL1080_84_20260908_before_helper_fix.zip';assert not previous.exists()
assert out.resolve().parent==Path('__MASKED_LOCAL_PATH_0294__').resolve()
assert previous.resolve().is_relative_to(ROOT.resolve())
shutil.move(str(out),str(previous));assert sha(previous)==old_result['sha256']
shutil.copy2(temporary,out);assert sha(out)==sha(temporary)
result.update(verification,path=str(out),bytes=out.stat().st_size,sha256=sha(out),zip_crc='PASS',all_packaged_sha256='PASS',packaged_file_count=len(listed)+1,previous_draft=dict(path=str(previous),sha256=old_result['sha256']))
report_path.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'logs/pipeline_status.json').write_text(json.dumps(dict(time=time.time(),step='COMPLETE',delivery=result),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=True))
