# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@file: 获取当前文件夹内文件名.py
@time: 2019/10/11 18:20
"""
import os


def get_file_name(file_dir):
    i = 1
    j = 1
    for root, dirs, files in os.walk(file_dir):
        # print(root)
        # print(dirs)
        # print('文件：', files)
        for file in files:
            print(str(i) + ' ' + file)
            i = i + 1
            # 方法一：
            # with open("文件名1.txt", "a") as f:
            # f.writelines(str(files))
        # 方法二：
        # with open("当前文件夹内文件名.txt", "a") as f:
        # for file in files:
        # file_name = str(j)+' '+file+'\n'
        # f.writelines(file_name)
        # 方法三：
            s = '\n'
            with open("当前文件夹内文件名.txt", "a") as f:  # 注意需用a模式，用w模式，每次写会清空上一次写的内容
                f.writelines(s.join(file))
    print("读取当前文件夹内文件名成功！")


if __name__ == "__main__":
    file_dir = os.getcwd()
    # file_dir = r'/Users/yaolei/PycharmProjects/PythonBase/Python Program Design By Dong Fu Guo'
    print('当前文件夹：', file_dir)
    get_file_name(file_dir)
