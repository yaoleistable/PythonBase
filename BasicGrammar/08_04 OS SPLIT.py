import os

path = r'F:\\weiyun\python\\lei_learn\\PythonBase'
path2 = r'F:\\weiyun\python\\lei_learn\\PythonBase\\报告模板.docx'

# listdir()函数列出文件夹及文件
filelist = os.listdir(path)
print(filelist)

# os.path.join() 将分离的部分合成一个整体
filename = os.path.join(path)
print(filename)

# os.path.splitext()将文件名和扩展名分开
fname, fename = os.path.splitext(path2)
print(fname)
print(fename)

# os.path.split（）返回文件的路径和文件名
dirname, filename = os.path.split(path2)
print(dirname)
print(filename)

# split（）函数
# string.split(str="", num=string.count(str))[n]
# str - - 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num - - 分割次数。
# [n] - - 选取的第n个分片
