#!//miniconda3/envs/py36/bin/
# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@contact: yaoleistable@gmail.com
@software: Lei
@file: P52-P57 Python文件操作1.py
@time: 2019/10/6 8:51 上午
"""
import pickle
import struct
import shelve

# 第7章 文件操作
# P52 1：文件对象基本用法
'''
    文本文件、二进制文件
    文件操作步骤：打开、读写、关闭
    open(fiel,mode='r',buffering =-1,encoding=None,errors=None.
    newline=None,closefd=True,opener=None)
'''
path = r"/Users/yaolei/PycharmProjects/PythonBase/Python Program Design By Dong Fu Guo/测试文本.txt"
f = open(path, "r")  # 打开文件
f.close()  # 关闭文件

# 推荐使用with管理打开文件
'''
    with open(filename,mode,encoding)as fp
'''
path_new = r"/Users/yaolei/PycharmProjects/PythonBase/Python Program Design By Dong Fu Guo/测试文本new.txt"
with open(path, "r")as src, open(path_new, 'w')as dst:
    dst.write(src.read())
    src.close()
    dst.close()
    print(src.closed)  # 判断文件是否关闭
    print(f.mode)  # 返回文件的打开模式
    print(f.name)  # 返回文件的名称
    print(f.buffer)  # 返回当前文件的缓冲区对象

# P53 2：文件对象基本用法2
'''
    文件打开方式：
    r 读模式
    w 写模式，如果文件存在，先清空原有内容
    x 写模式，创建新文件，如果文件存在则抛出异常
    a 追加模式，不覆盖文件中原有内容
    b 二进制模式
    t 文本模式，默认模式，可省略
    + 读、写模式
'''

# P54 3：文本文件操作例题讲解
s = 'hello world\n文本文件的读取方法\n文本文件的写入方法\n'
with open('sample.txt', 'w') as fp:
    fp.write(s)
with open('sample.txt')as fp:
    # print(fp.read())
    for line in fp:
        print(line)

filename = 'demo1.py'
with open(filename, 'r')as fp:
    lines = fp.readlines()
maxLength = len(max(lines, key=len))
index = 1
lines = [line.rstrip() + ' ' * (maxLength - len(line)) + '#' + str(index + 1) + '\n'
         for index, line in enumerate(lines)]
with open(filename[:-3] + 'new.py', 'w')as fp:
    fp.writelines(lines)

# P55 4：使用pickle模块操作二进制文件
'''
Pickle模块中最常用的函数为：
（1）pickle.dump(obj, file, [,protocol])
    函数的功能：将obj对象序列化存入已经打开的file中。
    参数讲解：
    obj：想要序列化的obj对象。
    file:文件名称。
protocol：序列化使用的协议。如果该项省略，则默认为0。如果为负值或HIGHEST_PROTOCOL，则使用最高的协议版本。
（2）pickle.load(file)
    函数的功能：将file中的对象序列化读出。
    参数讲解：
    file：文件名称。
'''
# 写入二进制文件
i = 130000
a = 99.056
s = '中华人民共和国'
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tu = (-5, 8, 10)
coll = {4, 5, 6}
dic = {'a': 'apple', 'b': 'banana', 'g': 'grape'}
data = [i, a, s, lst, tu, coll, dic]
with open('sample_pickle.dat', 'wb') as f:  # 'wb'写入二进制文件
    try:
        pickle.dump(len(data), f)  # 表示后面将要写入的数据个数
        for item in data:
            pickle.dump(item, f)
    except:
        print('写文件异常！')
# 读取二进制文件
with open('sample_pickle.dat', 'rb')as f:
    n = pickle.load(f)  # 读出文件的数据个数
    for i in range(n):
        x = pickle.load(f)
        print(x)

# P56 5：使用struct模块操作二进制文件
# struct写入
n = 132467
x = 956.78
b = True
s = 'a1@中国'
sn = struct.pack('if?', n, x, b)  # 序列化
f = open('sample_struct.dat', 'wb')
f.write(sn)
f.write(s.encode())  # 字符串直接编码为字节码写入
f.close()
# struct读取二进制文件
print('struct文件读取')
f = open('sample_struct.dat', 'rb')
sn = f.read(9)  # 读取9个字节
tu = struct.unpack('if?', sn)
print(tu)
n, x, b1 = tu
print('n=', n)
print('x=', x)
print('b1=', b1)
s = f.read(9).decode()
f.close()
print('s=', s)

# P57 6：使用shelve和marshal模块操作二进制文件
# 写入
zhangsan = {'age': 38, 'sex': 'male', 'address': 'sdibt'}
lisi = {'age': 40, 'sex': 'man', 'qq': '123456'}
with shelve.open('shelve_test.dat')as fp:
    fp['zhangsan'] = zhangsan  # 以字典形式把数据写入文件
    fp['lisi'] = lisi
    for i in range(5):
        fp[str(i)] = str(i)

# 读取
with shelve.open('shelve_test.dat')as fp:
    print(fp['zhangsan'])


