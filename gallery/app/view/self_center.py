# -*- coding: utf-8 -*-
import json
import sys

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt, QTimer, Signal)
from PySide6.QtGui import (QColor, QCursor,
                           QFont, QPainter)
from PySide6.QtWidgets import (QLabel, QListWidget, QPlainTextEdit, QPushButton, QVBoxLayout,
                               QWidget, QLineEdit)

import global_


################################################################################
## Form generated from reading UI file 'designerZHCMUq.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(823, 463)
        self.name = None
        self.sub_window = None
        self.mp = QLabel(Form)
        self.mp.setObjectName(u"mp")
        self.mp.setGeometry(QRect(150, 40, 231, 41))
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u5f69\u4e91"])
        font.setPointSize(18)
        font.setBold(False)
        self.mp.setFont(font)
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 190, 141, 251))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 140, 141, 51))
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(370, 160, 111, 301))
        font2 = QFont()
        font2.setFamilies([u"\u65b0\u5b8b\u4f53"])
        font2.setPointSize(12)
        self.verticalLayoutWidget.setFont(font2)
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton_6)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(190, 190, 141, 251))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 140, 141, 51))
        self.label_2.setFont(font1)
        self.label_2.setCursor(QCursor(Qt.WhatsThisCursor))
        self.label_2.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.retranslateUi(Form)
        self.pushButton_5.clicked.connect(self.clearAll)
        self.pushButton_2.clicked.connect(self.clearOne)
        self.pushButton_6.clicked.connect(Form.close)
        self.pushButton_4.clicked.connect(self.mishow)  # mimaxiugai
        self.pushButton_3.clicked.connect(self.mashow)
        QMetaObject.connectSlotsByName(Form)

    def clearAll(self):
        for i in range(self.listWidget.count()):
            text = self.listWidget.item(i).text()
            from dbconnect import changestar
            changestar(self.name, text)
        self.listWidget.clear()

    def clearOne(self):
        from dbconnect import changestar
        changestar(self.name, self.listWidget.currentItem().text())
        self.listWidget.takeItem(self.listWidget.currentRow())

    # setupUi
    def mishow(self):
        if self.sub_window is not None:
            self.sub_window.close()
        self.sub_window = self.SubWindow(self.name)
        self.sub_window.closed.connect(self.handle_child_closed)
        self.sub_window.setFixedSize(300, 100)
        self.sub_window.setWindowFlag(Qt.FramelessWindowHint)
        self.sub_window.show()

    def mashow(self):
        if self.sub_window is not None:
            self.sub_window.close()
        self.sub_window = self.SubWindow(self.name, False)
        self.sub_window.closed.connect(self.handle_child_closed)
        self.sub_window.setFixedSize(300, 100)
        self.sub_window.setWindowFlag(Qt.FramelessWindowHint)
        self.sub_window.show()

    def handle_child_closed(self, info):
        print(self.name)
        self.name = info

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mp.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u6211\u7684\u6536\u85cf", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u4e00\u9879", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u5168\u90e8", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u540d\u5b57", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u4fe1\u606f", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e\u6211\u7684", None))

    # retranslateUi
    class SubWindow(QWidget):
        closed = Signal(str)

        def __init__(self, name, x=True):
            self.x = x
            super().__init__()
            self.layout = QVBoxLayout()
            self.setLayout(self.layout)
            self.name = name
            self.closed = self.closed
            self.text_input = QLineEdit()
            self.layout.addWidget(self.text_input)
            self.exit_button = QPushButton("确定修改")
            self.exit_button.clicked.connect(self.thing)
            self.layout.addWidget(self.exit_button)

        def thing(self):
            txt: str = self.text_input.text()
            if self.x:
                if self.name == '老王':
                    self.text_input.setText("老王作为默认角色不能被修改密码")
                    QTimer.singleShot(2000, self.close)
                    return
                if len(txt) < 6:
                    self.text_input.setText("这个密码安全度不够")
                    return
                if txt == '123456' or global_.has_chinese_characters(txt):
                    self.text_input.setText("这个密码安全度不够")
                    return
                from dbconnect import changemi
                changemi(self.name, txt)
            else:
                from dbconnect import hasuser, changename
                if self.name == '老王':
                    self.text_input.setText("老王作为默认角色不能被修改")
                    QTimer.singleShot(2000, self.close)
                    return
                if hasuser(txt):
                    self.text_input.setText("这个用户名已经被占用了， 重新想一个吧。。")
                    return
                if not global_.is_all_chinese(txt):
                    self.text_input.setText("用户名必须中文，修改失败！")
                    return
                if len(txt) < 2 or len(txt) > 7:
                    self.text_input.setText("用户名太短/长，修改失败！")
                    return
                changename(self.name, txt)
                print(self.name)
                self.text_input.setText("修改成功，请重新登录。")
                QTimer.singleShot(2000, self.close)
                sys.exit()
            self.close()

        def closeEvent(self, event):
            self.closed.emit(self.name)
            print(self.name)
            super().closeEvent(event)


class subzx(Ui_Form, QWidget):
    def __init__(self, name, parent):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.name = name
        self.setWindowTitle('个人中心')

    def refresh12(self):
        from dbconnect import getuserdata
        n = getuserdata(self.name)
        me = n['star']
        pstr = global_.get_most_frequent(n['last'])
        self.plainTextEdit.setPlainText('姓名：' + str(self.name) + '\n' +
                                        '共消费 ' + str(
            n['cost']) + '元\n' + '爱吃' + pstr + '类食物\n')
        self.listWidget.clear()
        self.mp.setText("您好！  " + self.name + '!')
        self.mp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        for entry in me:
            self.listWidget.addItem(entry)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor("lightblue"))
        painter.drawRect(self.rect())
