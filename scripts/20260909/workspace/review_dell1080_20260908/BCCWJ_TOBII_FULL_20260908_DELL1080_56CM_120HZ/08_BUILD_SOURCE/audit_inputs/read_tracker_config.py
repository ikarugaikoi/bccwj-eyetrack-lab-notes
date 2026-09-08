# !__MASKED_LOCAL_PATH_0917__
'Optional read-only Tobii Research SDK getters; never installs or configures.\n\nUse only if the official Python SDK is already installed and compatible.\n    py -3 read_tracker_config.py --output __MASKED_LOCAL_PATH_0922__\nNo calibration, subscriptions, frequency changes, display-area writes or firmware\noperations are performed. Lists all discovered devices instead of choosing one.\nDevice serials may be present: keep output in the private research archive.\n'
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys


def collect(sdk):
    report={
        'timestamp_utc':datetime.now(timezone.utc).isoformat(),
        'purpose':'Observed SDK values only; not confirmation of physical installation or calibration quality',
        'device_writes_performed':False,
        'devices':[],
        'errors':[],
    }
    try:
        devices=sdk.find_all_eyetrackers()
    except Exception as exc:
        report['errors'].append({'operation':'find_all_eyetrackers','error':str(exc)})
        devices=[]
    for tracker in devices:
        item={'identity':{},'errors':[]}
        for field in ('address','model','device_name','serial_number'):
            try:
                item['identity'][field]=getattr(tracker,field)
            except Exception as exc:
                item['identity'][field]=None
                item['errors'].append({'operation':field,'error':str(exc)})
        for field,method in (
            ('current_gaze_frequency_hz','get_gaze_output_frequency'),
            ('available_gaze_frequencies_hz','get_all_gaze_output_frequencies'),
        ):
            try:
                value=getattr(tracker,method)()
                item[field]=list(value) if field.startswith('available') else value
            except Exception as exc:
                item[field]=None
                item['errors'].append({'operation':method,'error':str(exc)})
        try:
            area=tracker.get_display_area()
            item['display_area']={
                'coordinate_system':'User Coordinate System, millimetres relative to tracker',
                'width_mm':area.width,'height_mm':area.height,
                **{p+'_mm':list(getattr(area,p)) for p in ('top_left','top_right','bottom_left','bottom_right')},
            }
        except Exception as exc:
            item['display_area']=None
            item['errors'].append({'operation':'get_display_area','error':str(exc)})
        report['devices'].append(item)
    report['status']='OBSERVED_NOT_PHYSICALLY_VERIFIED' if devices and not report['errors'] and not any(d['errors'] for d in report['devices']) else 'INCOMPLETE_OR_UNAVAILABLE'
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    if args.output.exists():
        parser.error('Output already exists; choose a new filename. Nothing was overwritten.')
    try:
        import tobii_research as sdk
    except Exception as exc:
        report={
            'timestamp_utc':datetime.now(timezone.utc).isoformat(),
            'status':'SDK_UNAVAILABLE',
            'device_writes_performed':False,
            'error':str(exc),
            'action':'Do not install or upgrade for this optional check; use Manager/Pro Lab evidence instead.',
        }
    else:
        report=collect(sdk)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x',encoding='utf-8') as handle:
        json.dump(report,handle,ensure_ascii=False,indent=2)
        handle.write('\n')
    print(json.dumps({'status':report['status'],'output':str(args.output.resolve())},ensure_ascii=False))
    return 0 if report['status']=='OBSERVED_NOT_PHYSICALLY_VERIFIED' else 2


if __name__=='__main__':
    sys.exit(main())
