# if __name__ != "__main__":
#     from . import runtime, interpreter, Rtypes
# else:
# import runtime
import os
import interpreter
import Rtypes


def MainLoop(mode,FileName:None|str):
    # main_namespace = Rtypes.NameSpace()
    # safeIO = Rtypes.SafeIOSandbox()
    # interpreter = interpreter.Interpreter(mode,main_namespace,safeIO)
    if mode== Rtypes.ConsoleMode.FROM_FILE:
        try:
            with open(FileName,"r") as file:
                a:list[str] = file.readlines()
                for i in range(len(a)):
                    a[i] = a[i].strip()
                print(a)
        except OSError as e:
            print("Check your input!")
    elif mode==Rtypes.ConsoleMode.LINE_AND_LINE:
        while True:    
            print(interpreter.run(input(">>>")))


MainLoop(Rtypes.ConsoleMode.FROM_FILE,r"./first.rls")
