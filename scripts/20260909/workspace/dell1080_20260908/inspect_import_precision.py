'Read-only inspection of the installed 25.7 import formatter; no binary writes.'
import hashlib,json,sys
from pathlib import Path
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'diagnostic_deps'))
import dnfile
from dncil.cil.body.reader import read_method_body_from_bytes
path=Path('__MASKED_LOCAL_PATH_0300__')
p=dnfile.dnPE(str(path))
methods=[]
for t in p.net.mdtables.TypeDef:
    for m in t.MethodList:
        if (str(t.TypeName),str(m.row.Name)) not in [('ExcelSheetFormatter','FormatCell'),('Number','Format')]:continue
        instructions=[]
        for i in read_method_body_from_bytes(p.get_data(m.row.Rva,4096)).instructions:
            op=i.operand;resolved=None
            if hasattr(op,'value'):
                v=op.value;table=v>>24;idx=v&0xffffff
                if table==0x70:resolved=str(p.net.user_strings.get(idx))
                elif table in p.net.mdtables.tables:
                    r=p.net.mdtables.tables[table].rows[idx-1]
                    resolved=' '.join(str(getattr(r,k,'')) for k in ['Name','TypeName']).strip()
                    if hasattr(r,'Class'):resolved+=' '+str(getattr(r.Class.row,'TypeName',''))
            instructions.append(dict(instruction=str(i),resolved=resolved))
        methods.append(dict(type=str(t.TypeNamespace)+'.'+str(t.TypeName),method=str(m.row.Name),instructions=instructions))
out=dict(scope='Read-only HOST installation, file version 25.7.1400.0; guest UI reports same version but binary hash not compared',binary=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),finding='ExcelSheetFormatter.FormatCell parses numeric text and calls Number.Format. Number.Format calls Math.Round with 4 decimal places before converting to string.',methods=methods)
(root/'qa/import_formatter_evidence.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='methods'},ensure_ascii=False))
