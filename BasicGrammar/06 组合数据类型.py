# 第6章组合数据类型
# 集合类型、序列类型（元组和列表）、字典类型
# jieba库的学习
# 6.1 集合类型及操作
# 放入集合中的元素，不可被修改，集合中元素是独一无二的，集合用{}表示，集合是无序的
a = {'python', 123, 'p', 'o', ('python', 123)}  # 使用{}建立集合
b = set("python123")  # 使用set()建立集合，将其他类型变量转变为集合类型
print(a)
print(b)
# 集合操作符，集合间操作，并 S|T、差S-T、交S&T、补S^T 及关系操作符，如>= 、<等
# 四个增强操作符，S|=T(更新集合S，包括在集合S和T中的所有元素)、S-=T S&=T S^=T
a ^= b
print(a)
#  集合的操作方法
a.add('they')  # 在集合中增加元素
b.discard("y")  # 在集合中移除元素
print(a)
print(b)
print(b.remove("n"))  # 在集合中移除元素,如不在里面，报错
print(b.clear())  # 清除集合中所有元素
print(a.pop())  # 随机返回集合的一个元素
print(a.copy())  # 拷贝集合，形成副本
print(len(a))  # 返回集合的元素的个数

ls = ['p', 'y', 'y', '1', 'p', '3']
s = set(ls)  # 集合应用于数据去重
lt = list(s)  # 将集合转换为列表
print(lt)



