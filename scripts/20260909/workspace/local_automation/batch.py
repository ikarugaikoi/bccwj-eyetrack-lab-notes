"""DELL publication extract: retained function implementations are unchanged."""
from controller import command
from ui import UI


def exact_dialog(title):
    ws=[w for w in command('windows') if w['title']==title]
    if len(ws)!=1:raise RuntimeError('Expected exactly one dialog: '+title)
    return UI(ws[0]['hwnd'])
