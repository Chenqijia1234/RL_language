# cython: language_level=3
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# write by tcy shanghai songjiang xiaokunshan in 2020/4/12

import sys, os, shutil
from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext


class MadeFilePyToPyd:
    """
    将xxx.py文件批量转为xxx.pyd
    文件路径最好用'/'替代'\\',否则有些真实存在的文件存在判断，更名会有问题
    """

    def __init__(self):
        self.filenames_suffix_c = []
        self.filenames_pyd = []

    def __del__(self):
        pass

    def _get_filename_only(self, filenames: list):
        a = [f[:f.rfind('.')] for f in filenames]

    def findPathFilename(self, path: str = '', suffix: str = '.py') -> list:
        """
        查找指定路径下的所有以.py为后缀的文件名
        path:str path or list [file1,file2,...]
        suffix:str '.py' or 'py'
        """
        if path == '':
            path = os.getcwd()

        if suffix.find('.') == -1:
            suffix = '.' + suffix

        # 必须用'./build/'+x；用os.getcwd()+'\\'+x b.cp37-win_amd64.pyd文件即使存在也不能判断
        # 但是b.py文件存在却能够判断
        # filenames=[x for x in os.listdir(path) if os.path.isfile('./build/'+x) and os.path.splitext(x)[1].lower()==suffix.lower()]
        if isinstance(path, list):
            filenames = path
        elif isinstance(path, str):
            filenames = [x for x in os.listdir(path) if
                         os.path.isfile(x) and os.path.splitext(x)[1].lower() == suffix.lower()]
        else:
            return []

        self.filenames_suffix_c = [f[:f.rfind('.')] + '.c' for f in filenames]
        self.filenames_pyd = [f[:f.rfind('.')] + '.pyd' for f in filenames]
        return filenames

    def delFileOrDir(self, file: str) -> None:
        """
        删除文件夹及其中文件或单文件
        """
        if os.path.isdir(file):
            shutil.rmtree(file)
        elif os.path.isfile(file):
            os.remove(file)

    def delFileSuffixIs_C(self, dir: str = '') -> None:
        """
        删除后缀是xxx.c的文件;文件名来自dir文件夹;放在最后运行
        当dir=''删除当前目录下的xxx.c文件
        """
        for file in self.filenames_suffix_c:
            if dir:
                tmp = os.path.join(os.getcwd(), file)
            else:
                tmp = file
            if os.path.isfile(tmp):
                os.remove(file)

    def rename_cp37_win_amd64_pyd(self, path: str = './build') -> list:
        """
        更改指定文件夹下所有文件名：
        :param path: [str]
        :return: a.cp37-win_amd64.pyd名字更改为a.pyd
        """
        files = [x for x in os.listdir(path)]

        for file, newfile in zip(files, self.filenames_pyd):
            file = path + '/' + file  # './build/'+file必须这样用；'G:\\OpenCV\\C\\build\\'+file错误
            newfile = path + '/' + newfile
            os.rename(file, newfile)

    def pack_pyd(self, path: str = '', suffix: str = '.py', build_dir="./build", delFilesuffixls_C_mode=True):
        """
        :param path: str or list ['a.py','b.py']
        :param suffix:'.py' or 'py'
        :param build_dir:
        :param delFilesuffixls_C_mode:
        :return:
        """
        build_tmp_dir = 'tmp'
        module_list = self.findPathFilename(path, suffix)  # 获取py列表 or [ 'a.py', 'b.py']
        self.delFileOrDir(build_dir)

        try:
            setup(
                ext_modules=cythonize(module_list),
                script_args=["build_ext", "-b", build_dir, "-t", build_tmp_dir],
            )
            self.delFileOrDir(build_tmp_dir)
            self.rename_cp37_win_amd64_pyd(build_dir)
            if delFilesuffixls_C_mode:
                self.delFileSuffixIs_C()
        except Exception as ex:
            print("error! ", str(ex))


if __name__ == '__main__':
    a = MadeFilePyToPyd()
    cur_path = os.getcwd()  # G:\OpenCV\C
    # print(a.findPathFilename())
    print(a.findPathFilename())

    print(a.filenames_suffix_c)
    print(a.filenames_pyd)
    a.pack_pyd()
