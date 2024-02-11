import os, sys

sys.path.insert(0, "/")

from myrepl.myrepl import REPL

myrepl = REPL()
myrepl.load_settings()

print("Hello REPL World!")
print(f"os.getcwd() is {os.getcwd()}")
print(f"sys.path is {sys.path}.")
