# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@file: 文件重命名 从文本文件.py
@time: 2019/10/12 12:45
"""
import os


# 文件重命名，从文本文件
def file_rename(txt_path, file_dir):
    with open(txt_path, 'r', encoding='UTF-8') as f:
        s = f.readlines()
        print(s)
    file_name = os.listdir(file_dir)
    print(file_name[0])
    for i in range(len(s)):
        old_name = os.path.join(file_dir, file_name[i])

        new_name = old_name[0:-4:1]+' '+s[i].strip()+'.pdf'
        print('旧文件:', old_name)
        print('新文件:', new_name)
        i = i + 1
        os.rename(old_name, new_name)


if __name__ == "__main__":
    txt_path = r'C:\Users\yaole\Desktop\result.txt'
    file_dir = r'C:\Users\yaole\Desktop\PDF'
    file_rename(txt_path, file_dir)
