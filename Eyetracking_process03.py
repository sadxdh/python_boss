import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QFont
import b站搜索索引


class Ui_Widget(QWidget):

    def __init__(self, parent=None):
        super(Ui_Widget, self).__init__(parent)
        # 设置窗口的位置和大小
        self.setGeometry(220, 60, 1430, 760)
        # 设置窗口的标题
        self.setWindowTitle('b站搜索')
        # pix = QPixmap('1.webp')
        self.b_data = b站搜索索引.B_spider('大学生职业规划')

        self.le1 = QLabel(self)
        self.le1.setGeometry(640, 100, 200, 40)
        self.le1.setObjectName('le1')
        self.le1.setText('大学生职业规划')
        self.le1.setFont(QFont("Roman times", 20, QFont.Bold))

        self.urls = [u[0] for u in self.b_data]
        self.pics = [QPixmap(p[1]) for p in self.b_data]
        self.titles = [t[2] for t in self.b_data]

        lb = QLabel(self)
        lb.setGeometry(130, 250, 191, 141)
        lb.setStyleSheet("border: 2px solid red")
        lb.setPixmap(QPixmap(self.pics[0]))
        lb.setScaledContents(True)
        lb1 = QLabel(self)
        lb1.setGeometry(130, 380, 191, 70)
        lb1.setObjectName('lb1')
        lb1.setOpenExternalLinks(True)  # 允许访问超链接
        lb1.setText(f"<a href={self.urls[0]} >{self.titles[0]}</a>")
        lb1.setWordWrap(True)

        lb_2 = QLabel(self)
        lb_2.setGeometry(390, 250, 191, 141)
        lb_2.setStyleSheet("border: 2px solid red")
        lb_2.setPixmap(self.pics[1])
        lb_2.setScaledContents(True)
        lb2 = QLabel(self)
        lb2.setGeometry(390, 380, 191, 70)
        lb2.setObjectName('lb1')
        lb2.setOpenExternalLinks(True)  # 允许访问超链接
        lb2.setText(f"<a href={self.urls[1]} >{self.titles[1]}</a>")
        lb2.setWordWrap(True)

        lb_3 = QLabel(self)
        lb_3.setGeometry(650, 250, 191, 141)
        lb_3.setStyleSheet("border: 2px solid red")
        lb_3.setPixmap(self.pics[2])
        lb_3.setScaledContents(True)
        lb3 = QLabel(self)
        lb3.setGeometry(650, 380, 191, 70)
        lb3.setObjectName('lb1')
        lb3.setOpenExternalLinks(True)  # 允许访问超链接
        lb3.setText(f"<a href={self.urls[2]} >{self.titles[2]}</a>")
        lb3.setWordWrap(True)

        lb_4 = QLabel(self)
        lb_4.setGeometry(910, 250, 191, 141)
        lb_4.setStyleSheet("border: 2px solid red")
        lb_4.setPixmap(self.pics[3])
        lb_4.setScaledContents(True)
        lb4 = QLabel(self)
        lb4.setGeometry(910, 380, 191, 70)
        lb4.setObjectName('lb1')
        lb4.setOpenExternalLinks(True)  # 允许访问超链接
        lb4.setText(f"<a href={self.urls[3]} >{self.titles[3]}</a>")
        lb4.setWordWrap(True)

        lb_5 = QLabel(self)
        lb_5.setGeometry(1170, 250, 191, 141)
        lb_5.setStyleSheet("border: 2px solid red")
        lb_5.setPixmap(self.pics[4])
        lb_5.setScaledContents(True)
        lb5 = QLabel(self)
        lb5.setGeometry(1170, 380, 191, 70)
        lb5.setObjectName('lb1')
        lb5.setOpenExternalLinks(True)  # 允许访问超链接
        lb5.setText(f"<a href={self.urls[4]} >{self.titles[4]}</a>")
        lb5.setWordWrap(True)

        lb_6 = QLabel(self)
        lb_6.setGeometry(130, 520, 191, 141)
        lb_6.setStyleSheet("border: 2px solid red")
        lb_6.setPixmap(self.pics[5])
        lb_6.setScaledContents(True)
        lb6 = QLabel(self)
        lb6.setGeometry(130, 650, 191, 70)
        lb6.setObjectName('lb1')
        lb6.setOpenExternalLinks(True)  # 允许访问超链接
        lb6.setText(f"<a href={self.urls[5]} >{self.titles[5]}</a>")
        lb6.setWordWrap(True)

        lb_7 = QLabel(self)
        lb_7.setGeometry(390, 520, 191, 141)
        lb_7.setStyleSheet("border: 2px solid red")
        lb_7.setPixmap(self.pics[6])
        lb_7.setScaledContents(True)
        lb7 = QLabel(self)
        lb7.setGeometry(390, 650, 191, 70)
        lb7.setObjectName('lb1')
        lb7.setOpenExternalLinks(True)  # 允许访问超链接
        lb7.setText(f"<a href={self.urls[6]} >{self.titles[6]}</a>")
        lb7.setWordWrap(True)

        lb_8 = QLabel(self)
        lb_8.setGeometry(650, 520, 191, 141)
        lb_8.setStyleSheet("border: 2px solid red")
        lb_8.setPixmap(self.pics[7])
        lb_8.setScaledContents(True)
        lb8 = QLabel(self)
        lb8.setGeometry(650, 650, 191, 70)
        lb8.setObjectName('lb1')
        lb8.setOpenExternalLinks(True)  # 允许访问超链接
        lb8.setText(f"<a href={self.urls[7]} >{self.titles[7]}</a>")
        lb8.setWordWrap(True)

        lb_9 = QLabel(self)
        lb_9.setGeometry(910, 520, 191, 141)
        lb_9.setStyleSheet("border: 2px solid red")
        lb_9.setPixmap(self.pics[8])
        lb_9.setScaledContents(True)
        lb9 = QLabel(self)
        lb9.setGeometry(910, 650, 191, 70)
        lb9.setObjectName('lb1')
        lb9.setOpenExternalLinks(True)  # 允许访问超链接
        lb9.setText(f"<a href={self.urls[8]} >{self.titles[8]}</a>")
        lb9.setWordWrap(True)

        lb_10 = QLabel(self)
        lb_10.setGeometry(1170, 520, 191, 141)
        lb_10.setStyleSheet("border: 2px solid red")
        lb_10.setPixmap(self.pics[9])
        lb_10.setScaledContents(True)
        lb10 = QLabel(self)
        lb10.setGeometry(1170, 650, 191, 70)
        lb10.setObjectName('lb1')
        lb10.setOpenExternalLinks(True)  # 允许访问超链接
        lb10.setText(f"<a href={self.urls[9]} >{self.titles[9]}</a>")
        lb10.setWordWrap(True)

    def b_spider(self):
        self.b_data = b站搜索索引.B_spider(self.le1.text())


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Ui_Widget()
    ex.show()
    sys.exit(app.exec_())
