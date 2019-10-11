import os
print(os.path.relpath('1.py'))
print(os.path.abspath('1.py'))  # 获取当前工作目录路径
print(os.getcwd())  # 获取当前工作目录路径
print(os.path.abspath('.'))  # 获取当前工作目录路径
print(os.path.abspath('..'))  # 获取当前工作的父目录 ！注意是父目录路径
print(os.path.abspath(os.curdir))  # 获取当前工作目录路径
