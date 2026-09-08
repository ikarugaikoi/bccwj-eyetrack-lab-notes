"""DELL publication extract: retained function implementations are unchanged."""
import json
import time
import zipfile
from controller import command, ROOT, BRIDGE


def write(path, obj):
    content=json.dumps(obj,ensure_ascii=False,indent=2)
    if path==BRIDGE/'scope.json':
        #  HGFS caches an open handle that can deny host-side atomic replacement.
        #  Scope is changed only between completed guest commands.
        path.write_text(content,encoding='utf-8')
        return
    temp=path.with_suffix('.tmp')
    temp.write_text(content,encoding='utf-8')
    for attempt in range(20):
        try:temp.replace(path);return
        except PermissionError:
            if attempt==19:raise
            time.sleep(.1)


def normalize(s):
    return s.replace('_','').casefold()


def read_design(path):
    r=command('read_test_project',path=path)
    archive=BRIDGE/'responses'/r['readonly_snapshot']
    with zipfile.ZipFile(archive) as z:
        designs=[n for n in z.namelist() if '/Current/Design/' in n and n.endswith('.json')]
        if len(designs)!=1:raise RuntimeError('Expected one native design')
        d=json.loads(z.read(designs[0]))['Data']
        names={}
        for n in z.namelist():
            if '/Names/' in n:
                for x in json.loads(z.read(n))['Data']:
                    names[x['Key']['data']]=x['Value']
    return d,names,str(archive)
