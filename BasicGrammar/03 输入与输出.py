# -*- coding:utf-8 -*-
# 开发人员： yaolei
# 文件名称： 03 输入与输出.py
import keyword
import datetime
now_year = datetime.datetime.now().year
now_m = datetime.datetime.now().month
print("今年是"+str(now_year)+"年"+str(now_m)+"月")
print("大头儿子\n小头爸爸")
print("6"*3)
print("平生不会相思，\
才会相思，便害相思。")
print(r"平生不会相思，\
才会相思，便害相思。")   # 加入r后，转义符就会失效
print(keyword.kwlist)
a = 4
b = "你的眼神"
print(type(a))
print(type(b))
no = number = 2048
print(id(no))  # id()函数返回变量的内存地址
print(no)
print(id(number))

while True:
    a = input("请输入一个字符：")
    if len(a) >= 2:
        print("输入错误，请输入一个字符")
    else:
        print(a+"的ASCII码为：", ord(a))

