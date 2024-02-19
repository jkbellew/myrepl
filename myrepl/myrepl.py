"""My Personal REPL set up"""
import readline

from pathlib import Path
from rich import print as println
from os import system


def save_history(history_file):
    readline.write_history_file(history_file)


def cls(stmt: str=None) -> None:
    system("cls")
    if stmt is not None:
        println(stmt)


def clear() -> None:
    system("cls")


def run(pyfile: str | Path) -> None:
    if type(pyfile) is str:
        pyfile = Path(pyfile)

    if pyfile.is_file():
        exec(compile(pyfile.open().read(), "<string>","exec"))
        println("\n[bold green]END OF PROGRAM.[/bold green]\n")
    else:
        println("\n[bold red]ERROR IN PROGRAM.[/bold red]\n")


def load_settings(stmt, history_file: Path) -> None:
    cls(stmt)
    if history_file.exists():
        readline.read_history_file(history_file)
    else:
        history_file.touch()
