#!//miniconda3/envs/py36/bin/
# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@contact: yaoleistable@gmail.com
@software: Lei
@file: P58-P63 Python文件操作2：OS操作.py
@time: 2019/10/7 6:09 下午
"""
# P58 7：os、os.path、shutil模块基本用法
# 创建临时文件和文件夹可以使用tempfile模块
# pathlib
import os
import os.path

'''
os模块常用函数
    access(path,mode)测试是否可以按照mode制定的权限访问文件
    chdir(path) 把path设为当前工作目录
    chmod(path,mode.*,dir_fd=None,follow_symlinks=True)改变 文件的访问权限
    curdir 当前文件夹
    environ 包含系统环境变量和值的字典
    getcwd()返回当前工作目录
    listdir(path)返回path目录下的文件和目录列表
    remove(path)删除指定的文件
    rename(src,dst)重命名文件或目录
    system()启动外部程序
    
'''
print(os.curdir)
# print(os.environ)
# print(os.scandir())
print(os.getcwd())

'''
os.path常用文件操作函数
    abspath(path) 返回给定路径的绝对路径
    basename(path)返回指定路径的最后一个组成部分
    dirname(p)返回给定路径的文件夹部分
    exists(path)判断文件是否存在
    getsize(filename)返回文件的大小
    isdir(path) 判断path是否为文件夹
    isfile(path)判断path是否为文件
    join(path,*paths)连接两个或多个path
    split(path)
'''
path = '/Users/yaolei/PycharmProjects/PythonBase/Python Program Design By Dong Fu Guo/P1_PythonBasic_01_安装、版本.py'
abspath = os.path.abspath(path)
basename = os.path.basename(path)
dirname = os.path.dirname(path)
exists = os.path.exists(path)
getsize = os.path.getsize(path)
isdir = os.path.isdir(path)
split = os.path.split(path)
splitdrive = os.path.splitdrive(path)
splitext = os.path.splitext(path)
print('abspath =', abspath)
print('basename =', basename)
print('dirname =', dirname)
print('exists =', exists)
print('getsize =', getsize)
print('isdir =', isdir)
print('split =', split)
print('splitdrive =', splitdrive)
print('splitext =', splitext)

print('单元文件路径下后缀名为.py的文件')
for fname in os.listdir(os.getcwd()):
    if os.path.isfile(fname) and fname.endswith('.py'):
        print(fname)
# 列表表达式执行
print('列表表达式单元文件路径下后缀名为.py的文件')
[print(fname) for fname in os.listdir(os.getcwd())
 if os.path.isfile(fname) and fname.endswith('.py')]
file_list = [filename for filename in os.listdir('.') if filename.endswith('.txt')]
for filename in file_list:
    pass
#   newname = filename[:-3] + 'docx'
#   os.rename(filename, newname)
#   print(filename+'更名为：'+newname)
# shutil模块的使用
'''高级的文件，文件夹，压缩包的处理模块,也主要用于文件的拷贝'''

# P59 8：常用文件夹操作

# P60 9：综合例题讲解1

# P61 10：综合例题讲解2

# P62 11：综合例题讲解3

# P63 12：综合例题讲解4
