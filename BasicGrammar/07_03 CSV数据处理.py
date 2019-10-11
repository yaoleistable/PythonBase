# coding=utf-8
# !@Author : YaoLei
# read an write CSV
from csv import reader


def read_csv1():
    fo = open('成绩.csv', 'r', encoding='UTF-8-sig')
    ls = []
    for line in fo:
        line = line.replace('\n', '')
        ls.append(line.split(','))
    fo.close()
    print(ls)


def read_csv2():
    fo = open('成绩.csv', 'r', encoding='UTF-8-sig')
    read = reader(fo)
    for line in read:
        print(line)
    fo.close()


def write_csv(list):
    fo = open('成绩.csv', 'a+', encoding='UTF-8-sig')
    for item in list:
        fo.write(','.join(item)+'\n')
    fo.close()


list = [['王五', '88'], ['钟九', '69']]
read_csv1()
# read_csv2()
write_csv(list)
read_csv1()
