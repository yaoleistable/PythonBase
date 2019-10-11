import time as t
start = t.perf_counter()
print(t.time())  # 打印时间字符串
print(t.ctime())  # 打印系统当前时间
print(t.gmtime())  # 获取当前时间，打印为计算机可处理的时间格式
print(t.strftime("%Y-%m-%d %H:%M:%S", t.gmtime()))  # 格式化时间
timeStr = "2018-12-03 12:46:45"
print(t.strptime(timeStr, "%Y-%m-%d %H:%M:%S"))
end = t.perf_counter()  # 测量时间 单位ns
print("本段程序耗时:{}ns".format(end-start))


def wait():
    t.sleep(2)


print(wait())

