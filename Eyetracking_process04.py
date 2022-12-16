import sys
from PyQt5.QtWidgets import *
import 政策索引


class ComboxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboxDemo, self).__init__(parent)
        self.q = 政策索引.Ui_Form()
        self.titles = [t[1] for t in self.q.query()]
        self.hrefs = [t[0] for t in self.q.query()]
        self.i = '0'
        # 设置标题
        self.setWindowTitle('政策文件对应地址查询')
        self.move(500, 500)
        # 设置初始界面大小
        self.resize(500, 150)

        # 垂直布局
        layout = QVBoxLayout()
        # 创建标签，默认空白
        self.btn1 = QLabel(self.hrefs[0])

        # 实例化QComBox对象
        self.cb = QComboBox()
        self.cb.addItems(self.titles)
        # 当下拉索引发生改变时发射信号触发绑定的事件
        self.cb.currentIndexChanged.connect(self.selectionchange)

        # 控件添加到布局中，设置布局
        layout.addWidget(self.cb)
        layout.addWidget(self.btn1)
        self.setLayout(layout)

    def selectionchange(self, i):
        print('current index', i, 'selection changed', self.cb.currentText(), 'text url', self.hrefs[i])
        self.btn1.setText(self.hrefs[i])
        self.q.openurl(self.hrefs[i])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = ComboxDemo()
    comboxDemo.show()
    sys.exit(app.exec_())
