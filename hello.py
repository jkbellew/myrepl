import os, sys

sys.path.insert(0, "C:/Users/jason/PycharmProjects/myrepl")

from myrepl.myrepl import REPL

REPL.load_settings()

print("Hello REPL World!")
print(f"os.getcwd() is {os.getcwd()}")
print(f"sys.path is {sys.path}.")
