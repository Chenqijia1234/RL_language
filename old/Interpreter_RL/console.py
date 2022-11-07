import sys


class Console:
    def __init__(self):
        pass

    def writeLine(self,*args,file=sys.stdout,split="",endl="\n"):

        for i in args:
            file.write(i)
            file.write(split)
        file.write(endl)
        return
    def readLine(self,tip:str="",file=sys.stdin):
        print(tip,end="",file=sys.stdout)
        rs = file.readline()[-1]
        return rs


if __name__=="__main__":
    console = Console()
    console.writeLine("chenqijia","hello")
    print(console.readLine("hi"))