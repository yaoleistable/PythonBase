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
# 1.4.6 学习内置函数
a = 12
ab = "hello"
a1 = abs(a)  # 求a的绝对值
a2 = ascii(a)  # 把对象转换为ascii码的形式
a3 = bin(a)  # 把整数x转换为二进制串表示形式
a4 = bool(a)  # 返回与x等价的布尔值true or false"内置函数计算值：{0},{1},{2},{3}".format(a1, a2, a3, a4)
print("内置函数计算值1：{0},{1},{2},{3}".format(a1, a2, a3, a4))
a5 = bytes(a)  # 生成字节串
a6 = chr(a)  # 返回unicode编码的字符
# a6_1 = ord(ab)  # 返回一个字符x的Unicode编码
a7 = float(a)  # 返回浮点数
a8 = hash(a)  # 返回哈希值
print("内置函数计算值2：{0},{1},{2},{3}".format(a5, a6, a7, a8))
a9 = hex(a)  # 返回整数x的十六进制串
a10 = oct(a)  # 把整数x转换为八进制数
print("内置函数计算值3：{0},{1},{2},{3}".format(a9, a6, a7, a8))
b = {0, 5, -2, 3}
print(dir(b))  # dir（obj）返回指定对象或模块obj成员列表
b1 = len(b)  # 返回对象中元素个数
print("长度为{0}".format(b1))
print("排序后的列表：{0}".format(sorted(b, key=None, reverse=True)))  # reverse值代表升序还是降序
print("元素之和为：{0}".format(sum(b)))  # 求元素之和
print("类型为：{0}".format(type(b)))  # 返回类型
print("转换为字符串：{0}".format(str(b)))
c = input("请输入您的姓名:")
print("您的姓名是{0}".format(c))
d = 3.1415926
d1 = int(d)  # 返回整数部分
d2 = round(d, 4)  # 对x进行四舍五入
print("int(x)={0}，{1}".format(d1, d2))
print("我爱我的祖国", end=' ')  # 默认为end='\n'，会换行，可修改end值
print("姚蕾")
