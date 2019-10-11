# 备注的使用
# coding=utf-8
# !@Author : YaoLei

# TempConvert.py
# 温度转换实例

TempStr = input('请输入带有符号的温度值，如82F或18C:')
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print('输入格式错误')


def data_read(file_path):  # 读取文本文件内容并打印
    f = open(file_path, 'r', encoding='UTF-8-sig')
    lis = []
    for line in f:
        line = line.replace('\n', '')
        lis.append(line.split(','))
    f.close()
    print(lis)
    return


data_read('成绩.测试文本')
