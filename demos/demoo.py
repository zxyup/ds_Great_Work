# # QLabel控件的基本用法
#
# import sys
# # 导入QLabel模块  QVBoxLayout垂直布局  (QHBoxLayout 水平布局)
# from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
# # 导入调制板，调制QLabel背景色
# # 导入显示图片包QPixmap
# from PyQt5.QtGui import QPixmap,QPalette
# # 导入一些Qt的常量
# from PyQt5.QtCore import Qt
#
# # 编写一个类，从QWidget中继承
# class QLabelDemo(QWidget):
#     def __init__(self):
#         super().__init__()
#         # 调用初始化UI的一个方法
#         self.initUI()
#
#     # 规范代码，初始化UI直接写在一个方法里
#     def initUI(self):
#         # 创建四个label控件
#         label1 = QLabel(self)
#         label2 = QLabel(self)
#         label3 = QLabel(self)
#         label4 = QLabel(self)
#
#
#         # 给label1设置文本,支持html的标签
#         label1.setText("<font color=purpel>这是一个文本标签.</font>")
#         # 用调试板自动填充背景
#         label1.setAutoFillBackground(True)
#         # 创建调试板
#         palette = QPalette()
#         # 给调试板设置背景色
#         palette.setColor(QPalette.Window,Qt.blue)
#         # 对label1使用调试板
#         label1.setPalette(palette)
#         # 让label1居中对齐
#         label1.setAlignment(Qt.AlignCenter)
#
#
#         # 给label2设置<a>标签
#         label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")  # 可以在a标签里触发事件或者跳转网页 二者选其一
#
#         # 给label3设置文本居中
#         label3.setAlignment(Qt.AlignCenter)
#         # 给label3设置提示文本
#         label3.setToolTip('这是一个图片标签')
#         # 让label3显示图片
#         label3.setPixmap(QPixmap("./images/4.jpg"))   # 同级目录写法./images
#
#         # 给label4设置文本内容
#         label4.setText("<a href='https://www.baidu.com/'>打开百度</a>")  # setText里面的内容要用双引号，单引号会报错
#         # 让label4打开链接
#         # 如果设为True,用浏览器打开网页，如果设为False,调用槽函数
#         label4.setOpenExternalLinks(True)
#         # 让label4的文本右对齐
#         label4.setAlignment(Qt.AlignRight)
#         # 给label4设置提示文本
#         label4.setToolTip('这是一个超链接')
#
#         # 创建一个垂直布局
#         vbox = QVBoxLayout()
#         # 分别把这四个控件放到这个布局里面           布局函数 addWidget
#         vbox.addWidget(label1)
#         vbox.addWidget(label2)
#         vbox.addWidget(label3)
#         vbox.addWidget(label4)
#
#         # 将信号与槽绑定
#         label2.linkHovered.connect(self.linkHovered)
#         label4.linkActivated.connect(self.linkClicked)
#
#         # 设置布局
#         self.setLayout(vbox)
#         self.setWindowTitle('QLabel控件演示')
#         # 设置标题
#
#
#     # 槽有两个方法 1.滑过  2.单击
#     def linkHovered(self):
#         print("当鼠标滑过label2标签时，触发事件")
#
#     def linkClicked(self):
#         print("当鼠标单击label4标签时，触发事件")
#
#   # 防止别的脚本调用，只有自己单独运行，才会调用下面代码
# if __name__ == '__main__':
#
#     # 创建app实例，并传入参数
#     app =  QApplication(sys.argv)
#
#     # 设置图标
#     # app.setWindowIcon(QIcon('images/001.jpg'))
#
#     # 创建对象
#     main = QLabelDemo()
#
#     # 创建窗口
#     main.show()
#
#     # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
#     sys.exit(app.exec_())


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/17 20:01
# @Author : kevin
# @Site :
# @File : 绘制不同类型的直线.py
# @Software: PyCharm
"""
绘制不同类型的直线




"""
# import sys,math
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import Qt
#
# class DrawMultiLine(QWidget):
#     def __init__(self):
#         super(DrawMultiLine, self).__init__()
#         self.resize(400, 300)  # 设置主窗口尺寸
#         self.setWindowTitle('设置Pen的样式')  # 设置主窗口标题
#
#
#
#     def paintEvent(self,event):
#         painter = QPainter()  # 创建对象
#         painter.begin(self)  #
#
#         pen = QPen(Qt.red, 3, Qt.SolidLine)  # 红色，宽度为3像素， 实线____________
#         painter.setPen(pen)  # 设置画笔
#         painter.drawLine(40, 40, 350, 40)  # 40, 40, 350, 40 在resize中，起始横坐标， 起始纵坐标，结束横坐标，结束纵坐标
#         #  -----------------------下面两行可以没有，没有的话就不写字---------------------------------------------
#         painter.setFont(QFont('SimSun', 15))  # 设置字体，字号
#         painter.drawText(40, 20, 320, 20, 100, '这是实线')  #
#         #  ------------------------------------------------------------------------------------------------------
#
#         pen = QPen(Qt.black, 3, Qt.DashLine)  # 黑色，宽度为3像素，虚线——————
#         painter.setPen(pen)  # 设置画笔
#         painter.drawLine(40, 80, 350, 80)  # 40, 80, 350, 80 在resize中，起始横坐标， 起始纵坐标，结束横坐标，结束纵坐标
#         #  -----------------------下面两行可以没有，没有的话就不写字---------------------------------------------
#         painter.setFont(QFont('SimSun', 15))  # 设置字体，字号
#         painter.drawText(40, 40, 320, 40, 100, '这是虚线')  #
#         #  ------------------------------------------------------------------------------------------------------
#
#         pen = QPen(Qt.green, 3, Qt.DashDotLine)  # 绿色，宽度为3像素，点画线—.—.—.
#         painter.setPen(pen)  # 设置画笔
#         painter.drawLine(40, 120, 350, 120)  # 40, 120, 350, 120 在resize中，起始横坐标， 起始纵坐标，结束横坐标，结束纵坐标
#         #  -----------------------下面两行可以没有，没有的话就不写字---------------------------------------------
#         painter.setFont(QFont('SimSun', 15))  # 设置字体，字号
#         painter.drawText(40, 60, 320, 60, 100, '这是点画线')  #
#         #  ------------------------------------------------------------------------------------------------------
#
#         pen = QPen(Qt.blue, 3, Qt.DotLine)  # 蓝色，宽度为3像素，密集虚线 ......
#         painter.setPen(pen)  # 设置画笔
#         painter.drawLine(40, 160, 350, 160)  # 40, 160, 350, 160 在resize中，起始横坐标， 起始纵坐标，结束横坐标，结束纵坐标
#         #  -----------------------下面两行可以没有，没有的话就不写字---------------------------------------------
#         painter.setFont(QFont('SimSun', 15))  # 设置字体，字号
#         painter.drawText(40, 80, 320, 80, 100, '这是密集虚线')  #
#         #  ------------------------------------------------------------------------------------------------------
#
#         pen = QPen(Qt.gray, 3, Qt.DashDotDotLine)  # 灰色，宽度为3像素，点点线 —..—..—
#         painter.setPen(pen)  # 设置画笔
#         painter.drawLine(40, 200, 350, 200)  # 40, 200, 350, 200 在resize中，起始横坐标， 起始纵坐标，结束横坐标，结束纵坐标
#         #  -----------------------下面两行可以没有，没有的话就不写字---------------------------------------------
#         painter.setFont(QFont('SimSun', 15))  # 设置字体，字号
#         painter.drawText(40, 100, 320, 100, 100, '这是点点线')  #
#         #  ------------------------------------------------------------------------------------------------------
#
#         size = self.size()
#         painter.end()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = DrawMultiLine()
#     main.show()
#     sys.exit(app.exec_())
#
#
#
# def paintEvent(self, event):
#     painter = QPainter()
#     painter.begin(self)
#     # 自定义绘制方法
#     self.drawText(event, painter)
#     painter.end()
#
#
# def drawText(self, event, qp):
#     # 设置画笔的颜色
#     qp.setPen(QColor(168, 34, 3))
#     # 设置字体
#     qp.setFont(QFont('SimSun', 20))
#     # 绘制文字
#     qp.drawText(event.rect(), Qt.AlignCenter, self.text)
#
#
# import sys
# from PyQt5.QtWidgets import QApplication,QWidget
# from PyQt5.QtGui import QPainter,QColor,QFont
# from PyQt5.QtCore import Qt
#
# app = QApplication(sys.argv)
# demo=QWidget()
# demo.resize(800,800)
# a=QPainter()
# a.begin(demo)
# a.drawLine(100,100,700,700)
# demo.setWindowTitle('在窗口绘制文字')
# demo.show()
# sys.exit(app.exec_())
#
#
from PyQt5.QtGui import QPen, QColor

