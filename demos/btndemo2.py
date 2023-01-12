import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QToolButton, QStyle


class DemoIcon(QWidget):
    def __init__(self, parent=None):
        super(DemoIcon, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle('实战PyQt5: 内置图标演示')

        self.initUi()

    def initUi(self):
        layout = QGridLayout()

        line_count = 16  # 每一行的显示个数
        index = 0

        # 根据Qt的枚举变量来显示图标
        for key in dir(QStyle):
            value = getattr(QStyle, key)
            if isinstance(value, QStyle.StandardPixmap):
                if key != 'SP_CustomBase' and value < 71:
                    print(key, value)
                    btn = QToolButton()
                    btn.setFixedSize(32, 32)
                    btn.setIcon(QApplication.style().standardIcon(value))
                    btn.setToolTip('{0}: {1}'.format(key, value))
                    layout.addWidget(btn, index // line_count, index % line_count)
                    index += 1

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoIcon()
    window.show()
    sys.exit(app.exec())