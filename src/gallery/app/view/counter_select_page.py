# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dangAHAqoO.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt, QItemSelectionModel)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QListWidget, QListWidgetItem,
                               QPushButton, QVBoxLayout, QWidget, QGridLayout, QHBoxLayout)
from qfluentwidgets import ListWidget

from .common_food_page import count_list


class Ui_Form(object):
    def setupUi(self, form, uname):
        if not form.objectName():
            form.setObjectName(u"Form")
        form.resize(735, 682)
        self.uname = uname
        self.layou = QGridLayout()
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(16)
        self.listWidget = ListWidget()
        self.listWidget.setObjectName(u"listWidget")
        lay = QHBoxLayout()
        wid = QWidget()
        wid.setFixedHeight(262)
        lay.addWidget(wid)
        lay.addWidget(self.listWidget)
        self.Widget_2 = count_list(self.uname, [], "未选择", form, self)
        self.Widget_2.setFixedWidth(500)
        self.layou.addLayout(lay, 0, 0, 1, 1)
        self.layou.addWidget(self.Widget_2, 0, 1, 1, 4)
        self.left = ListWidget()
        self.outLayou = QHBoxLayout(form)
        lay = QHBoxLayout()
        wid = QWidget()
        wid.setFixedHeight(262)
        lay.addWidget(wid)
        lay.addWidget(self.left)
        self.outLayou.addLayout(lay)
        self.outLayou.addLayout(self.layou)
        form.setLayout(self.outLayou)
        QMetaObject.connectSlotsByName(form)

    # setupUi


class counter_list_holder(QWidget, Ui_Form):
    def __init__(self, tname, uname, mother):
        super().__init__()
        self.mother = mother
        self.tname = tname
        self.setupUi(self, uname)
        for house_name in {'学二', '合一', '新北', 'wings', '美食苑'}:
            item = QListWidgetItem(house_name)
            item.setFont(QFont('宋体', 12))
            self.left.addItem(item)
        self.setObjectName("选一个想吃的窗口")
        self.data = []
        self.left.itemClicked.connect(
            lambda item: self.load_sub_data(item.text())
        )

    def set_t(self, t):
        for index in range(self.left.count()):
            item = self.left.item(index)
            text = item.text()
            if text == t:
                self.left.setCurrentRow(index, QItemSelectionModel.SelectCurrent)  # 将匹配项设置为当前项
                self.left.itemClicked.emit(item)  # 触发 itemClicked 信号，传递匹配项作为参数

    def switch_to_food(self, food_name, count_name, house_name):
        self.mother.switch_to_food(food_name, count_name, house_name)

    def load_sub_data(self, text):
        from dbconnect import getplacefood
        self.data = getplacefood(text)
        self.listWidget.clear()
        self.Widget_2.clear()
        self.fendang = {}
        for dic in self.data:
            if str(dic["档口"]) not in self.fendang:
                self.fendang[str(dic["档口"])] = []
            self.fendang[str(dic["档口"])].append(dic)
        for item in self.fendang.keys():
            # 创建一个QListWidgetItem对象
            list_item = QListWidgetItem()
            # 设置该项的文本为数组中的元素
            list_item.setText(item)
            list_item.setFont(QFont('宋体', 12))
            # 将该项添加到QListWidget中
            self.listWidget.addItem(list_item)
        self.listWidget.itemClicked.connect(
            lambda item: self.flush(item.text()))

    def flush(self, dang):
        data = self.fendang[str(dang)]
        self.Widget_2.reload(data, dang)