"""
绘制不同类型的直线
"""
"""
用像素点绘制正弦曲线

-2PI  2PI
drawPoint(x, y)

# """
# import sys, math
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import Qt
#
# class DrawMultiLine(QWidget):
#     def __init__(self):
#         super(DrawMultiLine, self).__init__()
#         self.resize(300, 300)
#         self.setWindowTitle('设置Pen的样式')
#
#     def paintEvent(self,event):
#         painter = QPainter(self)
#         painter.begin(self)
#
#         #设置画笔的颜色, 字体大小, 线的实心样式
#         pen = QPen(Qt.red, 3, Qt.SolidLine)
#         #设置画笔
#         painter.setPen(pen)
#         #绘制线
#         painter.drawLine(20, 40, 250, 40)
#
#         #设置画笔的虚线样式
#         pen.setStyle(Qt.DashLine)
#         painter.setPen(pen)
#         painter.drawLine(20, 80, 250, 80)
#
#         #设置画笔的虚线和点样式
#         pen.setStyle(Qt.DashDotLine)
#         painter.setPen(pen)
#         painter.drawLine(20, 120, 250, 120)
#
#         #设置画笔的点线样式
#         pen.setStyle(Qt.DotLine)
#         painter.setPen(pen)
#         painter.drawLine(20, 160, 250, 160)
#
#         #设置虚线的点点样式
#         pen.setStyle(Qt.DashDotDotLine)
#         painter.setPen(pen)
#         painter.drawLine(20, 200, 250, 200)
#
#         #设置自定义线
#         pen.setStyle(Qt.CustomDashLine)
#         pen.setDashPattern([1, 10, 5, 4])
#         painter.setPen(pen)
#         painter.drawLine(20, 240, 250, 240)
#
#         painter.end()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     main = DrawMultiLine()
#     main.show()
#
#     sys.exit(app.exec_())



