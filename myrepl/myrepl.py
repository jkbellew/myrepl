"""My Personal REPL set up"""

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

initial_stmt: str = "[italic green]Welcome to the Python REPL[/italic green]"

pretty.install()
traceback.install(show_locals=False)

class REPL:
    def __init__(self, file: Path=history_file, stmt: str=None):
        self.history_file = file
        self.statement = stmt


    def save_history(self, file=history_file):
        if file:
            readline.write_history_file(file)
        else:
            readline.write_history_file(self.history_file)


    def cls(self, stmt: str=None) -> None:
        system("cls")
        if stmt:
            println(stmt)
        else:
            println(self.statement)


    def run(self, pyfile: str | Path) -> None:
        if type(pyfile) is str:
            pyfile = Path(pyfile)
            if not pyfile.is_file():
                println("\n[bold red]ERROR IN PROGRAM.[/bold red]\n")
            else:
                exec(compile(pyfile.open().read(), "<string>","exec"))
                println("\n[bold green]END OF PROGRAM.[/bold green]\n")


    def load_settings(self) -> None:
        self.cls(initial_stmt)

        if self.history_file.exists():
            readline.read_history_file(self.history_file)
        elif history_file.exists():
            readline.read_history_file(history_file)
        else:
            history_file.touch()


    atexit.register(save_history)  # need atexit module
