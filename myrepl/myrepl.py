"""My Personal REPL set up"""

import sys
import readline
import atexit

# from importlib import reload
from pathlib import Path
# from pprint import pp
from rich import pretty, traceback
from rich import print as println
from os import system

history_file = Path.home() / ".pyhistory"

sys.ps1 = "\033[32mpy> "
sys.ps2 = "py| "

initial_stmt: str = "[italic green]Welcome to the Python REPL[/italic green]"

pretty.install()
traceback.install(show_locals=False)

class REPL:
    def __init__(self):


def save_history(file=history_file):
    readline.write_history_file(file)


def cls(stmt: str=None) -> None:
    system("cls")
    println(stmt)


def run(pyfile: str | Path) -> None:
    if type(pyfile) is str:
        pyfile = Path(pyfile)
        if not pyfile.is_file():
            println("\n[bold red]ERROR IN PROGRAM.[/bold red]\n")
        else:
            exec(compile(pyfile.open().read(), "<string>","exec"))
            println("\n[bold green]END OF PROGRAM.[/bold green]\n")


def load_settings() -> None:
    cls(initial_stmt)

    if history_file.exists():
        readline.read_history_file(history_file)
    else:
        history_file.touch()

    atexit.register(save_history)  # need atexit module
