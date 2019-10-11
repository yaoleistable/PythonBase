# KochDraw.py 科勒曲线及科勒雪花绘制小包裹
import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)


def main():
    turtle.setup(800, 800)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pensize(2)
    turtle.pencolor('red')
    turtle.pendown()
    level = 3  # 科勒函数阶数
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
    turtle.done()


main()
