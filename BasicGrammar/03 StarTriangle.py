n = eval(input())   # 输入一个奇数N
for i in range(1, n+1):
    a = "*"*i
    if i % 2 in [1]:
        print("{0:^{1}}".format(a, n))  # 关键是对.format()中槽机制的理解，槽中可以嵌套槽，用来表示宽度、填充等含义
