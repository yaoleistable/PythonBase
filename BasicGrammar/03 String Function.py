# 字符串处理方法
a = "adfaFsbaAbSq12"
b = "A,B,C"
c = "+"
print(a.lower())  # 字符串全部小写
print(a.upper())  # 字符串全部大写
print(b.split(","))  # 分隔函数
print(a.count("a"))  # 计数函数
print(a.replace("a", "1"))  # 替换函数
print(b.center(20, "="))  # 居中处理
print(a.strip("a2"))  # strip(chars) 从str中去掉在其左侧和右侧chars中列出的字符
print(c.join(a))  # str.join(iter) 在变量除最后元素外每个元素后增加一个str
