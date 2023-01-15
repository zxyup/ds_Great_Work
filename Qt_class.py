from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont, QPen, QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyle,QLabel,QWidget,QMainWindow,QSizePolicy
from path_planning import dijk,arc

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
     [1100,650,"小巨蛋"],           #小巨蛋
     [520,420,"三期站台"],          #三期站台
     [1250,420,"一期站台"],         #一期站台
     [1350,790,"能源学院"],         #能源学院
     [940,1040,"南大门"],           #南大门
     [650,520,"动物中心"],          #动物中心
     [1565,680,"东门"],             #东门
     [450,585,"二期站台"]]           #二期站台

spoint=0
epoint=6
a=[]



seed=[i for i in range(len(vex))] 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global spoint,epoint
        print(type(MainWindow))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2055, 1178)
        MainWindow.setFixedSize(2055,1178)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rB=[0 for i in range(len(vex))]
        for i in range(len(vex)):
            self.rB[i] = QtWidgets.QRadioButton(self.centralwidget)
            self.rB[i].setGeometry(QtCore.QRect(vex[i][0],vex[i][1], 64, 64))
            self.rB[i].setObjectName("radioButton_"+str(i))
            # self.rB[i].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            if i == 0:
                self.rB[i].setChecked(True)
            self.rB[i].setStyleSheet("QRadioButton{border-image: url(res/location.png)}")

        self.rB[8].setStyleSheet("QRadioButton{border-image: url(res/rcs.png)}")

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
        self.start.clicked.connect(MainWindow.navigation)


        MainWindow.setCentralWidget(self.centralwidget)

    def start(self):
        global spoint
        for i in range(len(vex)):
            if self.rB[i].isChecked() == True:
                spoint=i
                print(vex[i][2])
                print("spoint="+str(spoint))
                self.label1.setText("起点是：" + str(vex[spoint][2]))
                break
    def end(self):
        global epoint
        for i in range(len(vex)):
            if self.rB[i].isChecked() == True:
                epoint=i
                print(vex[i][2])
                print("epoint="+str(epoint))
                self.label2.setText("终点是：" + str(vex[epoint][2]))
                break

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

        # 绘图的方法就写在这里，begin与end之间
        self.draw(qp, a)

        qp.end()

    def draw(self, qb, a=[]):
        pen = QPen(QColor(238, 0, 0), 10)
        qb.setPen(pen)  # 对画笔进行设置，QColor参数为颜色的rgb值，后面10为点的大小
        if len(a)== 0 :
            print("Same!")
        else:
            for i in range(len(a)-1):
                if a[i]!=-1:
                        qb.drawLine(vex[a[i]][0]+32,vex[a[i]][1]+64,vex[a[i+1]][0]+32,vex[a[i+1]][1]+64)

    
    def navigation(self):
        global a
        b=dijk(arc,spoint,epoint)
        si=0
        ei=b.index(epoint)
        for i in range(len(b)):
            if b[i]==b[0]:
                si=i
        a.clear()
        a.append(spoint)
        print(si)
        print(ei)
        while ei <= si:
            ei=len(b)
            print(ei)
        a=a+b[si:ei+1]
        for i in a:
            if a.count(i) >= 2:
                s=i
                ii=a.index(i)
                for j in range(len(a)):
                    if j>=ii:
                        a[j]=-1
                        if a[j+1] == s:
                            break
        while a.count(-1)!=0:
            a.remove(-1)                        
        print(a)
        # a=random.sample(seed,5)
        # print(a)
        print("Clicked")
        QWidget.repaint(self)
        dijk(arc,spoint,epoint)
