'Exact, user-approved import deviation. No generic tolerance relaxation.'
import hashlib,json
from pathlib import Path
RECORD=Path(__file__).with_name('ACCEPTED_DEVIATION.json')
PAIRS={'DOT_H':('0.07777778','0.0778'),'DOT_Y':('0.06666667','0.0667')}
def policy(path=RECORD):
    p=Path(path)
    obj=json.loads(p.read_text(encoding='utf-8'))
    assert obj['id']=='DELL1080_DOT_IMPORT_ROUNDING_20260908' and obj['approved'] is True
    assert obj['user_instruction']=='ok记录这个偏差然后使用继续搭建吧'
    assert set(obj['changes'])==set(PAIRS)
    assert all((obj['changes'][k]['expected'],obj['changes'][k]['observed'])==v for k,v in PAIRS.items())
    return {'id':obj['id'],'record':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def permitted(differences):
    policy()
    return all(d['column'] in PAIRS and (str(d['expected']),str(d.get('observed',d.get('actual'))))==PAIRS[d['column']] for d in differences)
