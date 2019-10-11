# 序列，是具有先后顺序的一组元素，序列是一维元素向量，元素类型可以不同，序列是一个基类类型
# 序列包含字符串类型、元组类型、列表类型


def get_number():  # 获得用户不定长度定输入
    nums = []
    inumstr = input("请输入数字（回车退出）:")
    while inumstr != "":
        nums.append(eval(inumstr))
        inumstr = input("请输入数字（回车退出）:")
    return nums


def mean(number):  # 计算平均数
    s = 0.0
    for num in number:
        s = s+num
    return s/len(number)


def dev(number, mean):  # 计算方差
    sdev = 0.0
    for num in number:
        sdev = sdev + (num-mean)**2
    return pow(sdev/(len(number)-1), 0.5)


def median(number):  # 计算中位数
    sorted(number)
    size = len(number)
    if size % 2 == 0:
        med = (number[size//2-1]+number[size//2])/2
    else:
        med = number[size//2]
    return med


n = get_number()
m = mean(n)
print("平均值:{}，方差:{:.2f},中位数:{}".format(m, dev(n, m), median(n)))
