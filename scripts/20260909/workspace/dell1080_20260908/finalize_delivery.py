'Package only the 84 accepted native UI exports and their audit evidence.'
import csv,hashlib,json,shutil,zipfile
from pathlib import Path
from build import ROOT,queue,sha,PACKAGE
from acceptance import policy,RECORD

q=queue();assert len(q['jobs'])==84 and q['static_verified']==84
assert all(j['status']=='static_verified' for j in q['jobs'])
approval=policy()
source_zip=Path('__MASKED_LOCAL_PATH_0295__')
source_sha=json.loads(RECORD.read_text(encoding='utf-8'))['source_package_sha256']
assert sha(source_zip)==source_sha
dest=ROOT/'delivery/BCCWJ_DELL1080_84'
assert not dest.exists(),'Refusing to replace an existing delivery'
dest.mkdir(parents=True)
for sub in ['NATIVE_BACKUPS','QA','SPEC']:(dest/sub).mkdir()
shutil.copy2(source_zip,dest/'SPEC'/source_zip.name)
projects=[]
for j in q['jobs']:
    p=ROOT/'backups'/(j['actual']+'.zip')
    assert sha(p)==j['backup_sha256']
    with zipfile.ZipFile(p) as z:
        assert z.testzip() is None
        assert not any('/Recordings/' in n for n in z.namelist() if not n.endswith('/'))
        assert all(n.startswith(j['actual']+'/') for n in z.namelist())
        assert j['actual']+'/tobii.project' in z.namelist()
    for ending in ['_native_accepted.json','_full_backup_accepted.json']:
        report=json.loads((ROOT/'qa'/(j['actual']+ending)).read_text(encoding='utf-8'))
        assert report.get('failure_count',0)==0 and report.get('passed',True)
        assert report['acceptance']['sha256']==approval['sha256']
    shutil.copy2(p,dest/'NATIVE_BACKUPS'/p.name)
    for report in (ROOT/'qa').glob(j['actual']+'_*.json'):
        if 'REVIEW' in report.name or 'precision_review' in report.name:continue
        shutil.copy2(report,dest/'QA'/report.name)
    projects.append(dict(project=j['actual'],blueprint_project=j['planned'],language=j['language'],sequence=j['sequence'],kind=j['blueprint']['kind'],backup='NATIVE_BACKUPS/'+p.name,backup_sha256=sha(p),bytes=p.stat().st_size,guest_path=j['guest_path'],status='STATIC_VERIFIED_WITH_APPROVED_DOT_ROUNDING',hardware_status='PENDING_LAB'))
