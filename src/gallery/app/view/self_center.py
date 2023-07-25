# -*- coding: utf-8 -*-
import sys

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtCore import (QTimer)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QSizePolicy, QSpacerItem, QWidget)
from PySide6.QtWidgets import (QVBoxLayout,
                               QListWidgetItem, QDialog)
from qfluentwidgets import CaptionLabel, PushButton, ListWidget, LineEdit, MessageBox
from qfluentwidgets.window.stacked_widget import StackedWidget

import global_


class Ui_Form2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(654, 475)
        self.layout = QVBoxLayout()
        Form.setLayout(self.layout)
        self.stacked_widget = StackedWidget()
        self.layout.addWidget(self.stacked_widget)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = PushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 80))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        self.pushButton_3.setFont(font)
        self.gridLayout.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 100))
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 2)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)
        self.pushButton = PushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 80))
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.pushButton_2 = PushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 80))
        self.pushButton_2.setFont(font1)
        self.gridLayout.addWidget(self.pushButton_2, 3, 3, 1, 1)
        self.label = CaptionLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 80))
        font2 = QFont()
        font2.setFamilies([u"\u5b8b\u4f53"])
        font2.setPointSize(18)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)
        self.retranslateUi(Form)
        self.page1 = QWidget()
        page1_layout = QVBoxLayout()
        page1_layout.addLayout(self.gridLayout)
        self.page1.setLayout(page1_layout)
        self.stacked_widget.addWidget(self.page1)
        self.page2 = QWidget()
        self.button_back2 = PushButton()
        self.button_back2.setText("返回")
        page2_layout = QVBoxLayout()
        self.list2 = ListWidget()
        page2_layout.addWidget(self.list2)
        page2_layout.addWidget(self.button_back2)
        self.page2.setLayout(page2_layout)
        self.stacked_widget.addWidget(self.page2)
        self.page3 = QWidget()
        self.button_back3 = PushButton()
        self.button_back3.setText("返回")
        page3_layout = QVBoxLayout()
        self.list3 = ListWidget()
        page3_layout.addWidget(self.list3)
        page3_layout.addWidget(self.button_back3)
        self.page3.setLayout(page3_layout)
        self.stacked_widget.addWidget(self.page3)
        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u4e2a\u4eba\u8d44\u6599", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6536\u85cf", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8bc4\u5206", None))
        font = QFont('宋体')
        font.setPointSize(16)  # 设置字号
        self.pushButton_3.setFont(font)
        self.pushButton.setFont(font)
        self.pushButton_2.setFont(font)
    # retranslateUi


class self_manage_center(QWidget, Ui_Form2):
    def __init__(self, name, mother):
        super().__init__()
        self.mother = mother
        self.name = name
        self.setupUi(self)
        self.pushButton.clicked.connect(self.change1)
        self.pushButton_2.clicked.connect(self.change2)
        self.pushButton_3.clicked.connect(self.subshow)
        self.button_back2.clicked.connect(self.change3)
        self.button_back3.clicked.connect(self.change3)
        self.list2.itemClicked.connect(
            lambda item: self.mother.switch_to_food(item.text().split()[0].split('-')[0],
                                                    item.text().split()[0].split('-')[1],
                                                    item.text().split()[0].split('-')[2]))
        self.list3.itemClicked.connect(
            lambda item: self.mother.switch_to_food(item.text().split()[0].split('-')[0],
                                                    item.text().split()[0].split('-')[1],
                                                    item.text().split()[0].split('-')[2]))

    def change1(self):
        self.stacked_widget.setCurrentIndex(1)
        from dbconnect import getstar
        list = getstar(self.name)
        for item in list:
            list_item = QListWidgetItem(item)  # 创建 QListWidgetItem 对象
            list_item.setFont(QFont("SimSun", 15))  # 设置字体为宋体，字号为15
            self.list2.addItem(list_item)  # 将 QListWidgetItem 添加到 QListWidget

    def change2(self):
        self.stacked_widget.setCurrentIndex(2)
        from dbconnect import get_top_scores
        list = get_top_scores(self.name)
        for item in list:
            list_item = QListWidgetItem(item[0] + ' 评分为 ' + str(item[1]))  # 创建 QListWidgetItem 对象
            list_item.setFont(QFont("SimSun", 15))  # 设置字体为宋体，字号为15
            self.list3.addItem(list_item)  # 将 QListWidgetItem 添加到 QListWidget

    def change3(self):
        self.stacked_widget.setCurrentIndex(0)
        self.list2.clear()
        self.list3.clear()

    def subshow(self):
        self.dia = subwind()
        self.dia.exec_()

    def refresh12(self):
        from dbconnect import getuserdata
        self.data = getuserdata(self.name)
        pstr = global_.get_most_frequent(self.data['last'])
        self.label.setText('您好！ ' + self.name + '\n' + '共消费 ' + str(
            self.data['cost']) + '元\n' + '爱吃' + pstr + '类食物\n')


class subwind(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 200)
        self.text_edit1 = LineEdit()
        self.text_edit1.setPlaceholderText("新用户名")
        self.text_edit2 = LineEdit()
        self.text_edit2.setPlaceholderText("旧密码")
        self.text_edit3 = LineEdit()
        self.text_edit3.setPlaceholderText("新密码")
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit1)
        layout.addWidget(self.text_edit2)
        layout.addWidget(self.text_edit3)
        button = PushButton()
        button.setText('保存')
        layout.addWidget(button)
        self.setLayout(layout)
        self.setWindowFlag(Qt.FramelessWindowHint)
        button.clicked.connect(self.store)


    def store(self):
        from dbconnect import getuserdata
        from global_ import name
        data = getuserdata(name)
        if self.text_edit2.text()!=data['password']:
            me = MessageBox('修改失败,原密码错误','' ,self)
            me.cancelButton.hide()
            me.exec_()
            self.close()
        from dbconnect import hasuser
        if self.text_edit1.text()!='' and hasuser(self.text_edit1.text()):
            me = MessageBox('修改失败,该用户名已被他人注册', '', self)
            me.cancelButton.hide()
            me.exec_()
            self.close()
        if self.text_edit3.text() == '':
            me = MessageBox('修改失败,新密码不能为空', '', self)
            me.cancelButton.hide()
            me.exec_()
            self.close()
        from dbconnect import changename, changemi
        from global_ import name
        if self.text_edit1.text() != '':
            changemi(name, self.text_edit3.text())
            changename(name, self.text_edit1.text())
            me = MessageBox('修改成功,请重新登录', '', self)
            me.cancelButton.hide()
            me.exec_()
            self.close()
            QTimer.singleShot(2000, self.close)
            sys.exit()
        else:
            changemi(name, self.text_edit3.text())
            me = MessageBox('修改成功', '', self)
            me.cancelButton.hide()
            me.exec_()
            self.close()




