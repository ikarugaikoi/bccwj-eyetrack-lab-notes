# !__MASKED_LOCAL_PATH_0917__
'Release checks + independent ZIP extraction test; no native project writes.'
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile

from assemble_package import PROFILE, LAYOUT, refresh_manifest, read, write, digest


def verify(p):
    proc=subprocess.run([sys.executable,str(p/'05_QA/verify_package.py')],check=True,
                        capture_output=True,text=True,cwd=tempfile.gettempdir())
    return json.loads(proc.stdout)


def extra_checks(p):
    params=read(p/'03_SPEC/BUILD_PARAMETERS.json')
    assert params['profile_id']==PROFILE and params['layout']==LAYOUT
    assert params['presentation_resolution']==[1920,1080]
    assert params['eye_midpoint_to_screen_plane_target_mm']==560
    assert params['recording_frequency_target_hz']==120
    assert params['tracker_model_confirmed_by_lab'] is True
    assert params['actual_display_verified'] is False and params['native_hardware_verification_done'] is False
    spec=read(p/'05_QA/EXPECTED_PROJECTS_QA_ONLY.json')
    assert spec['geometry']==LAYOUT
    idx={x['project']:x for x in spec['projects']}
    n=0
    for lang in ['ZH','JA']:
        projects=read(p/f'04_PROJECT_BLUEPRINTS/PROJECTS_{lang}.json')['projects']
        for project in projects:
            expected=idx[project['bilingual_project_name']]
            assert expected['elements']==project['elements']
            assert expected['presets']==params['presets']
            assert expected['expected_display']==[1920,1080]
            for e in project['elements']:
                for c in e.get('containers',[]):
                    assert c['layout']==LAYOUT[c['name']]
                    n+=1
    assert n==1292
    plan=read(p/'04_PROJECT_BLUEPRINTS/SELECTED_BUILD_PLAN.json')
    for j in plan['jobs']:
        assert j['profile_id']==PROFILE and j['workbook_sha256']==digest(p/j['workbook_path'])
    progress=read(p/'05_QA/BUILD_PROGRESS_TEMPLATE.json')
    for j in progress['projects']:
        for k in ['native_saved','static_verified','export_verified']:
            assert j[k]=='not_started',(k,j)
    geometry=read(p/'03_SPEC/DISPLAY_GEOMETRY.json')
    now=[d for d in geometry['distance_sensitivity'] if d['role']=='current_target']
    assert len(now)==1 and now[0]['eye_to_screen_plane_mm']==560
    assert abs(now[0]['character_x_deg']-.8986386)<1e-6
    assert geometry['normalized']==LAYOUT
    return {'parameter_blueprint_checker_consistency':'PASS','containers_checked':n,
            'project_table_hashes_checked':84,'distance_recalculation':'PASS',
            'all_native_progress_blank':True}


def package_zip(p,target):
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for f in sorted(p.rglob('*')):
            if f.is_file() and '__pycache__' not in f.parts and f.name!='.DS_Store':
                assert not f.is_symlink()
                z.write(f,Path(p.name)/f.relative_to(p))


def extracted_verify(zip_path,name):
    with tempfile.TemporaryDirectory(prefix='bccwj_release_extract_') as tmp:
        with zipfile.ZipFile(zip_path) as z:
            assert z.testzip() is None
            for entry in z.infolist():
                rel=Path(entry.filename)
                assert not rel.is_absolute() and '..' not in rel.parts
            z.extractall(tmp)
        return verify(Path(tmp)/name)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--package',type=Path,required=True)
    ap.add_argument('--checker-report',type=Path,required=True)
    args=ap.parse_args();p=args.package.resolve()
    check=read(args.checker_report)
    assert check['tests_passed'] and len(check['cases'])==11 and check['native_project_writes']==0
    write(p/'06_REFERENCE_DO_NOT_IMPORT/NATIVE_CHECKER_REGRESSION.json',check)
    supplemental=extra_checks(p)
    refresh_manifest(p)
    verify(p)
    #  Reconstruction from only the supplied package, including frozen old table
    #  inputs and approved pixels. No original Mac source tree is passed in.
    with tempfile.TemporaryDirectory(prefix='bccwj_source_rebuild_') as tmp:
        dest=Path(tmp)/'REASSEMBLED';(dest/'02_DESIGN_TABLES').mkdir(parents=True)
        for table in (p/'02_DESIGN_TABLES').glob('*.xlsx'):
            shutil.copy2(table,dest/'02_DESIGN_TABLES'/table.name)
        src=p/'08_BUILD_SOURCE'
        command=[sys.executable,str(src/'assemble_package.py'),'--baseline',str(src/'baseline_inputs'),
                 '--audit',str(src/'audit_inputs'),'--assets',str(p),'--out',str(dest)]
        subprocess.run(command,check=True,capture_output=True,text=True,cwd=tmp)
        smoke=verify(dest)
        for folder in ['01_MEDIA','02_DESIGN_TABLES','04_PROJECT_BLUEPRINTS']:
            for f in (p/folder).rglob('*'):
                if f.is_file():assert digest(f)==digest(dest/f.relative_to(p)),str(f)
    report={'status':'PASS_MAC_MATERIALS_ONLY','profile_id':PROFILE,'supplemental':supplemental,
            'source_reassembly_without_old_mac_tree':'PASS','reassembly_verify':smoke,
            'native_checker_regression_cases':11,'native_projects_built':0,
            'hardware_verified':False,'reassembly_note':'Used supplied final XLSX plus frozen baseline metadata and supplied PNG/AOI only; Node authoring independently performed on Mac and saved-XLSX reimported for visual review.'}
    write(p/'06_REFERENCE_DO_NOT_IMPORT/RELEASE_QA.json',report)
    refresh_manifest(p)
    result=verify(p)
    write(p/'06_REFERENCE_DO_NOT_IMPORT/PACKAGE_VERIFY_RESULT.json',result)
    refresh_manifest(p)
    target=p.with_suffix('.zip')
    package_zip(p,target)
    extraction=extracted_verify(target,p.name)
    receipt={'archive':target.name,'bytes':target.stat().st_size,'sha256':digest(target),
             'archive_crc':'PASS','fresh_extraction_independent_cwd':extraction,
             'old_source_unchanged':read(p/'06_REFERENCE_DO_NOT_IMPORT/PACKAGE_BUILD_CHECKS.json')['old_package_hashes_unchanged'],
             'native_projects_built':0,'hardware_verified':False}
    write(p.with_name(p.name+'_RECEIPT.json'),receipt)
    print(json.dumps(receipt,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
