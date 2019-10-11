#!//miniconda3/envs/py36/bin/
# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@contact: yaoleistable@gmail.com
@software: Lei
@file: P7_PythonBasic_07_基本输入输出和模块对象导入.py
@time: 2019/10/4 6:29 下午
"""
import math  # 导入模块
from math import cos  # 导入模块中的某一个函数
from math import tan as t  # 导入模块中的函数，并起别名
# 1.4.7学习基本输入输出和模块对象的导入
a = 3
b = 7
print("a,b的值分别为：{0},{1}".format(a, b))
del b
print("a的值为：{0}".format(a))
x = input("请输入您的姓名:")  # 输入，input的返回值都是字符串
print(x)  # 输出
path = r"/Users/yaolei/PycharmProjects/PythonBase/Python Program Design By Dong Fu Guo/测试文本.txt"
fp = open(path, 'a+')
print("内容写入的文本中", file=fp)
fp.close()
for i in range(5, 10):
    print(i, end=' ')

print(math.sin(30))  # 导入math模块
print(cos(45))  # 导入math中的cos函数
print(t(45))  # 导入math模块中的tan函数，并起别名
