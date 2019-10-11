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
# pip的使用：
"""
1.查看python解释器的版本
　　python --version
2.查看pip的版本
　　pip --version
　　pip show pip
3.查看pip的帮助
　　pip --help
4.查看python的帮助
　　python --help
5.查看pip安装的外部包
　　pip list
6.查看需要更新的外部包
　　pip list --outdated
7.pip在线安装外部包
　　pip install 包名
8.pip在线通过镜像网站安装外部包
　　pip install -i https://pypi.tuna.tsinghua.edu.cn/simple包名
9.pip离线安装外部包
　　pip install 将下载好的包拖到此处（注意：包名不能修改）
10.pip卸载包
　　pip uninstall 包名
11.pip更新pip和外部包
　　pip install --upgrade pip或者外部包
12.通过镜像网站更新外部包
　　pip install -U -i https://pypi.tuna.tsinghua.edu.cn/simple 包名
13.更改pip的默认下载网站
　　在用户目录下新建一个pip文件夹，在里面新建一个pip.ini文件，文件里面写上以下内容：
　　[global]
　　Index-url = https://pypi.tuna.tsinghua.edu.cn/simple
14.使用pip安装jupyter，并修改器默认启动路径,
　　(1) pip install jupyter
　　(2) 生成jupyter的配置文件
　　　  jupyter notebook --generator-config
　　(3) 将要指定的路径填入 #c.NotebookApp.notebook_dir = ' ' 中的 ' ' 中即可，同时注意将 #c 中的 # 删去
15.安装requirements.txt文件中指定的扩展库
    pip install -r requirements.测试文本
16.以requirements格式列出已安装模块
    pip freeze [requirements.测试文本]
"""
# conda的使用：
'''
    打开终端，conda list 查看；
    下面是创建python=3.6版本的环境，取名叫py36
    conda create -n py36 python=3.6 
    删除环境（不要乱删啊啊啊）
    conda remove -n py36 --all
    激活环境
    下面这个py36是个环境名
    source activate py36
    退出环境
    source deactivate
'''
# 常用内置对象
# 1.数字类型 int、float、complex
a = 32
print("数字类型：", a)
# 2.字符串 str
b = '你好'
c = "你好"
d = '''你好'''
print("字符串类型：", b)
# 3.字节串 bytes 以字母b引导
e = b'hello'
print("字节串类型：", e)
# 4.列表 list
f = [1, 2, 3]
g = ['a', 'b', ['c', 2]]
for i in f:  # 打印列表
    print("打印列表类型元素：", i)
for i in g:
    print("打印列表类型元素：", i)

# 5.字典 dict
h = {1: 'food', 2: 'taste', 3: 'import'}
for i in h:  # 打印字典
    print("打印字典类型元素：", i)
# 6.元祖 tuple
k = (2, -5, 6)
for i in k:  # 打印元祖
    print("打印元祖类型元素：", i)
# 7.集合 set、frozenset
l = {'a', 'b', 'c'}
for i in l:  # 打印集合
    print("打印集合类型元素：", i)
# 8.布尔型 bool（true or false）

# 9.空类型 None
# 10.异常 Exception、ValueError、TypeError
# 11.文件 f = open('data.dat','rb')
# 12.其他迭代对象 生成器对象、range对象、zip对象、enumerate对象、map对象、filter对象等等
# 13.编程单元 函数（def定义）、类（class定义）、模块（module定义）
