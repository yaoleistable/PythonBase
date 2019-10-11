# noinspection SpellCheckingInspection
def daydayup(df):
    dayup = pow(1+df, 365)
    return dayup


a = 0.01
b = -0.01
print("每天努力{:.2f}时为：{:.2f}，每天下降{:.2f}值为：{:.2f}".format(a, daydayup(a), b, daydayup(b)))

