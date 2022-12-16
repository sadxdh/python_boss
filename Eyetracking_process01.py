# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Eyetracking_process01.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import pprint
import time
import pymysql
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog
from selenium import webdriver


class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(844, 520)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 411, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 90, 421, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 130, 421, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 170, 421, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 210, 421, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 250, 421, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 90, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 130, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 170, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(140, 210, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 250, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(140, 290, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(140, 350, 54, 12))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(140, 410, 54, 12))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(570, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(240, 290, 421, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(240, 350, 421, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(240, 410, 421, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 450, 201, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.query)
        self.pushButton_2.clicked.connect(self.open_url)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "职位查询"))
        self.lineEdit.setText(_translate("Dialog", ""))
        self.label.setText(_translate("Dialog", "职位名"))
        self.label_2.setText(_translate("Dialog", "地址"))
        self.label_3.setText(_translate("Dialog", "薪资"))
        self.label_4.setText(_translate("Dialog", "工作经验"))
        self.label_5.setText(_translate("Dialog", "公司名"))
        self.label_6.setText(_translate("Dialog", "职位信息"))
        self.label_7.setText(_translate("Dialog", "公司福利"))
        self.label_8.setText(_translate("Dialog", "招聘链接"))
        self.pushButton.setText(_translate("Dialog", "查询"))
        self.lineEdit_9.setText(_translate("Dialog", "http://www.baidu.com"))
        self.pushButton_2.setText(_translate("Dialog", "点击查看详情页面"))

    def query(self):
        # 1. 连接数据库，
        conn = pymysql.connect(
            host='192.168.96.128',
            user='root',
            password='123456',
            db='boss',
            charset='utf8',
            # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
        )
        # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
        # 2. 创建游标对象，
        cur = conn.cursor()
        # 4). **************************数据库查询*****************************
        sqli = f"select * from boss where job_name = '{self.lineEdit.text()}';"
        result = cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
        # print("默认不返回查询结果集， 返回数据记录数：", result)
        info = list(cur.fetchall())  # 3). 获取所有的查询结果
        # print("获取所有的查询结果：")
        pprint.pprint(info)
        # print("获取所有的查询结果长度：", len(info))
        # print("返回执行sql语句影响的行数：", cur.rowcount)  # 4). 返回执行sql语句影响的行数
        # 4. 关闭游标
        cur.close()
        # 5. 关闭连接
        conn.close()

        self.lineEdit_2.setText(info[0][0])
        self.lineEdit_3.setText(info[0][1])
        self.lineEdit_4.setText(info[0][2])
        self.lineEdit_5.setText(info[0][3])
        self.lineEdit_6.setText(info[0][4])
        self.lineEdit_7.setText(info[0][5])
        self.lineEdit_8.setText(info[0][6])
        self.lineEdit_9.setText(info[0][7])

    def open_url(self):
        driver = webdriver.Chrome()
        driver.get(self.lineEdit_9.text())
        driver.set_window_size(1250, 900)
        time.sleep(15)
        driver.close()