import sys
from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtCore import Qt
from time import sleep as sp
import Qt_class
import random

a=[7,6,8]

class Start_c(QWidget):
    def __init__(self, parent=None):
        super(Start_c,self).__init__()
        self.setObjectName("MainWindow")
        self.resize(2055, 1178)

    def paint(self):
        qp = QtGui.QPainter()
        qp.begin(self)

        # 绘图的方法就写在这里就好，begin与end之间
        self.draw(qp, a)

        qp.end()

    def paintEvent(self,event):
        qp = QtGui.QPainter()
        qp.begin(self)

        # 绘图的方法就写在这里就好，begin与end之间
        self.draw(qp, a)

        qp.end()

    def draw(self, qb, a=[]):
        pen = QPen(QColor(238, 0, 0), 10)
        qb.setPen(pen)  # 对画笔进行设置，QColor参数为颜色的rgb值，后面3为点的大小
        if len(a)== 0 :
            print("Same!")
        else:
            for i in a:
                for j in a:
                    if i!=j:
                        print(i)
                        print(j)
                        qb.drawLine(int(Qt_class.vex[i][0]),int(Qt_class.vex[i][1]),int(Qt_class.vex[j][0]),int(Qt_class.vex[j][1]))
                        print("Ok")



if __name__=="__main__":
    app=QApplication(sys.argv)
    myapp=Start_c()
    myapp.paint()
    myapp.show()
    sys.exit(app.exec_())