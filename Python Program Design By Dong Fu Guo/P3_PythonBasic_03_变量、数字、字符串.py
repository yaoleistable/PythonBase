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
"""
Python不需要事先声明变量及其类型，直接赋值即可,编译器可自动识别类型
"""
x = 3
print(type(x))  # 查看变量的类型
x = 3.0
print(type(x))
x = "hello word"
print(type(x))
a = isinstance(3, int)  # 测试对象是否是某个对象的实例
print(a)
a = isinstance("hello", int)
print(a)
# 字符串和元祖属于不可变序列
b = (1, 2, 3)
# b[0] = 3  # 试图修改元祖元素的值    TypeError: 'tuple' object does not support item assignment
'''Python中允许多个变量指向同一个值'''
x = 3
print("x的内存地址:", id(x))  # 输出对象的内存地址
y = x
print("y的内存地址:", id(y))
x += 6  # 修改x的值
print("x的值:", x)
print("x的内存地址:", id(x))  # 修改后新的x内存地址改变
print("y的值:", y)  # y为x的引用，修改x，y值不变
print("y的内存地址:", id(y))  # y的内存地址不变

'''
Python采用基于值的内存管理方式，如果为不同变量赋相同值，
这个值在内存中只有一份，多个变量指向同一块内存地址
'''
x = 15
print("x的内存地址:", id(x))
y = 15
print("y的内存地址:", id(y))
'''Python具有内存自动管理功能，垃圾自动进行清理'''
print(dir())
'''
1.4.3 数字
    十进制：0、-1、9
    十六进制：0x10、0xfa，以0x开头
    八进制： 0o35 ，以0o开头  
    二进制：  ob101 ，以ob开头  
    Python内置支持复数
    字符串界定符前面加字母r表示原始字符串，用于正则表达式、文件路径、URL等
'''
a = 3 + 5j  # Python内置复数类型
b = 4 + 6j
c = a + b
print(c)
''' 
1.4.4 字符串
'''
str1 = "我爱你"
str2 = "中国"
print(str1 + str2)  # 字符串合并
# 字符串格式化
str3 = "我的名字是%s,我今年%d岁了" % ('YaoLei', 30)
print(str3)
