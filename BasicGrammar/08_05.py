# coding:utf-8
import os


def getword(path):
    f_list = os.listdir(path)
    for i in f_list:
        if i.split('.')[-1] == 'docx':
            print(i)


def getwords(path):
    f_list = os.listdir(path)
    for i in f_list:
        if os.path.splitext(i)[-1] == '.docx':
            print(i)


if __name__ == '__main__':
    path = r'F:\\weiyun\python\\lei_learn\\PythonBase'
    getword(path)
    getwords(path)
