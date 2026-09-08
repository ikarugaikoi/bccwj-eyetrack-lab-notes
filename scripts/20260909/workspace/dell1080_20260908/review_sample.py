'Collect strict diagnostics without accepting or hiding precision deviations.'
import json, zipfile
import openpyxl
import build

j=build.queue()['jobs'][0]
u=build.main_ui()
u=build.open_job(u,j)
try:
    u=build.update_table(u,j)
except AssertionError:
    #  Preserve the strict failure; inspect every differing cell below.
    u=build.main_ui()
u=build.browse(u,build.TEST)
u=build.open_job(u,j)
d,n,archive=build.read_design(j['guest_path'])
dest=build.ROOT/'snapshots'/j['actual']
dest.mkdir(exist_ok=True)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for name in z.namelist():
        assert (dest/name).resolve().is_relative_to(dest.resolve())
    z.extractall(dest)
    roots={name.split('/')[0] for name in z.namelist()}
    assert len(roots)==1
result=build.checker.inspect(dest/next(iter(roots)),j['planned'],build.SPEC)
build.write(build.ROOT/'qa'/(j['actual']+'_native.json'),result)
book=build.PACKAGE/build.bp(j)['workbook_path']
wb=openpyxl.load_workbook(book,read_only=True,data_only=True)
rows=list(wb['Tobii_Design'].values);wb.close()
tid,t=next(iter(d['Tables'].items()))
assert [n[c] for c in t['Columns']]==list(rows[0])
assert len(t['Cells'])==(len(rows)-1)*len(rows[0])
diffs=[]
for index,(actual,expected) in enumerate(zip(t['Cells'],[v for row in rows[1:] for v in row])):
    if (None if actual is None else str(actual))!=(None if expected is None else str(expected)):
        diffs.append(dict(excel_row=index//len(rows[0])+2,column=rows[0][index%len(rows[0])],observed=actual,expected=expected))
out=dict(status='REVIEW_REQUIRED',native_snapshot=str(archive),workbook=str(book),workbook_sha256=build.sha(book),table_differences=diffs,native_checks=result['check_count'],native_failures=result['failures'])
try:
    build.inherited_check(j,d)
    out['inheritance']='PASS: no other changes after specified geometry and independently reported table changes'
except RuntimeError as exc:
    out['inheritance']=str(exc)
build.write(build.ROOT/'qa'/(j['actual']+'_precision_review.json'),out)
build.stage(j,'sample_review_pending')
build.log(j,'Sample reopened; strict diagnostics collected; precision decision pending',status='needs_review',checks=result['check_count'],failures=result['failure_count'],table_differences=len(diffs),inheritance=out['inheritance'])
print(json.dumps({k:v for k,v in out.items() if k not in ('table_differences','native_failures')},ensure_ascii=False),flush=True)
