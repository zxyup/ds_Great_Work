
# -*- coding=utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from demo import *
# from demoo import *

count=0


class ds_GA(QMainWindow):
    def __init__(self,parent=None):
        super(ds_GA,self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(2055, 1178)
        centralwidget = QtWidgets.QWidget(self)
        self.setWindowTitle("ds_ai_GA")
        centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(centralwidget)

    def paintEvent(self,event):
        qp = QtGui.QPainter()
        qp.begin(self)

        # 绘图的方法就写在这里就好，begin与end之间
        self.draw(qp, a)

        qp.end()

    def draw(self, qb, a=[]):
        global count
        print(count)
        if count>80:
            a[0]=2
            a[1]=9
            a[2]=5
        count+=1
        pen = QPen(QColor(238, 0, 0), 10)
        qb.setPen(pen)  # 对画笔进行设置，QColor参数为颜色的rgb值，后面3为点的大小
        if len(a)== 0 :
            print("Same!")
        else:
            for i in a:
                for j in a:
                    if i!=j:
                        print(a)
                        # print(i)
                        # print(j)
                        qb.drawLine(int(vex[i][0]),int(vex[i][1]),int(vex[j][0]),int(vex[j][1]))
                        # print("Ok")
        print("updated!")


app = QApplication(sys.argv)
# window=QMainWindow()
window = ds_GA()
window.setStyleSheet("#MainWindow{border-image:url(res/xmu_map2.png)}") # 这里使用相对路径，也可以使用绝对路径
# ui=Ui_MainWindow()
# ui.setupUi(window)
# ui.draw(window,a)
window.show()
sys.exit(app.exec_())

# app = QApplication(sys.argv)
# form  = ds_GA()
# form.show()
# sys.exit(app.exec_())

##========================================================
# -*- coding: utf-8 -*-

# import sys
# from PyQt5.QtWidgets import  QMainWindow, QApplication
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
#     def __init__(self, parent = None):
#         super(MainWindow,self).__init__(parent)
#         self.resize(400,200)
#         # self.status = self.statusBar()
#         # self.status.showMessage("这是状态栏提示",5000)
#         # self.setWindowTitle("PyQt MainWindow 例子")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     # app.setWindowIcon(QIcon("./images/cartoon1.ico"))
#     form  = MainWindow()
#     form.show()
#     sys.exit(app.exec_())