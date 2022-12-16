from Eyetracking_main import *
import Eyetracking_process01
import Eyetracking_process02
import Eyetracking_process03
import Eyetracking_process04
from PyQt5.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()

    child1 = Eyetracking_process01.Ui_Dialog()
    # 通过toolButton将两个窗体关联
    btn1 = window.pushButton
    btn1.clicked.connect(child1.show)

    child2 = Eyetracking_process02.Ui_Dialog()
    # 通过toolButton将两个窗体关联
    btn2 = window.pushButton_2
    btn2.clicked.connect(child2.show)

    # child3 = Eyetracking_process03.Ui_Widget()
    # # 通过toolButton将两个窗体关联
    # btn3 = window.pushButton_3
    # btn3.clicked.connect(child3.show)

    child4 = Eyetracking_process04.ComboxDemo()
    # 通过toolButton将两个窗体关联
    btn4 = window.pushButton_4
    btn4.clicked.connect(child4.show)

    window.show()
    sys.exit(app.exec_())
