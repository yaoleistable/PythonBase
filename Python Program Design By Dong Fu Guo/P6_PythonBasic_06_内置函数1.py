#!//miniconda3/envs/py36/bin/
# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@contact: yaoleistable@gmail.com
@software: Lei
@file: P6_PythonBasic_06_内置函数1.py
@time: 2019/10/4 5:57 下午
"""
import math

print("dir()函数的使用：", dir(math))  # dir函数返回模块中包含的成员
print("help()函数的使用：")
help(math.cos)
help(math.tan)
help(ord)
print("enumerate枚举函数{0}".format(list(enumerate("abode"))))
print("for循环使用枚举函数:")
for index, value in enumerate(range(10, 15)):
    print((index, value), end='')
