# My REPL Setup

This is my setup whenever I go to the REPL. There are three functions:
- _cls()_ : This clears the screen. 
- _save_history(file=history_file)_ : Takes an argument for the name of the history file.
- _run(pyfile: str | Path)_ : This takes a string or _Path_ object representing a python script and then sends it to be compiled and executed. It will return either __END OF PROGRAM__ for successful execution of python script or __ERROR IN PROGRAM__ for unsuccessful. 
