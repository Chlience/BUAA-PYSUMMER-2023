# -*- coding: utf-8 -*-
import random
import sys

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt, QRectF, QTimer)
from PySide6.QtGui import QPainter, QPaintEvent, QPen, QBrush, QColor, QFont, QIcon
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton,
                               QTextBrowser, QWidget, QApplication)

from submanager import submanger


################################################################################
## Form generated from reading UI file 'testbvWYcu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_Form(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowTitle("登录。。。")
        Form.resize(500, 200)
        Form.setMinimumSize(QSize(500, 200))
        Form.setMaximumSize(QSize(500, 200))
        Form.setStyleSheet(u"QLineEdit{\n"
                           "    border:0px;    #\u53bb\u9664\u8fb9\u6846\n"
                           "    margin:10px; 	#\u8bbe\u7f6e10\u50cf\u7d20\u7684\u5916\u6846\u8ddd\n"
                           "	margin-left:50px;    #\u8bbe\u7f6e\u5de6\u8fb9\u5916\u6846\u8ddd50px\n"
                           "	margin-right:50px;		#\u8bbe\u7f6e\u53f3\u8fb9\u5916\u6846\u8ddd50px\uff0c\u8fd9"
                           "\u6837\u5782\u76f4\u5206\u5e03\u53ef\u4ee5\u5c45\u4e2d\n"
                           "    border-bottom: 2px solid #B3B3B3; 	"
                           "#\u663e\u793a\u4e0b\u6846\u7ebf\uff0c\u4e14\u4e3a2px\u50cf\u7d20\u5bbd\u5ea6\u989c\u8272"
                           "\u4e3a#B3B3B3\n"
                           "    font-family:'黑体'; 	#\u8bbe\u7f6e\u5b57\u4f53\n"
                           "    font-size:20px; 	#\u5b57\u4f53\u5927\u5c0f\n"
                           "    font-weight:bold;		#\u7c97\u4f53\n"
                           "    }")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 60, 54, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 100, 54, 16))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 60, 113, 20))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
                                    "    border:0px;    #\u53bb\u9664\u8fb9\u6846\n"
                                    "    margin:10px; 	#\u8bbe\u7f6e10\u50cf\u7d20\u7684\u5916\u6846\u8ddd\n"
                                    "	margin-left:50px;    #\u8bbe\u7f6e\u5de6\u8fb9\u5916\u6846\u8ddd50px\n"
                                    "	margin-right:50px;		#\u8bbe\u7f6e\u53f3\u8fb9\u5916\u6846\u8ddd50px\uff0c\u8fd9\u6837\u5782\u76f4\u5206\u5e03\u53ef\u4ee5\u5c45\u4e2d\n"
                                    "    border-bottom: 2px solid #B3B3B3; 	#\u663e\u793a\u4e0b\u6846\u7ebf\uff0c\u4e14\u4e3a2px\u50cf\u7d20\u5bbd\u5ea6\u989c\u8272\u4e3a#B3B3B3\n"
                                    "    font-family:'Times Roman'; 	#\u8bbe\u7f6e\u5b57\u4f53\n"
                                    "    font-size:20px; 	#\u5b57\u4f53\u5927\u5c0f\n"
                                    "    font-weight:bold;		#\u7c97\u4f53\n"
                                    "    }")
        self.lineEdit_2 = QLineEdit(Form)

        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 100, 113, 20))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
                                      "    border:0px;    #\u53bb\u9664\u8fb9\u6846\n"
                                      "    margin:10px; 	#\u8bbe\u7f6e10\u50cf\u7d20\u7684\u5916\u6846\u8ddd\n"
                                      "	margin-left:50px;    #\u8bbe\u7f6e\u5de6\u8fb9\u5916\u6846\u8ddd50px\n"
                                      "	margin-right:50px;		#\u8bbe\u7f6e\u53f3\u8fb9\u5916\u6846\u8ddd50px\uff0c\u8fd9\u6837\u5782\u76f4\u5206\u5e03\u53ef\u4ee5\u5c45\u4e2d\n"
                                      "    border-bottom: 2px solid #B3B3B3; 	#\u663e\u793a\u4e0b\u6846\u7ebf\uff0c\u4e14\u4e3a2px\u50cf\u7d20\u5bbd\u5ea6\u989c\u8272\u4e3a#B3B3B3\n"
                                      "    font-family:'Times Roman'; 	#\u8bbe\u7f6e\u5b57\u4f53\n"
                                      "    font-size:20px; 	#\u5b57\u4f53\u5927\u5c0f\n"
                                      "    font-weight:bold;		#\u7c97\u4f53\n"
                                      "    }\n"
                                      "")
        self.lineEdit.returnPressed.connect(self.lineEdit_2.setFocus)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 200, 75, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(170, 200, 75, 24))
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(270, 30, 181, 121))
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 160, 75, 24))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(380, 160, 75, 24))
        self.textBrowser.setStyleSheet("font-family: Times Roman; font-size:17px")
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"exit()", None))

    # retranslateUi


