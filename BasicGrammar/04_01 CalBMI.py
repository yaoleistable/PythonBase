# CalBMI.py
print("请输入体重（kg):")
weight = eval(input())
print("请输入身高（m):")
height = eval(input())
bmi = weight/(height*height)
d = " "
if bmi >= 28:
    d = "肥胖"
elif 24 < bmi < 27.9:
    d = "偏胖"
elif 18.5 <= bmi <= 24:
    d = "正常"
else:
    d = "偏瘦"
print("您的BMI指数为{:.2f},{}".format(bmi, d))
