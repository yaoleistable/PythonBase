#  字符串处理函数
a = "字符串ABC"
b = 1.23
c = 45
print(len(a))  # 返回字符串x的长度
print(str(b))  # 任意类型x对应的字符串形式
print(hex(c), oct(c))  # 整数x的十六进制或八进制形式字符串
print(chr(9801))  # Unicode编码，chr(x)输出Unicode编码x对应的文字
print(str(ord("你")))  # 输出文字对应的unicode编码
for i in range(12):  # 输出12星座对应的字符
    print(chr(9800+i), end="")

