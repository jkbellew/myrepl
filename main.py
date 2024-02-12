from myrepl.myrepl import REPL


if __name__ == '__main__':
    repl = REPL()
    repl.cls('I cleared the screen!')
    repl.run(pyfile="tests/hello.py")
