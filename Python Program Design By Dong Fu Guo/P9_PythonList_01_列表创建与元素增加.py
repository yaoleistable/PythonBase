#!//miniconda3/envs/py36/bin/
# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@contact: yaoleistable@gmail.com
@software: Lei
@file: P9_PythonList_01_列表创建与元素增加.py
@time: 2019/10/5 9:28 上午
"""
# python常用的序列结构有：列表、元组、字符串、字典、集合以及range等对象

lst = [10, 20, 35, 45]  # 列表这样表示,里面可以包含各种类型元素
# lst.append(14)  # 列表增加元素
lst.extend(lst)  # 将列表l中所有元素添加至lst尾部
lst.remove(20)  # 删除首次出现的指定元素
lst.pop(2)  # 删除并返回lst中下标为index的元素
print(lst)
print(lst.index(10))
print(lst.count(10))  # 返回指定元素x在列表lst中出现的次数
lst.reverse()  # 对列表lst所有元素逆序
print("逆序后：{0}".format(lst))
lst.sort(key=None, reverse=True)  # 对列表lst中的元素排序
print("排序后：{0}".format(lst))
lst.copy()  # 返回列表lst的浅复制
print(lst)
lst = lst + [5]  # 列表后增加元素
print(lst)
lst.clear()  # 删除列表所有元素
print(lst)
del lst  # 删除列表
