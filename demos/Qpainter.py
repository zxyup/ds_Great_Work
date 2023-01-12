# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
import sys
import random

a=[0,1,2,3]


class ExcelWindow(QWidget):
    def __init__(self):
        super(ExcelWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(200, 200)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawPoint(random.randint(0, 199), random.randint(0, 199))
        # 绘图的方法就写在这里就好，begin与end之间
        self.drewDot(qp,a)

        qp.end()
    def drewDot(self, qp,a=[]):
        pen = QPen(QColor(238, 0, 0), 3)
        qp.setPen(pen)  # 对画笔进行设置，QColor参数为颜色的rgb值，后面3为点的大小
        print(self.size())  # 确认下能画画的画布像素范围
        # 随机画几个点
        for i in a:
            # drawPoint的参数有两个，一个是点的横坐标，一个是点的纵坐标
            qp.drawPoint(random.randint(0, 199), random.randint(0, 199))


def main():
    app = QApplication(sys.argv)
    gui = ExcelWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()