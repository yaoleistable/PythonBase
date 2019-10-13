# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@file: P70 Python tkinter.py
@time: 2019/10/13 6:06 下午
"""
# ! /usr/bin/env python

# 1  开一个小窗
from tkinter import *


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("tkinter Menus")
        self.configure(height=120, width=200)
        self.grid(padx=15, pady=15, sticky=N + S + E + W)

        # 2 创建空菜单，加入空菜单
        self.menu = Menu(self)
        self.master.config(menu=self.menu)

        # 3 加入自己的菜单
        self.tkMenu = Menu(self.menu)
        self.menu.add_cascade(label="TkMenu", menu=self.tkMenu)

        self.tkMenu.add_command(label="Simple", command=Simple)
        self.tkMenu.add_separator()
        self.tkMenu.add_command(label="Menu", command=Menu0)


def Simple():
    print("Simple")


def Menu0():
    print("Menu")


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
