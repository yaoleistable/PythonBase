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
import you_get
import os
import platform
'''
下载网站歌曲、视频等
'''
sys_str = platform.system()  # Darwin
# Mac系统执行如下命令
# print(sys_str)
# print('当前目录文件有:')
# print(os.system('ls'))
# print('当前时间为:')
# print(os.system('date'))
# url_str = "https://www.kugou.com/song/#hash=B9F1789EDC96760E6DBDF9B91D8B259B&album_id=29498302"
# 下载网易云音乐，需先解析获得真实下载地址，通过油猴插件可以获得
url_str = "http://m10.music.126.net/20191004101926/8932abdf05ed22cb1bb88a15a28e4ba4/ymusic/015d/0059/065e" \
          "/67740c9f7a73955cd7f31461ad05f7e0.mp3 "
# command = 'you-get -h' # you-get帮助文件
# print(os.system(command))
# path = r'/Users/yaolei/PycharmProjects/PythonBase/Python Program Design By Dong Fu Guo/Download'
command_download = 'you-get' + ' ' + '\'' + url_str + '\''
print(command_download)
os.system(command_download)
