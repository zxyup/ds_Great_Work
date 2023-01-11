
# -*- coding=utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from Qt_class import *
import random

count=0

seed=[0,1,2,3,4,5,6,7,8,9,10]


class ds_GA(QMainWindow):
    def __init__(self,parent=None):
        super(ds_GA,self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(2055, 1178)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setWindowTitle("ds_ai_GA")
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        ui=Ui_MainWindow()
        ui.setupUi(self)

    def paintEvent(self,event):
        qp = QtGui.QPainter()
        qp.begin(self)

        # 绘图的方法就写在这里就好，begin与end之间
        self.draw(qp, a)

        qp.end()

    def draw(self, qb, a=[]):
        global count
        # print(count)
        count+=1
        pen = QPen(QColor(238, 0, 0), 10)
        qb.setPen(pen)  # 对画笔进行设置，QColor参数为颜色的rgb值，后面10为点的大小
        if len(a)== 0 :
            print("Same!")
        else:
            for i in range(len(a)-1):
                        # print("i="+str(i))
                        # print("j="+str(j))
                        # print("a[i]="+str(a[i]))
                        # print("a[j]="+str(a[j]))
                        qb.drawLine(vex[a[i]][0]+32,vex[a[i]][1]+64,vex[a[i+1]][0]+32,vex[a[i+1]][1]+64)
                        # print("Ok")
        print("updated!")

    
    
    def start(self):
            for i in range(11):
                if self.rB[i].isChecked() == True:
                    spoint=i
                    print(vex[i][2])
                    self.label1.setText("起点是：" + str(vex[spoint][2]))
                    break
    def end(self):
        for i in range(11):
            if self.rB[i].isChecked() == True:
                epoint=i
                print(vex[i][2])
                self.label2.setText("终点是：" + str(vex[epoint][2]))
                break
            
    def navigation(self):
        global a
        a=random.sample(seed,5)
        print(a)
        print("Clicked")
        QWidget.repaint(self)


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./res/GPS.ico"))
window = ds_GA()
window.setStyleSheet("#MainWindow{border-image:url(res/xmu_map2.png)}") # 这里使用相对路径，也可以使用绝对路径
ui=Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())