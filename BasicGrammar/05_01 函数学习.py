def fact(n, m=1):  # 定义求阶乘函数，m为可选参数，放在不可选参数之后
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m, n, m  # return 可以返回多个值


def fact2(n, *b):  # *b代表可变参数
    s = 1
    for i in range(1, n+1):
        s *= i
    for item in b:
        s *= item
    return s


def fact3(n):  # 求n的阶乘，理解函数递归
    if n == 0:
        return 1
    else:
        return n*fact3(n-1)


def rvs(s):  # 反转字符串
    if s == '':
        return s
    else:
        return rvs(s[1:])+s[0]


def f(n):  # 斐波那契函数，递归重点理解n与n-1直接的关系，不关注具体的实现过程
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)


a = fact(10)
b = fact(10, 8)
c = fact2(10, 3, 2, 4)
print(a, b, c)
d = fact3(5)
print(d)
print(rvs('87sujj61'))
e = 10
print("{0}的斐波那契函数值为：{1}".format(e, f(e)))



