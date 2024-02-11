import os
import sys
sys.path.insert(0, "C:/Users/jason/PycharmProjects/myrepl")

import myrepl.myrepl as settings

settings.load_settings()


print("Hello REPL World!")
print(f"os.getcwd() is {os.getcwd()}")
print(f"sys.path is {sys.path}.")
