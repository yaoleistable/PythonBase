#!//miniconda3/envs/py36/bin/
# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@contact: yaoleistable@gmail.com
@software: Lei
@file: P11_PythonList_03_列表切片操作.py
@time: 2019/10/5 5:41 下午
"""
import random

# 2.1.4 列表元素访问与计数
lst = [0, 3, 7, 5, 0, 3]
a = lst.count(3)
print("列表中3的个数为：", a)

# 2.1.5成员资格判断
print("判断成员是否属于列表", 3 in lst)
print("判断成员是否属于列表", 18 in lst)
print("判断成员是否属于列表", 4 not in lst)

# 2.1.6切片操作
# 适用于列表、元组、字符串、range对象等类型
# 切片为浅复制，是指生成一个新的列表，并且把原列表所有元素的引用都复制到新列表中。
# lst[start:end:step]
print("切片第三位表示步长:", lst[::-1])
print("切片第三位表示步长:", lst[::2])  # 偶数位置
print("切片第三位表示步长:", lst[1::2])  # 奇数位置
print("切片第三位表示步长:", lst[2:4])
lst[len(lst):] = [9]
print("尾部追加元素:", lst)
lst[:3] = {0, 2, 4}
print("替换列表前3个元素:", lst)
lst[:3] = []
print("删除列表前3个元素:", lst)
lst = lst * 2  # 列表翻倍
del lst[:3]  # 删除前三个元素
print(lst)
del lst[::2]  # 删除偶数位置
print(lst)
# 2.1.7 列表排序
# sort()方法
lst_b = [5, 7, 2, 3, 6, 8, 0]
random.shuffle(lst_b)  # 类似洗牌，打乱列表元素顺序
lst_b.sort()  # 默认升序排列
print("排序后的列表", lst_b)
lst_b.sort(reverse=True)  # 降序排列
print("排序后的列表", lst_b)
# reversed()反转函数，返回迭代对象
lst_c = reversed(lst_b)
# 通过list()函数将迭代对象转换为列表
print("反转后的新列表为:", list(lst_c))
# 2.1.8 用于列表操作的其他内置函数
# len(list)求长度
# max(list)、min(list)
# sum(list) 对列表元素求和
