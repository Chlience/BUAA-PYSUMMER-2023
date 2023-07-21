# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dangAHAqoO.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QListWidget, QListWidgetItem,
                               QPushButton, QVBoxLayout, QWidget, QGridLayout, QHBoxLayout)
from qfluentwidgets import ListWidget

from .common_food_page import count_list


class Ui_Form(object):
    def setupUi(self, Form, uname):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(735, 682)
        self.uname = uname
        self.layou = QGridLayout()
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(16)
        self.listWidget = ListWidget()
        self.listWidget.setFixedWidth(100)
        self.listWidget.setObjectName(u"listWidget")
        self.Widget_2 = count_list(self.uname, [], "未选择")
        self.Widget_2.setFixedWidth(700)
        self.layou.addWidget(self.listWidget, 0, 0, 1, 1)
        self.layou.addWidget(self.Widget_2, 0, 1, 1, 4)
        self.left = ListWidget()
        self.outLayou = QHBoxLayout(Form)
        print(12345)
        self.outLayou.addWidget(self.left)
        self.outLayou.addLayout(self.layou)
        Form.setLayout(self.outLayou)
        QMetaObject.connectSlotsByName(Form)

    # setupUi


class counter_list_holder(QWidget, Ui_Form):
    def __init__(self, tname, uname):
        super().__init__()
        self.tname = tname
        self.setupUi(self, uname)
        for house_name in {'学二', '合一', '新北', 'wings', '美食苑'}:
            self.left.addItem(house_name)
            print('y')
        self.setObjectName("选一个想吃的窗口")
        self.data = []
        self.left.itemClicked.connect(
            lambda item: self.load_sub_data(item.text())
        )

    def load_sub_data(self, text):
        from dbconnect import getplacefood
        self.data = getplacefood(text)
        self.listWidget.clear()
        fendang = {}
        for dic in self.data:
            if str(dic["档口"]) not in fendang:
                fendang[str(dic["档口"])] = []
            fendang[str(dic["档口"])].append(dic)
        print('fendang='+str(fendang))
        for item in fendang.keys():
            # 创建一个QListWidgetItem对象
            list_item = QListWidgetItem()
            # 设置该项的文本为数组中的元素
            list_item.setText(item)
            # 将该项添加到QListWidget中
            self.listWidget.addItem(list_item)
        self.listWidget.itemClicked.connect(
            lambda item: self.flush(fendang[str(item.text())], item.text()))

    def flush(self, data, dang):
        self.Widget_2.reload(data, dang)
