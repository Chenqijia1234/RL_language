# if __name__ != "__main__":
#     from . import runtime, interpreter, types
# else:
# import runtime


import interpreter
import types


def MainLoop(mode,FileName:None|str):
    # main_namespace = types.NameSpace()
    # safeIO = types.SafeIOSandbox()
    # interpreter = interpreter.Interpreter(mode,main_namespace,safeIO)
    if mode== types.ConsoleMode.FROM_FILE:
        try:
            with open(FileName,"r") as file:
                print(file.read())
        except OSError as e:
            print("Check your input!")
    elif mode==types.ConsoleMode.LINE_AND_LINE:
        while True:    
            print(interpreter.run(input(">>>")))


MainLoop(types.ConsoleMode.FROM_FILE,"first.rls")