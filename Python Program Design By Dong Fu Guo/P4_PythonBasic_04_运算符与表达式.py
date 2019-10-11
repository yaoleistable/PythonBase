#!//miniconda3/envs/py36/bin/
# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@contact: yaoleistable@gmail.com
@software: Lei
@file: P5_PythonBasic_05_内置函数1.py
@time: 2019/10/4 11:33 上午
"""
ascii_str = "姚"
print(ord(ascii_str))  # 转换为ascii码函数
print(ord("蕾"))
chr_str = 34174
print("姚")
print(chr(chr_str))  # ascii转换为字符
print(hex(23002))
a = 15
b = 13
c = a + b * a
d = a / b
e = a // b
print('c={0},d={1:.2f},e={2}'.format(c, d, e))  # 格式化函数
