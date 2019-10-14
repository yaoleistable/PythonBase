# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@file: P68-P69 Python tkinter.py
@time: 2019/10/13 4:52 下午
"""
import tkinter
import tkinter.messagebox

# Python标准库tkinter是对Tcl/Tk的进一步封装
"""
常用组件：


"""
# 创建应用程序主窗口
root = tkinter.Tk()

# 在窗口上创建标签组件
lableName = tkinter.Label(root,
                          text='User Name:',
                          justify=tkinter.RIGHT,
                          width=80)
lableName.place(x=10, y=5, width=80, height=20)

# 创建字符串变量和文本框组件，同时设置关联的变量
varName = tkinter.StringVar(root, value='')
entryName = tkinter.Entry(root,
                          width=80,
                          textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)

lablePwd = tkinter.Label(root,
                         text='User Pwd:',
                         justify=tkinter.RIGHT,
                         width=80)
lablePwd.place(x=10, y=30, width=80, height=20)

# 创建密码文本框
varPwd = tkinter.StringVar(root, value='')
entryPwd = tkinter.Entry(root,
                         show='*',
                         width=80,
                         textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)


# 登录按钮事件处理函数
def login():
    # 获取用户名和密码
    name = entryName.get()
    pwd = entryPwd.get()
    if name == 'admin' and pwd == '123456':
        tkinter.messagebox.showinfo(title='恭喜',
                                    message='登录成功！')
    else:
        tkinter.messagebox.showinfo(title='警告',
                                    message='用户名和密码不匹配')


# 创建按钮组件，同时设置按钮事件处理函数
buttonOK = tkinter.Button(root,
                          text='Login',
                          command=login)
buttonOK.place(x=30, y=70, width=50, height=20)


# 取消按钮的事件处理函数
def cancel():
    varName.set('')
    varPwd.set('')


buttonCancel = tkinter.Button(root,
                              text='Cancel',
                              command=cancel)
buttonCancel.place(x=90, y=70, width=50, height=20)

# 启动消息主循环，启动应用程序
root.mainloop()
