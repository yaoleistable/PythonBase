import turtle as t
t.setup(800, 400, 200, 200)   # 设置绘图窗口
t.penup()  # 抬起画笔，海龟飞行
t.fd(-250)  #
t.pendown()  # 画笔落下，海龟在爬行
t.pensize(25)  # 画笔尺寸
t.pencolor("purple")  # 画笔颜色
# t.forward(100)  # 运动控制函数，向前走
# t.circle(-100, 90)  # 运动控制函数，弧型走
t.setheading(-40)
for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 80/2)
t.fd(40)
t.circle(16, 180)
t.fd(40*2/3)
# t.left(30)
# t.right(30)
t.done()



