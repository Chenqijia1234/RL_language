# cython:language_level=3
import sys
import traceback
if __name__ != "__main__":
    from . import types
    from . import errors
else:
    from Interpreter_RL import types
    from Interpreter_RL import errors


class Interpreter:
    Process = []

    def __init__(self, mode: str = "shell"):
        self.__key = None
        self.ver = types.CONFIG["ver"]
        self.edition = types.CONFIG["edition"]
        self.stdout = []
        self.returned_val = []
        self.stdouted = []
        self.runned_command = []
        self.errored = []
        self.running_command = (None, None)
        self.Mode = mode
        self.generate_key()
        if self.Mode == "":
            raise errors.InitError("value", "interpreter init...", "无效的mode参数")
        Interpreter.Process.append(self)

    def run_shell(self, command: str):
        if command.endswith(";"):
            command = command[:-1]
        command_formatd = command.split()
        self.__run_shell_inner(command_formatd[0], command_formatd[1:])

    def __run_shell_inner(self, command: str, args: list):
        # print(command,args)
        total, func_obj = types.INNER_FUNCTIONS.find_func(command)
        self.running_command = (command, func_obj)
        self.runned_command.append(self.running_command)
        # print(self.runned_command)
        if total:
            self.retn_val = func_obj(self, args)
        else:
            raise errors.Runtime_error("undefined_var", f"call {command}", "未定义的命令")
        self.__update_stdout()

    def run_script(self, commands: str):
        if commands.endswith(";"):
            commands = commands[:-1]
        scripts = commands.split(";")
        if len(scripts) == 1:
            self.run_shell(scripts[0])
            return
        for i in range(len(scripts)):
            scripts[i] = scripts[i].split()
        for j, *k in scripts:
            self.__run_shell_inner(j, k)

    def run_loop(self):
        print("""
 ____  _       _        _    _   _  ____ _   _   _    ____ _____  
|  _ \| |     | |      / \  | \ | |/ ___| | | | / \  / ___| ____| 
| |_) | |     | |     / _ \ |  \| | |  _| | | |/ _ \| |  _|  _|   
|  _ <| |___  | |___ / ___ \| |\  | |_| | |_| / ___ \ |_| | |___  
|_| \_\_____| |_____/_/   \_\_| \_|\____|\___/_/   \_\____|_____| 
        """)
        print(f"RL锐麟Language Console {self.ver} Preview Edition  输入help ;获取帮助。")
        while True:
            try:
                while True:
                    com = input(">>")
                    self.run_script(com)
                    # print("std",self.stdouted)
                    if self.retn_val is not None:
                        print("return val:", self.retn_val)
            except Exception as e:
                # traceback.print_tb(sys.exc_info()[2])
                print(f"\033[1;31;48m{str(e)}\033[0m")
                self.errored.append(str(e))

    def generate_key(self):
        import random
        self.__key = random.randint(100000, 1000000)

    def close(self, debug=False):
        inu = input(f"真的要退出吗？如果是，请在下方重复此数字{self.__key}\n")
        if int(inu) == self.__key and debug != True:
            sys.exit(0)
        elif int(inu) == self.__key and debug:
            print("运行过的命令", self.runned_command)
            print("运行过命令的返回值", self.returned_val)
            print("命令输出过的内容", self.stdouted)
            print("错误日志", self.errored)
            sys.exit(self.__key)
        else:
            return "Field"

    def __update_stdout(self):
        # print(self.stdout)
        for i in range(len(self.stdout)):
            print(self.stdout[i])
            self.stdouted.append(self.stdout[i])
        self.stdout.clear()
