from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont, QPen, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyle,QLabel


vex=[[260,520,"二期运动场"],       #二期运动场
     [130,880,"信院院楼"],       #信院院楼
     [620,900,"生科院楼"],       #生科院楼
     [920,820,"教学楼群"],       #教学楼群
     [1470,940,"电院院楼"],      #电院院楼
     [890,590,"航院院楼"],       #航院院楼
     [850,320,"体育馆"],       #体育馆
     [960,330,"游泳馆"],       #游泳馆
     [840,80,"新工科大楼"],        #新工科大楼
     [1470,540,"一期运动场"],      #一期运动场
     [1100,650,"小巨蛋"]]       #小巨蛋

spoint=0
epoint=6


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2055, 1178)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.rB=[0 for i in range(11)]
        for i in range(11):
            self.rB[i] = QtWidgets.QRadioButton(self.centralwidget)
            self.rB[i].setGeometry(QtCore.QRect(vex[i][0],vex[i][1], 64, 64))
            self.rB[i].setObjectName("radioButton_"+str(i))
            if i == 0:
                self.rB[i].setChecked(True)
            # self.rB[i].toggled.connected(lambda :self.rbstate(self.rB[i],i) )
            self.rB[i].setStyleSheet("QRadioButton{border-image: url(res/location.png)}")

        self.rB[8].setStyleSheet("QRadioButton{border-image: url(res/RCS.jpg)}")

        self.label1=QLabel(self.centralwidget)
        self.label1.move(1700,250)
        self.label1.resize(500,100)
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.red)
        self.label1.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.yellow)
        self.label1.setPalette(pe)
        self.label1.setFont(QFont("Roman times", 18, QFont.Bold))
        self.label1.setText("起点是："+str(vex[spoint][2]))

        self.label2 = QLabel(self.centralwidget)
        self.label2.move(1700, 650)
        self.label2.resize(500, 100)
        self.label2.setAutoFillBackground(True)
        self.label2.setPalette(pe)
        self.label2.setFont(QFont("Roman times", 18, QFont.Bold))
        self.label2.setText("终点是：" + str(vex[epoint][2]))


        self.spoint=QtWidgets.QPushButton(self.centralwidget)
        self.spoint.setText("将选中的点设为起点")
        self.spoint.resize(200,100)
        self.spoint.move(1800,100)
        self.spoint.setStyleSheet('QPushButton:pressed {background-color:red;}')
        self.spoint.clicked.connect(self.start)

        self.epoint = QtWidgets.QPushButton(self.centralwidget)
        self.epoint.setText("将选中的点设为终点")
        self.epoint.resize(200, 100)
        self.epoint.move(1800, 500)
        self.epoint.setStyleSheet('QPushButton:pressed {background-color:red;}')
        self.epoint.clicked.connect(self.end)

        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setText("开始导航")
        self.start.setFont(QFont("Roman times", 18, QFont.Bold))
        self.start.resize(200, 100)
        self.start.move(1800, 800)
        self.start.setStyleSheet('QPushButton:pressed {background-color:green;}')
        self.start.clicked.connect(self.navigation)

        self.painter = QPainter()  # 创建对象
        self.painter.begin(self.centralwidget)  #
        pen = QPen(Qt.red, 5, Qt.SolidLine)  # 红色，宽度为3像素， 实线____________
        self.painter.setPen(pen)  # 设置画笔
        # self.painter.drawLine(vex[spoint][0], vex[spoint][1], vex[epoint][0],
        #                       vex[epoint][1])  # 40, 40, 350, 40 在resize中，起始横坐标， 起始纵坐标，结束横坐标，结束纵坐标
        self.painter.drawLine(40, 40, 1000,
                              1000)
        self.painter.setFont(QFont('SimSun', 15))  # 设置字体，字号
        self.painter.drawText(40, 20, 320, 20, 100, '这是实线')  #
        self.painter.end()

        MainWindow.setCentralWidget(self.centralwidget)

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

        pass

    # def rbstate(self,btn,i):
    #     if btn.isChecked()== True:
    #         flag=i
    #         print(i)