# 一、Python开发环境搭建
## 1.1 软件安装
1. 安装3.6.5版本 或直接安装 Anaconda（建议），科学计算的各种包都包含了，方便进行虚拟环境搭建
2. mac 安装 minconda3
3. 安装Pycharm
4. 搭建虚拟环境
5. 使用conda或pip安装软件包
## 1.2 虚拟环境的搭建
	打开终端，conda list 查看；
	//下面是创建python=3.6版本的环境，取名叫py36
	conda create -n py36 python=3.6.9 
	删除环境（不要乱删啊啊啊）
	conda remove -n py36 --all
	激活环境
	conda info -e 查看已按照环境
	//下面这个py36是个环境名
	source activate py36 （Mac 用此命令）
	 conda activate py36 （Windows 用此命令）
	退出环境
	source deactivate
![](_images/虚拟环境01.png)
## 1.3Python模块安装

### 1.3.1pip安装

    安装pyqt5时使用命令：
        pip install pyqt5
        一直因为网络问题无法正确下载。
        然后网上搜了一下，换用了这个命令：
        pip install PyQt5 -i https://pypi.douban.com/simple
        同理 安装pyqt5-tools：
        pip install PyQt5-tools -i http://pypi.douban.com/simple --trusted-host=pypi.douban.com
        解决。
        pip install PyQt5-tools -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com
### 1.3.2手动安装

有时候pip安装python包会失败，提示   未找到和环境相匹配的包。可以试试手动安装。

对于手动安装python包，比如chardet，需要下载解压后放到 Lib->site-packages下面（python安装目录下好像也可以，没放过。site-packages是放第三方包的），然后再chardet的目录下有个setup.py，需要在这个目录下打开命令行，运行python setup.py install 完成编译。这样就完成安装了。

## 1.4更改Python更新源为国内源

	常见的国内源：
	清华：https://pypi.tuna.tsinghua.edu.cn/simple
	阿里云：http://mirrors.aliyun.com/pypi/simple/
	中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
	豆瓣：http://pypi.douban.com/simple/
	在Linux系统中，修改~/.pip/pip.conf文件；在Windows系统中，修改C:\Users\XXX\pip\pip.ini文件。如果没有上述文件，需要手动建立。
	在文件中输入以下内容：
	[global]
	index-url = https://pypi.mirrors.ustc.edu.cn/simple/
	[install]
	trusted-host = mirrors.ustc.edu.cn
## 1.5Mac OS系统下安装Xcode Command Line Tools
    打开终端， xcode-select --install
## 1.6安装homebrew
```python
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

常用命令:
brew --help: 帮助
brew install wget: 安装wget包(Homebrew 会将软件包安装到独立目录, 并将其文件软链接至 /usr/local).
brew search mysql: 搜索.
brew info mysql: 主要看具体的信息. 比如目前的版本, 依赖, 安装后注意事项等.
brew update: 更新Homebrew.
brew outdated: 列出所有安装包里可以升级的包.
brew upgrade: 升级所有可以升级包.
brew cleanup: 清理不需要的版本极其安装包缓存.
brew reinstall mysql: 重新覆盖安装包.
brew uninstall mysql: 卸载
brew doctor: 检查有没有问题
```
## 1.7Git设置	
1. 首先在GitHub创建一个Python库，然后
2. command+k ，提交到本地
3. command+shift+k ，push到GitHub
4. 选择文件夹，提交并push，就可以在GitHub网站看到了
5. github上的版本和本地版本冲突的解决方法
    git push -u origin master -f

![](_images/git01.png)

## 1.8PyCharm设置

### 1.8.1设置代码模板

```
#!//miniconda3/envs/py36/bin/
# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@license: (C) Copyright 2011-2019.
@contact: yaoleistable@gmail.com
@software: Lei
@file: ${NAME}.py
@time: ${DATE} ${TIME}
"""
```

![1571120699771](_images/1571120699771.png)

### 1.8.2Pycharm不自动打开最近项目，显示项目列表

目标： Pycharm如何不自动打开最近项目，显示项目列表。

  路径：File->settings->system settings->startup->reopen lase project on startup。

  操作：勾掉"reopen lase project on startup"，然后，点击【Apply】或【OK】即可！

![1571120908042](_images/1571120908042.png)

### 1.8.3PyCharm插件安装

- **.ignore插件**

  设置里面选择插件，搜索，安装，重启

![1571124889370](_images/1571124889370.png)

- 创建合适的忽略文件

![1571124931942](_images/1571124931942.png)

![1571124959933](_images/1571124959933.png)

### 1.8.4快捷键

- **注释**： 代码选中的条件下，同时按住
  Ctrl+/，被选中行被注释，再次按下Ctrl+/，注释被取消

至此，可以开心的在安装环境中进行Python学习了

# 二、 PyQt5环境搭建

## 2.1安装PyQt5

```python
pip install pyqt5
pip install PyQt5-tools (windows需要安装这个，Mac不用)
```

## 2.2 Qt designer图形界面mac配置

### 2.2.1Qt Designer配置

  打开 pycharm->preference
  找到tools->External Tools，点击➕号新增，如下图所示
![](../Python%20Study%20Notes/_images/qtdesigner01.png)
    Qt Designer
    /miniconda3/envs/py36/bin/Designer.app
    $FileDir$

### 2.2.2PyUIC配置：

```
program  自己的路径，不要选错:/Users/liuchen/PycharmProjects/spiderM/venv/bin/python
这其实就是在命令行中运行就可以的 -m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
$FileDir$ 固定不变
```

![](../Python%20Study%20Notes/_images/Desigener02.png)

### 2.2.3PyRcc配置

pyrcc用于PyQt5的资源文件转码。具体配置与上述内容相同，Arguments填入：

>Program:H:\ProgramData\Miniconda3\envs\py36\Scripts\pyrcc5.exe
>
>Argumennts: $FileName$ -o $FileNameWithoutExtension$_rc.py
>
>Working directory:$FileDir

![1571120226293](_images/1571120226293.png)

## 2.3 Qt designer图形界面Windows配置

  比较简单，百度搜索即可，可参考网址：https://www.jianshu.com/p/51b19e726f50

## 2.4 Qt designer使用流程

  新建GUI图形界面，如下图：
![](../Python%20Study%20Notes/_images/e7b57f9e.png)
  创建的UI文件转换成py文件
  编写主程序，调用图形界面，如下所示。
  参考代码路径：PyQT/P02_UI_Mac_main.py

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQT.P02_UI_Mac import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
```

  



  

