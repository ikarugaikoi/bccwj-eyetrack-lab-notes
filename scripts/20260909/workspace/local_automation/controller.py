"""DELL publication extract: retained function implementations are unchanged."""
import argparse
import json
import os
import time
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BRIDGE = ROOT / "bridge"


def command(op, timeout=45, **kwargs):
    if (ROOT/'PAUSE').exists() and op not in ('ping','windows','observe','read_test_project','list_build_projects'):
        raise RuntimeError('Local execution paused before the next action')
    cid = uuid.uuid4().hex
    payload = dict(kwargs, op=op, id=cid, expires_at=time.time()+timeout)
    path = BRIDGE / 'requests' / (cid+'.json')
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(payload, ensure_ascii=False), encoding='utf-8')
    os.replace(tmp, path)
    result = BRIDGE / 'responses' / path.name
    deadline = time.monotonic()+timeout
    while time.monotonic() < deadline:
        if result.exists():
            try:
                data = json.loads(result.read_text(encoding='utf-8'))
            except (PermissionError, json.JSONDecodeError):
                #  VMware HGFS may briefly keep an atomically renamed file locked.
                time.sleep(.1)
                continue
            if not data['ok']:
                raise RuntimeError(data['error'])
            return data['result']
        time.sleep(.1)
    raise TimeoutError('Guest did not respond: '+cid)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('op')
    ap.add_argument('--args', default='{}')
    ap.add_argument('--out')
    a = ap.parse_args()
    result = command(a.op, **json.loads(a.args))
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if a.out:
        Path(a.out).write_text(text, encoding='utf-8')
    else:
        print(text)


if __name__ == "__main__":
    main()
