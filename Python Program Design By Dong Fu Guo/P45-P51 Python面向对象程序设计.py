#!//miniconda3/envs/py36/bin/
# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@contact: yaoleistable@gmail.com
@software: Lei
@file: P45-P51 Python面向对象程序设计.py
@time: 2019/10/6 8:30 上午
"""

# P45 1：类的定义与使用、self参数
# 第6章 面向对象程序设计
# 计算机程序由多个能够起到子程序作用的单元或对象组合而成
# 封装、继承、多态
# Python中一切内容都可以成为对象

# 类的所有实例方法都不许至少有一个名为self的参数，
# 且必须是方法的第一个形参，self参数代表将来要创建的对象本身
from this import s


class Car:
    price = 100000  # 定义类属性

    def __init__(self, c):
        self.speed = None
        self.color = c  # 定义实例属性

    def info(self):
        print("This is a car")

    def demo(self):
        pass  # 空语句


car1 = Car("Red")  # 实例化对象
car2 = Car("Blue")
print(car1.color, Car.price)  # 查看实例属性和类属性的值

car1.info()

# P46 2：类成员与实例成员

Car.price = 110000
Car.name = "QQ"  # 动态增加类属性
car1.color = "Yellow"
print(car2.color, Car.price, Car.name)
print(car1.color, Car.price, Car.name)

import types


def setSpeed(self, s):
    self.speed = s


car1.setSpeed = types.MethodType(setSpeed, car1)  # 动态增加成员方法
car1.setSpeed(50)
print(car1.speed)
# P47 3：私有成员与公有成员
'''
    Python么有对私有成员提供严格的访问保护机制
        在定义类成员时，如果成员名以两个下划线"__"或更多下划线开头而不以两个
        或更多下划线结束则表示是私有成员。
        私有成员在类的外部不能直接访问，需要调用对象的公开方法类访问
'''


class A:
    def __init__(self, value1=0, value2=0, value3=0):
        self._value1 = value1  # 受保护的成员
        self.__value2 = value2  # 私有成员
        self.value3 = value3  # 公开成员

    def setValue(self, value1, value2, value3):
        self._value1 = value1
        self.__value2 = value2
        self.value3 = value3

    def show(self):
        print(self._value1, self.__value2, self.value3)


a1 = A()
a1.show()
a2 = A(13, 15)
print(a2._value1)
print(a2._A__value2)  # 在外部访问对象的私有数据成员,此处为特殊的方法               a2.show()
print(a2.value3)
a2.show()
print(dir(A))


# P48 4：成员方法、类方法、静态方法
class Root:
    __total = 0  # 私有成员

    def __init__(self, v):  # 构造方法
        self.__value = v
        Root.__total += 1

    def show(self):  # 普通实例方法
        print('self.__value:', self.__value)
        print('Root.__total:', Root.__total)

    @classmethod  # 修饰器，声明类方法
    def classShowTotal(cls):  # 类方法
        print(cls.__total)

    @staticmethod  # 修饰器，声明静态方法
    def staticShowTotal():  # 静态方法
        print(Root.__total)


root1 = Root(15)
root1.show()
root1.classShowTotal()
root1.staticShowTotal()
root2 = Root(20)
root2.show()
Root.staticShowTotal()  # 通过类名调用静态方法
root3 = Root(3)
Root.classShowTotal()  # 通过类名调用类方法


# P49 5：属性定义与使用
class Test:
    def __init__(self, value, name="姚蕾"):
        self.__value = value
        self.__name = name

    def __get(self):
        return self.__name

    def __set(self, name):
        self.__name = name

    name = property(__get, __set)  # 可读、可写属性

    def __set(self, sex):
        self.__sex = sex

    def __get(self):
        return self.__sex

    def __del(self):  # 定义删除
        del self.__sex

    def show(self):
        print(self.__name)

    sex = property(__get, __set, __del)  # 定义可读、可写、可删除属性

    @property
    def value(self):  # 只读属性，无法修改和删除
        return self.__value


t1 = Test(5)
print('属性值为:', t1.value)
t1.show()
print(t1.name)
t1.name = "姚林"
print(t1.name)
t1.sex = "男"
print(t1.sex)
del t1.sex


# P50 6：特殊方法及其含义
# 构造函数 __init__()
# 析构函数 __del__()
# 类的静态方法 __new__(),用于确定是否要创建对象
# __add__() +
# __sub__() -
# __mul__() *
# __truediv__() /
# __floordiv__() //
# __mod__() %
# __pow__() **


# P51 7：例题讲解1自定义数组
class MyArray:
    def __IsNumber(self, n):
        return isinstance(n, (int, float, complex))

    def __init__(self, *args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__IsNumber(arg):
                    print("所有元素必须是数字")
            self.__value = list(args)

    # 重载运算符+
    # 数组中每个元素都与数字n相加，或两个数组相加，返回新数组
    def __add__(self, n):
        if self.__IsNumber(n):
            # 数组中所有元素都与数字n相加
            b = MyArray()
            b.__value = [item + n for item in self.__value]
            return b
        elif isinstance(n, MyArray):
            # 两个等长的数组对应元素相加
            if len(n.__value) == len(self.__value):
                c = MyArray()
                c.__value = [i + j for i, j in zip(self.__value, n.__value)]
                return c
            else:
                print("长度不相等")
        else:
            print("不支持相加")

    # 重载运算符-
    def __sub__(self, n):
        if not self.__IsNumber(n):
            print("不支持" + type(n) + "操作")
            return
        b = MyArray()
        b.__value = [item - n for item in self.__value]
        return b

    if __name__ == '__main__':
        print("please use me as a module")
