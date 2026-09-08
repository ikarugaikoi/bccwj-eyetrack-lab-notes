# !__MASKED_LOCAL_PATH_0917__
'Reproducible geometric conversions; no workbook, stimulus or device writes.'
import json
import math
from pathlib import Path


def distance_calculations():
    sx,sy=527/1920,296/1080
    distances=[]
    for d in [550,560,650]:
        angle=lambda mm:math.degrees(2*math.atan(mm/(2*d)))
        pixels=lambda degrees,scale:2*d*math.tan(math.radians(degrees/2))/scale
        row={'eye_to_screen_plane_mm':d,
             'role':'current_target' if d==560 else ('nearby_comparison' if d==550 else 'withdrawn_target_comparison_only'),
             'character_x_deg':angle(32*sx),'character_y_deg':angle(32*sy),
             'dot_x_deg':angle(16*sx),'dot_y_deg':angle(16*sy),
             'gate_w_deg':angle(96*sx),'gate_h_deg':angle(84*sy),
             'one_pixel_x_deg':angle(sx),'one_pixel_y_deg':angle(sy),
             'row_pitch_165px_deg':angle(165*sy),
             'screen_w_deg_centered_eye':angle(527),'screen_h_deg_centered_eye':angle(296),
             'one_degree_pixels_x':pixels(1,sx),'one_degree_pixels_y':pixels(1,sy),
             'half_degree_pixels_x':pixels(.5,sx),'half_degree_pixels_y':pixels(.5,sy)}
        assert math.isclose(angle(row['one_degree_pixels_x']*sx),1,abs_tol=1e-12)
        assert math.isclose(angle(row['half_degree_pixels_x']*sx),.5,abs_tol=1e-12)
        distances.append(row)
    return {
        'distance_target_mm':560,
        'distance_status':'560 mm target after user correction to preserve previous approximately 55 cm EIZO setup; actual distance and tracking coverage require onsite verification. 650 mm default withdrawn.',
        'distance_basis':{
            'old_eizo_target_mm':550,'old_eizo_pixel_pitch_mm':.270,
            'new_assumed_horizontal_pixel_pitch_mm':sx,
            'equal_pixel_visual_angle_new_distance_mm':550*sx/.270,
            'rounded_operating_target_mm':560,
            'historical_design_document':'experiment_design/2026-06-28_L2_eye_tracking_space0_design.md, Viewing Distance',
            'not_proof_of_old_measured_distance':True,
        },
        'angular_formula':'theta_deg = 2*atan(size_mm/(2*distance_mm))*180/pi; size_px = 2*distance_mm*tan(theta_deg*pi/360)/mm_per_px',
        'angular_assumptions':'Standard centered-target / near-axis conversion using rounded 527x296 mm and perpendicular screen distance. Exact eccentric-target angles need eye position relative to the target. Not measured calibration error or hardware gaze-angle coverage.',
        'distance_sensitivity':distances,
    }


def main():
    here=Path(__file__).resolve().parent
    update=distance_calculations()
    for name in ['PROPOSED_GEOMETRY.json','SOURCE_AUDIT.json']:
        p=here/name; data=json.loads(p.read_text(encoding='utf-8'))
        geometry=data['geometry'] if name=='SOURCE_AUDIT.json' else data
        old_pixel={k:v for k,v in geometry.items() if not k.startswith(('distance_','angular_'))}
        geometry.update(update)
        assert old_pixel=={k:v for k,v in geometry.items() if not k.startswith(('distance_','angular_'))}
        p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(update,ensure_ascii=False,indent=2))


if __name__=='__main__': main()
