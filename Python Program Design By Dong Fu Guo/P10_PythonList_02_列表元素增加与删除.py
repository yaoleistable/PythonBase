#!//miniconda3/envs/py36/bin/
# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@contact: yaoleistable@gmail.com
@software: Lei
@file: P10_PythonList_02_列表元素增加与删除.py
@time: 2019/10/5 4:41 下午
"""
import time

# 2.1.2
lst = [1, 5, 7, 4, 2, 9]
# 列表增加元素方法一：+
lst = lst + [8]
# 列表增加元素方法二：append(),速度快
lst.append(25)


def list_1():  # 列表增加元素速度测试1
    result = []
    start = time.time()
    for i in range(10000):
        result = result + [i]
    print(len(result), ',', time.time() - start)
    print(id(result))


def list_2():  # 列表增加元素速度测试2
    result = []
    start = time.time()
    for i in range(10000):
        result.append(i)
    print(len(result), ',', time.time() - start)
    print(id(result))


list_1()
list_2()

a = [1, 2, 3]
b = [1, 2, 3]
print("元素内存地址:")
print(id(a))  # 元素内存地址
print(id(b))
print(a == b)
print(id(a) == id(b))
print(id(a[0]) == id(b[0]))
# 列表增加元素方法三：extend()
a.extend([7, 8, 9])  # 将另一个迭代对象增加到尾部
print(a)
# 列表增加元素方法四：insert() 插入元素 ,由于自动内存管理，速度较慢
b.insert(1, 5)
print("列表b插入元素后：", b)
# 列表增加元素方法五：使用乘法
print(a * 3)
# 2.1.3 列表元素的删除
c = [0, 5, 2, 7, 9]
del c[2]  # 通过del删除元素
print("删除元素后的列表:", c)
c.pop(1)  # 通过pop删除元素
print("通过pop删除元素后:", c)
c.remove(5)  # 通过remove删除元素
print("通过remove删除元素后：", c)

