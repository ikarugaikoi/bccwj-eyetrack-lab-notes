'Continue the authorized local pipeline after the existing ZH worker exits.\n\nOnly one worker operates Pro Lab at a time; stop on every nonzero exit.\n'
import argparse,json,subprocess,sys,time,traceback,zipfile,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--wait-pid',type=int);ap.add_argument('--resume-japanese',action='store_true');a=ap.parse_args()
def status(step,**extra):
    obj=dict(time=time.time(),step=step,**extra)
    (ROOT/'logs/pipeline_status.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(obj,ensure_ascii=True),flush=True)
def run(script,*args):
    status(script)
    subprocess.run([sys.executable,str(ROOT/script),*args],check=True)
try:
    if not a.resume_japanese:
        assert a.wait_pid is not None,'Provide --wait-pid or --resume-japanese'
        status('Waiting for the active Chinese worker to exit',pid=a.wait_pid)
        subprocess.run(['powershell.exe','-NoProfile','-NonInteractive','-Command',f'Wait-Process -Id {a.wait_pid} -ErrorAction SilentlyContinue'],creationflags=subprocess.CREATE_NO_WINDOW)
    q=json.loads((ROOT/'queue.json').read_text(encoding='utf-8'))
    assert all(j['status']=='static_verified' for j in q['jobs'] if j['language']=='ZH'),'Chinese worker ended before all 42 passed; inspect its error'
    if not a.resume_japanese:
        run('prepare_japanese.py')
        run('transfer_japanese.py')
    else:
        transferred=json.loads((ROOT/'logs/japanese_transfer_complete.json').read_text(encoding='utf-8'))
        assert len(transferred)==42
    run('build.py','--start','43','--end','84')
    run('finalize_delivery.py')
    folder=ROOT/'delivery/BCCWJ_DELL1080_84'
    script=folder/'Restore-Projects.ps1'
    status('Verify all 84 portable native backups and test restoring one')
    base=['powershell.exe','-NoProfile','-NonInteractive','-ExecutionPolicy','Bypass','-File',str(script)]
    with (ROOT/'logs/restore_verify.txt').open('w',encoding='utf-8') as f:
        subprocess.run([*base,'-VerifyOnly'],check=True,stdout=f,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
        target=ROOT/'restore_test'
        assert not target.exists()
        subprocess.run([*base,'-ProjectName','D1080_PR_A_ZH','-Destination',str(target)],check=True,stdout=f,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW)
    with zipfile.ZipFile(folder/'NATIVE_BACKUPS/D1080_PR_A_ZH.zip') as z:
        for n in z.namelist():
            if n.endswith('/'):continue
            p=(target/n).resolve();assert p.is_relative_to(target.resolve())
            assert hashlib.sha256(p.read_bytes()).digest()==hashlib.sha256(z.read(n)).digest()
    result_path=ROOT/'DELIVERY_VERIFICATION.json'
    result=json.loads(result_path.read_text(encoding='utf-8'));result.update(restore_script_verify_all='PASS',restore_smoke_test_byte_equality='PASS')
    result_path.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    status('COMPLETE',delivery=result)
except Exception as exc:
    status('STOPPED_FOR_REVIEW',error=str(exc),trace=traceback.format_exc())
    raise
