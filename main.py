# -*- coding=utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from demo import *

app = QApplication(sys.argv)
window = QMainWindow()
# window.setObjectName("MainWindow")
window.setStyleSheet("#MainWindow{border-image:url(res/xmu_map2.png)}") # 这里使用相对路径，也可以使用绝对路径
ui=Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())

