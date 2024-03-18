"""My Personal REPL set up"""
from pathlib import Path
from rich import print as println

import os
import readline


def save_history(history_file):
    readline.write_history_file(history_file)


def cls(stmt: str = None) -> None:
    os.system("cls")
    if stmt is not None:
        println(stmt)


def clear() -> None:
    os.system("cls")


def ch(p: Path) -> None:
    if p.exists():
        os.chdir(p)
    else:
        println("[bold red]That path does not exist.[/bold red]")


def run(pyfile: str | Path) -> None:
    if type(pyfile) is str:
        pyfile = Path(pyfile)

    if pyfile.is_file():
        exec(compile(pyfile.open().read(), "<string>", "exec"))
        println("\n[bold green]END OF PROGRAM.[/bold green]\n")
    else:
        println("\n[bold red]ERROR IN PROGRAM.[/bold red]\n")


def load_settings(stmt, history_file: Path) -> None:
    cls(stmt)
    if history_file.exists():
        readline.read_history_file(history_file)
    else:
        history_file.touch()
