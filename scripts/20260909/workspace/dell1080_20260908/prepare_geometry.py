'Prepare independent ZH copies while table-precision decision remains pending.\n\nThis does not import tables or mark any project accepted.\n'
import argparse, traceback
import build

ap=argparse.ArgumentParser()
ap.add_argument('--start',type=int,default=2)
ap.add_argument('--end',type=int,default=42)
a=ap.parse_args()
j=None
try:
    u=build.main_ui()
    for j in build.queue()['jobs']:
        if j['language']!='ZH' or not a.start<=j['sequence']<=a.end:continue
        if j.get('stage')=='geometry_prepared' or j['status']=='static_verified':continue
        build.log(j,'Prepare geometry; table acceptance remains pending')
        u=build.rename_job(u,j) if j.get('stage') is None else build.open_job(u,j)
        u=build.resolution(u,j)
        if not j.get('fixed_pages_verified'):u=build.fixed_pages(u,j)
        u=build.browse(u,build.TEST)
        u=build.open_job(u,j)
        d,_,snapshot=build.read_design(j['guest_path'])
        assert '1920,1080' in d['Settings'].values()
        #  All table contents remain exactly those from this old design copy.
        original=build.read_backup_design(build.source_for_job(j))
        assert d['Tables']==original['Tables']
        build.inherited_check(j,d)
        build.stage(j,'geometry_prepared',geometry_snapshot=str(snapshot))
        build.log(j,'Short name and geometry saved/reopened; table migration pending',status='preparing')
except Exception as exc:
    if j:build.log(j,'Preparation stopped for review',status='failed',error=str(exc),trace=traceback.format_exc())
    raise
