#  TextProBar.py
import time
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = "*"*i
    b = "."*(scale-i)  # 注意此处为scale-i
    c = (i/scale)*100
    d = time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, d), end="")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, "-"))