manifest=dict(project_count=84,projects=projects,acceptance=approval,scope='ZH42 then JA42 cloned from corresponding verified ZH; new DELL1080 directory',original_material_zip_sha256=source_sha)
(dest/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
with (dest/'PROJECT_INDEX.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(projects[0]));w.writeheader();w.writerows(projects)
for name in ['ACCEPTED_DEVIATION.json','PRECISION_INCIDENT.md','name_mapping.json','BUILD_STATUS.md']:
    shutil.copy2(ROOT/name,dest/name)
(dest/'BUILD_STATUS.md').write_text('# 最终状态\n\n84/84 工程完成软件静态验收及完整原生导出（中文42、日文42），含明确批准的DOT导入舍入差异。现场硬件验收待实验室执行。\n\n最新逐工程结果见 MANIFEST.json 与 QA，实际短名称见 PROJECT_INDEX.csv。原制作过程阶段日志留在物理机工作目录。\n',encoding='utf-8')
shutil.copy2(ROOT/'qa/import_formatter_evidence.json',dest/'QA/import_formatter_evidence.json')
for source in ['03_SPEC/REBUILD_REQUIREMENTS.md','03_SPEC/BUILD_PARAMETERS.json','05_QA/ACCEPTANCE_CHECKLIST.md','05_QA/ONSITE_CHECKLIST.md']:
    p=PACKAGE/source
    if p.exists():shutil.copy2(p,dest/'SPEC'/p.name)
restore=ROOT/'Restore-Projects.ps1'
shutil.copy2(restore,dest/'Restore-Projects.ps1')
readme='# BCCWJ DELL1080：84份新工程\n\n中文42份（练习2、正式8、续跑32），日文42份对应复制。所有工程在虚拟机 Pro Lab 25.7.1400 中配置、保存、重新打开、静态核查并完整原生导出。无实验录制。\n\n虚拟机位置：__MASKED_LOCAL_PATH_0296__\n\n## 在实验室恢复\n\n1. 将整个外层压缩包解压到一个新的独立文件夹。\n2. 用 Restore-Projects.ps1 恢复原生工程；脚本默认输出到此包的 PROJECTS 子目录，已有同名目标会停止，不覆盖旧项目。也可逐个解压 NATIVE_BACKUPS 中所需工程，保留其目录层级。\n3. 在 Pro Lab 中 Browse 打开相应目录内的 tobii.project。\n\nPowerShell 可先运行 `powershell -ExecutionPolicy Bypass -File .\\Restore-Projects.ps1 -VerifyOnly` 校验，再去掉 `-VerifyOnly` 恢复。脚本仅校验并逐字节解压原生导出，不改数据库结构或实验设置。\n\n## 本版显示及已接受差异\n\n目标被试屏1920×1080、100%缩放，MAIN为W/H/X/Y=1/1/0/0、Original，无旧1200p上下60px留边。正文图片、字号、分页和AOI参考没有重新生成。\n\nPro Lab 的 Design Table 导入将 DOT_H 0.07777778 存为0.0778，将 DOT_Y 0.06666667 存为0.0667。对应高度84.024px、Y=72.036px，底边约156.060px。用户已明确接受这一最大约0.06px偏差；原Mac表不改，完整记录见 ACCEPTED_DEVIATION.json。QA 中保留原始八位要求下的失败报告，另有 `_accepted.json` 报告；不能把原始失败报告误当成其他设置未通过，也不能把接受记录扩展到其他数值变化。\n\n本包是新1080p配置，与9月7日1920×1200的pilot分开。新配置理论屏幕到图像offset为(0,0)，仍须用现场真实ImageStart矩形和导出坐标核实；不能给旧pilot套用新偏移。\n\n## 验收边界\n\n软件静态检查覆盖完整Design Table、绑定、实际展开的媒体/文章顺序、校准设置、按键/注视触发设置、图片字节一致性及完整备份可读性。原生工程保留空白Participant模板；没有复制pilot或其他参与者录制。\n\n23.8英寸Dell实际型号/有效尺寸、560mm距离、Fusion120安装映射、Windows被试屏实际信号/刷新率、真实注视门控与校准质量需实验室现场核验。静态通过不等于已经进行了带设备的完整录制；遵照SPEC中的现场检查清单。\n\nNATIVE_BACKUPS为84份正式交付原生备份；QA为逐工程严格报告和已批准偏差下的验收报告；SHA256SUMS.txt覆盖包内文件（除自身），MANIFEST.json和PROJECT_INDEX.csv提供索引。\n\nSPEC 内另附原 Mac 素材ZIP，内容及SHA256保持不变，包含原Design Table、冻结蓝图、图片、全部AOI参考及映射。材料中的八位规范原文保留，实际软件舍入差异以本包接受记录补充。\n'
(dest/'README.md').write_text(readme,encoding='utf-8')
files=sorted(p for p in dest.rglob('*') if p.is_file())
(dest/'SHA256SUMS.txt').write_text(''.join(sha(p)+'  '+p.relative_to(dest).as_posix()+'\n' for p in files),encoding='utf-8')
out=Path('__MASKED_LOCAL_PATH_0297__')
assert not out.exists(),'Refusing to overwrite desktop ZIP'
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
    for p in sorted(dest.rglob('*')):
        if p.is_file():z.write(p,arcname=dest.name+'/'+p.relative_to(dest).as_posix(),compress_type=zipfile.ZIP_STORED if p.suffix=='.zip' else zipfile.ZIP_DEFLATED)
with zipfile.ZipFile(out) as z:assert z.testzip() is None
result=dict(path=str(out),bytes=out.stat().st_size,sha256=sha(out),zip_crc='PASS',native_project_count=84,acceptance=approval)
(ROOT/'DELIVERY_VERIFICATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
