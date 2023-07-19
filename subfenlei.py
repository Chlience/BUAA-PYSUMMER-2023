# -*- coding: utf-8 -*-
import random

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt, QRectF)
from PySide6.QtGui import (QBrush, QColor, QFont, QPainter,
                           QPaintEvent, QPen)
from PySide6.QtWidgets import (QGridLayout, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QWidget)


################################################################################
## Form generated from reading UI file 'fenleiFrevpR.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(553, 646)
        Form.setStyleSheet(u"QPushButton { border-radius: 10px; width: 200px;font-weight: bold;"
                           "height: 50px;font-size: 15px; font-family: '华文宋体'; background-color: rgb(170, 170, 255); }\n"
                           )
        Form.setWindowTitle("还没想好？看看各种分类")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(110, 80, 331, 371))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 6, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 8, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 9, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 6, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 10, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 4, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 6, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 10, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 7, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 8, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 6, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 8, 4, 1, 1)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 10, 4, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 4, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 3, 0, 1, 1)

        self.pushButton_13 = QPushButton(Form)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(370, 520, 75, 24))
        self.pushButton_14 = QPushButton(Form)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(110, 520, 75, 24))

        self.retranslateUi(Form)
        self.pushButton_13.clicked.connect(Form.close)
        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5206\u7c7b", None))
        self.pushButton.setText("主食")
        self.pushButton_2.setText("西餐")
        self.pushButton_3.setText("蛋类")
        self.pushButton_4.setText("猪肉")
        self.pushButton_5.setText("蔬菜")
        self.pushButton_6.setText("牛肉")
        self.pushButton_7.setText("豆类")
        self.pushButton_8.setText("鸡肉")
        self.pushButton_9.setText("鱼肉")
        self.pushButton_10.setText("饮料")
        self.pushButton_11.setText("咖啡")
        self.pushButton_12.setText("甜品")
        self.pushButton_13.setText("返回")
        self.pushButton_14.setText("随机")


from sub2 import sub23


class subfen(QWidget, Ui_Form):
    def __init__(self, parent, username):
        super().__init__()
        self.user = username
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置为无边框窗口
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        self.arr = {7: "豆类", 5: "蔬菜", 1: "主食", 8: "鸡肉", 4: "猪肉", 3: "蛋类", 9: "鱼肉", 6: "牛肉",
                    2: "西餐", 10: "饮料", 11: "咖啡", 14: "随机", 13: '牛肉', 12: '甜品'}
        self.pushButton.clicked.connect(self.show1)
        self.pushButton_2.clicked.connect(self.show2)
        self.pushButton_3.clicked.connect(self.show3)
        self.pushButton_4.clicked.connect(self.show4)
        self.pushButton_5.clicked.connect(self.show5)
        self.pushButton_6.clicked.connect(self.show6)
        self.pushButton_7.clicked.connect(self.show7)
        self.pushButton_8.clicked.connect(self.show8)
        self.pushButton_9.clicked.connect(self.show9)
        self.pushButton_10.clicked.connect(self.show10)
        self.pushButton_11.clicked.connect(self.show11)
        self.pushButton_12.clicked.connect(self.show12)
        self.pushButton_14.clicked.connect(self.show14)

    def show1(self):
        self.sub1 = sub23(self, self.user, self.arr[1])
        self.hide()  # 隐藏母窗口
        self.sub1.show()

    def show2(self):
        self.sub2 = sub23(self, self.user, self.arr[2])
        self.hide()
        self.sub2.show()

    def show3(self):
        self.sub3 = sub23(self, self.user, self.arr[3])
        self.hide()
        self.sub3.show()

    def show4(self):
        self.sub4 = sub23(self, self.user, self.arr[4])
        self.hide()
        self.sub4.show()

    def show5(self):
        self.sub5 = sub23(self, self.user, self.arr[5])
        self.hide()
        self.sub5.show()

    def show6(self):
        self.sub6 = sub23(self, self.user, self.arr[6])
        self.hide()
        self.sub6.show()

    def show7(self):
        self.sub7 = sub23(self, self.user, self.arr[7])
        self.hide()
        self.sub7.show()

    def show8(self):
        self.sub8 = sub23(self, self.user, self.arr[8])
        self.hide()
        self.sub8.show()

    def show9(self):
        self.sub9 = sub23(self, self.user, self.arr[9])
        self.hide()
        self.sub9.show()

    def show10(self):
        self.sub10 = sub23(self, self.user, self.arr[10])
        self.hide()
        self.sub10.show()

    def show11(self):
        self.sub11 = sub23(self, self.user, self.arr[11])
        self.hide()
        self.sub11.show()

    def show12(self):
        self.sub12 = sub23(self, self.user, self.arr[12])
        self.hide()
        self.sub12.show()

    def show13(self):
        self.sub13 = sub23(self, self.user, self.arr[13])
        self.hide()
        self.sub13.show()

    def show14(self):
        self.hide()
        show_functions = []
        for i in range(1, 14):
            show_func = getattr(self, f"show{i}")
            show_functions.append(show_func)
        random_show_func = random.choice(show_functions)
        random_show_func()

    def close(self):
        super().close()
        self.parent.show()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        rounded_rect = QRectF(self.rect()).adjusted(1, 1, -1, -1)  # 调整为内部矩形，以防止绘制超出边界
        pen = QPen(Qt.NoPen)  # 创建无边框画笔
        painter.setPen(pen)
        brush = QBrush(QColor(255, 192, 203))  # 创建白色画刷
        painter.setBrush(brush)
        painter.drawRoundedRect(rounded_rect, 10, 10)  # 绘制圆角矩形
