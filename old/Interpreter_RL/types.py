import os
import os.path
import sys
from . import interpre
from . import types


# 构建解释器函数存储对象
class RlFuncObj:
    def __init__(self, func_name: str, func_pyobj):
        self.func_name = func_name
        self.func_pyobj = func_pyobj


class FuncList(list):
    def __init__(self):
        super().__init__()

    def find_func(self, name):
        for i in self:
            if i.func_name == name:
                return (True, i.func_pyobj)
        return (False, None)


def platform_my(inter_obj,args):
    import sys
    return sys.platform

def echo(inter_obj,args):
    # print(args)
    n_args = "".join(args)
    # print(n_args)
    inter_obj.stdout.append(n_args)
    return 0
def cls_my(inter_obj,args):
    inter_obj.stdout.append("\033c")

def help(inter_obj,args):
    inter_obj.stdout.append("已编译的函数：")
    for i in types.INNER_FUNCTIONS:
        inter_obj.stdout.append(i.func_name)
    return 0

def load_funcs(inter_obj,arg):
    inter_obj.stdout.append("我们仍在开发这个函数。")
    home_path = sys.argv[0]


def exit(inter_obj,arg):
    # print(arg)
    if len(arg)>0:
        if arg[0]=="yes":
            return inter_obj.close(debug=True)
    return inter_obj.close()


global CONFIG;
CONFIG={
    "ver":"0.1.2",
    "edition":"Previews DEV",
    "log":"""
    9.16：发布解释器v0.1PreviewDEV；
    9.17：添加了ASCII图标和CONFIG字典；
          """
}
global func_com_mapping
# 可在此处手动配置
func_com_mapping = {

}

# 配置内置函数映射
Inner_fun_tmp = {
    "echo":echo,
    "load":load_funcs,
    "exit":exit,
    "help":help,
    "platform":platform_my,
    "cls":cls_my
}

global INNER_FUNCTIONS
INNER_FUNCTIONS = FuncList()


def main():
    for k in func_com_mapping:
        INNER_FUNCTIONS.append(RlFuncObj(k, func_com_mapping[k]))
    for k in Inner_fun_tmp:
        INNER_FUNCTIONS.append(RlFuncObj(k, Inner_fun_tmp[k]))


main()
