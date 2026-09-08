"""DELL publication extract: retained function implementations are unchanged."""
from ui import UI
from controller import command


def submit_dialog(d, main_hwnd, button='DialogOkButton'):
    old=d.hwnd
    try:
        d.act('invoke',{'automation_id':button,'type':'Button'})
    except RuntimeError as exc:
        if 'Target is not a visible Tobii window' not in str(exc):raise
    if any(w['hwnd']==old for w in command('windows')):
        raise RuntimeError('Expected dialog to close after submission')
    return UI(main_hwnd)
