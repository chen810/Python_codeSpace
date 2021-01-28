# from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication([])  # 建立应用
    wo = QWidget()  # 建立窗口
    wo.show()  # 显示窗口
    sys.exit(app.exec_())
