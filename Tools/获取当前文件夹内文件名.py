# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@file: 获取当前文件夹内文件名.py
@time: 2019/10/11 18:20
"""
import os


def get_file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root)
        # print(dirs)
        # print('文件：', files)
        for file in files:
            print("文件名", file)
        # 方法一：
        # with open("文件名1.txt", "w") as f:
        # f.writelines(str(files))
        # 方法二：
        # with open("文件名2.txt", "w") as f:
        # for file in files:
        # f.writelines(file + '\n')
        # f.write(file+'\n')
        # 方法三：
        s = '\n'
        with open("当前文件夹内文件名.txt", "w") as f:
            f.writelines(s.join(files))
            # f.write(s.join(files))
    print("读取当前文件夹内文件名成功！")


if __name__ == "__main__":
    file_dir = os.getcwd()
    # file_dir = r'/Users/yaolei/PycharmProjects/PythonBase/Python Program Design By Dong Fu Guo'
    print('当前文件夹：', file_dir)
    get_file_name(file_dir)
