# 学习文件的打开
# 文件操作的步骤：打开-操作-关闭


def read_txt1():  # 遍历全文本，方法一
    fo = open('文件操作.测试文本', 'r', encoding='UTF-8')  # 文件路径需要为反斜杠\或／／，如'd:\45\3.tet'，
# 'r' 只读 'w' 覆盖写模式 'x' 创建写模式 'a'追加写模式 't' 文件以文本文件打开，'b' 文件以二进制打开
# '+' 与r/w/x/a一同使用，增加同时读写功能
    txt = fo.read()  # 读人全部内容,一次读入，全文处理
    fo.close()  # 文件的关闭
    return print(txt)


def read_txt2():  # 遍历全文本，方法二
    fo = open('文件操作.测试文本', 'r', encoding='UTF-8')
    txt = fo.read(2)
    while txt != "":
        txt = fo.read(2)  # 按数量读入，逐步处理
    fo.close()
    return print(txt)


def read_txt3():  # 逐行遍历文件，方法一
    fo = open('文件操作.测试文本', 'r', encoding='UTF-8')
    for line in fo.readlines():
        print(line)
    fo.close()


def read_txt4():  # 逐行遍历文件，方法二
    fo = open('文件操作.测试文本', 'r', encoding='UTF-8')
    for line in fo:
        print(line)
    fo.close()


# read_txt4()


def write_txt1():
    fo = open('文件写入.测试文本', 'w+', encoding='UTF-8')
    fo.write("我爱中国")  # 向文件中写入字符串
    ls = ['china', 'jeep', 'jap']
    fo.writelines(ls)  # 将一个元素全为字符串的列表写入文件
    fo.seek(0)  # 0 文件开头 1 当前位置 2 文件结尾 ,如无此行，则无法输出
    for line in fo:
        print(line)
    fo.close()


write_txt1()
