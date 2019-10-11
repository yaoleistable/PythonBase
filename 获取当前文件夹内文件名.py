# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@file: 获取当前文件夹内文件名.py
@time: 2019/10/11 18:20
"""
import os


def get_file_name():
    file_dir = os.getcwd()
    print(file_dir)
    for root, dirs, files in os.walk(file_dir):
        print(root)
        print(dirs)
        print(files)
        with open("文件名.txt", "w") as f:
            f.write(files)


if __name__ == "__main__":
    get_file_name()