import re


def is_all_chinese(text):
    pattern = "^[\u4e00-\u9fa5]+$"
    return bool(re.match(pattern, text))


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = {}
        self.setWindowTitle('登录器')
        self.subman = submanger()
        self.lineEdit.setText('老王')
        self.lineEdit_2.setText('666666')
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton_3.clicked.connect(self.display)
        self.pushButton_3.setStyleSheet("QPushButton {border-radius: 10px;background-color: white;}")
        self.pushButton_4.setStyleSheet("QPushButton {border-radius: 10px;background-color: white;}")
        self.pushButton_4.clicked.connect(self.close)
        self.lineEdit_2.returnPressed.connect(self.display)
        quotes = [
            "活着就是为了吃饭，难道还有其他原因吗？",
            "勇气不是没有恐惧，而是能够面对恐惧并战胜它。",
            "想象力比知识更重要，因为知识是有限的，而想象力概括着世界的一切。",
            "你不能选择如何开始你的人生，但你可以选择如何结束。",
            "成功的关键在于始终保持积极的态度。",
            "人生不是等待风暴过去，而是学会在雨中跳舞。",
            "不要问别人做了什么，问问自己可以吃什么。",
            "生活中最大的冒险就是决心去追逐自己的梦想。"
        ]
        quote = random.choice(quotes)
        # 在文本浏览器中展示名言警句
        self.textBrowser.setPlainText("      欢迎您使用美食系统😃😃😃😃😃\n      " + quote)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置为无边框窗口
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        rounded_rect = QRectF(self.rect()).adjusted(1, 1, -1, -1)  # 调整为内部矩形，以防止绘制超出边界
        pen = QPen(Qt.NoPen)  # 创建无边框画笔
        painter.setPen(pen)
        brush = QBrush(QColor(173, 216, 230))  # 创建白色画刷
        painter.setBrush(brush)
        painter.drawRoundedRect(rounded_rect, 10, 10)  # 绘制圆角矩形

    def display(self):
        # 利用line Edit控件对象text()函数获取界面输入
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        # 利用text Browser控件对象setText()函数设置界面显示
        from dbconnect import hasuser, getuserdata
        if username == "admin" and password == '123456':
            self.subman.show()
        elif username == 'admin':
            self.textBrowser.setText("你的用户名不正确！")
        elif not is_all_chinese(username):
            self.textBrowser.setText("你必须给自己取一个中文名字！")
        elif len(username) < 2:
            self.textBrowser.setText("用户名太短，建议长一点！")
        elif password == '123456':
            self.textBrowser.setText("密码太简单了吧\U0001F609")
        elif len(password) < 6:
            self.textBrowser.setText("密码不安全，试试其他密码吧！")
        elif hasuser(username):
            data = getuserdata(username)
            print(data['mi'])
            print(password)
            if str(data['mi']) == password:
                self.textBrowser.setText("登录成功!\n" + "用户名是: " + username)
                if username == '老王':
                    self.textBrowser.append("\U0001F613")
                name = username
                from sub1 import sub1
                self.sub1 = sub1(name, self)
                QTimer.singleShot(1200, self.sub1.show)
                QTimer.singleShot(1200, self.close)
            else:
                self.textBrowser.setText("密码错误\U0001F613")
        else:
            self.textBrowser.setText(f"注册成功\U0001F613\n您好！{username}\n密码是 {password}")
            dic = {'name': username, 'mi': password, 'cost': 0.0, 'star': [], 'last': []}
            from dbconnect import zhuce
            zhuce(dic)


if __name__ == '__main__':
    app = QApplication([])
    font = QFont("Times Roman", 12)  # 设置字体为 "Times Roman"，字号为 12
    app.setFont(font)
    icon = QIcon("resources/tupian.ico")
    # 设置应用程序图标
    app.setWindowIcon(icon)
    widget = MyWidget()
    widget.show()
    app.exec()
    sys.exit()
