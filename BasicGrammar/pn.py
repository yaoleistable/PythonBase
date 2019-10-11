# coding=utf-8
# !@Author : YaoLei
# 深圳设计降雨量与年径流总量控制率关系
# 设计降雨量（mm）：[16.9, 23.1, 31.3, 36.4, 43.3, 52.2]
# 年径流总量控制率(%)：[50, 60, 70, 75, 80, 85]


def pn():   # 插值法求年径流总量控制率
    file = '设计降雨量与年径流总量控制率.测试文本'
    fo = open(file, 'r', encoding='UTF-8')
    list_x = eval(fo.readline())
    list_y = eval(fo.readline())
    fo.close()
    # list_x = [16.9, 23.1, 31.3, 36.4, 43.3, 52.2]
    # list_y = [50, 60, 70, 75, 80, 85]
    x = eval(input('输入要求的设计降雨量(16.9~52.2)，单位mm)：'))
    if 16.9 <= x <= 52.2:
        for i in range(len(list_x)):
            if list_x[i] <= x <= list_x[i + 1]:
                y = (list_y[i + 1] - list_y[i]) * (x - list_x[i]) / (list_x[i + 1] - list_x[i]) + list_y[i]
                print("{}mm降雨量对应年径流总量控制率为:{:.2f}%".format(x, y))
            else:
                continue
    else:
        print('输入有误')
    return


def pn_y():   # 插值法求降雨量
    file = '设计降雨量与年径流总量控制率.测试文本'
    fo = open(file, 'r', encoding='UTF-8')
    list_x = eval(fo.readline())
    list_y = eval(fo.readline())
    fo.close()
    # list_x = [16.9, 23.1, 31.3, 36.4, 43.3, 52.2]
    # list_y = [50, 60, 70, 75, 80, 85]
    list_x, list_y = list_y, list_x  # 交换数据
    x = eval(input('输入要求的年径流总量控制率(50~85)，单位%：'))
    if 50 <= x <= 80:
        for i in range(len(list_x)):
            if list_x[i] <= x <= list_x[i+1]:
                y = (list_y[i+1]-list_y[i])*(x-list_x[i])/(list_x[i+1]-list_x[i])+list_y[i]
                print("年径流总量控制率为{}%对应降雨量为:{:.2f}mm".format(x, y))
            else:
                continue
    else:
        print('输入有误')
    return


def main():
    pn()
    pn_y()
    input('Please press enter key to exit ...')


if __name__ == '__main__':
    main()
