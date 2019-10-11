def data_ct(file_path):  # 空格分隔读入文件
    f = open(file_path, 'r+', encoding='UTF-8')
    txt = f.read()
    ls = txt.split()
    f.close()
    return print(ls)


def data_ct2(file_path):  # 特殊符号分隔读入文件
    f = open(file_path, 'r+', encoding='UTF-8')
    txt = f.read()
    ls = txt.split('#')
    f.close()
    return print(ls)


def data_write(file_path, list):
    f = open(file_path, 'w+', encoding='UTF-8')
    f.write('#'.join(list))
    f.close()
    return print("写入成功")


def data_read(file_path):
    f = open(file_path, 'r', encoding='UTF-8')
    lis = []
    for line in f:
        line = line.replace('\n', '')
        lis.append(line.split(','))
    f.close()
    print(lis)
    return


ls = ['日本', '加拿大', '巴西']
file = "一维数据写入.测试文本"
file2 = "成绩.测试文本"
data_write(file, ls)
data_ct2(file)
data_read(file2)


