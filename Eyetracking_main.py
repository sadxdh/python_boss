from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
import os


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.sel_spider()
        # self.data_handle()
        # self.policy_spider()
        self.setupUi(self)
        self.retranslateUi(self)
        self.yiyan()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 80, 351, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 196, 351, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 313, 351, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 430, 351, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(QtCore.QRect(10, 540, 561, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "boss直聘求职辅助工具"))
        self.pushButton.setText(_translate("MainWindow", "职位查询"))
        self.pushButton_2.setText(_translate("MainWindow", "职位数据可视化"))
        self.pushButton_3.setText(_translate("MainWindow", "就业辅导"))
        self.pushButton_4.setText(_translate("MainWindow", "政策指导"))
        self.label.setText(_translate("MainWindow", "好运总会照顾低头努力的人！"))

    def data_handle(self):
        os.system("python E:\BaiduSyncdisk\Python\学校作业\python大作业boss\职位可视化代码.py")

    def sel_spider(self):
        os.system("python E:\BaiduSyncdisk\Python\学校作业\python大作业boss\直聘.py")

    def yiyan(self):
        import requests
        resp = requests.get('https://v1.hitokoto.cn/?encode=json&c=k&c=i&c=d')
        json_data = resp.json()
        hitokoto = json_data['hitokoto']
        _from = json_data['from']
        creator = json_data['creator']
        self.label.setText(f"******{hitokoto}******")

    def policy_spider(self):
        os.system("python E:\BaiduSyncdisk\Python\学校作业\python大作业boss\政策指导爬虫.py")
