import os
import os.path
import sys
from . import interpre
import Interpreter_RL


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


def echo(inter_obj,args):
    # print(args)
    n_args = "".join(args)
    # print(n_args)
    inter_obj.stdout.append(n_args)
    return 0


def load_funcs(inter_obj,arg):
    home_path = sys.argv[0]


def exit(inter_obj,arg):
    if arg[0]=="yes":
        return inter_obj.close(debug=True)
    return inter_obj.close()

global func_com_mapping
# 可在此处手动配置
func_com_mapping = {

}

# 配置内置函数映射
Inner_fun_tmp = {
    "echo": echo,
    "load":load_funcs,
    "exit":exit
}

global INNER_FUNCTIONS
INNER_FUNCTIONS = FuncList()


def main():
    for k in func_com_mapping:
        INNER_FUNCTIONS.append(RlFuncObj(k, func_com_mapping[k]))
    for k in Inner_fun_tmp:
        INNER_FUNCTIONS.append(RlFuncObj(k, Inner_fun_tmp[k]))


main()
