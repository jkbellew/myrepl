"""My Personal REPL set up"""
import code
import sys
import readline
import atexit

from pathlib import Path
from rich import pretty, traceback
from rich import print as println
from os import system

history_file = Path.home() / ".pyhistory"

sys.ps1 = "\033[32mpy> "
sys.ps2 = "py| "

banner: str = "[italic green]Welcome to the Python REPL[/italic green]"

pretty.install()
traceback.install(show_locals=False)

class REPL(code.InteractiveConsole):
    def __init__(self, globals, *args, **kwargs):
        code.InteractiveConsole.__init__(self, *args, **kwargs)
        self.globals = globals

    def run(self, code):
        try:
            exec(compile(code), self.globals, self.locals)
        except SystemExit:
            raise
        except:
            self.showtraceback()
