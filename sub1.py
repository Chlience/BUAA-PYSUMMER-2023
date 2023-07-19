# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerszrWuZ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt, QRectF)
from PySide6.QtGui import (QFont, QPainter, QColor, QPaintEvent, QPen, QBrush)
from PySide6.QtWidgets import (QGridLayout, QLabel, QPushButton,
                               QWidget)


class Ui_Look(QWidget):
    def setupUi(self, Look):
        if not Look.objectName():
            Look.setObjectName(u"Look")
        Look.resize(502, 394)
        self.label = QLabel(Look)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 50, 161, 61))
        font = QFont()
        font.setFamilies([u"\u96b6\u4e66"])
        font.setPointSize(26)
        self.label.setFont(font)
        self.widget = QWidget(Look)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(140, 140, 191, 191))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.display)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_3")
        self.pushButton_4.setText("必吃")
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_3")
        self.pushButton_5.setText("个人")
        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setText("食堂")
        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setText("分类")
        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 1)

    def display(self):
        pass

    def display2(self):
        pass

    # setupUi

    def retranslateUi(self, Look):
        self.label.setText(QCoreApplication.translate("Look", u"\u822a\u5473\u7cfb\u7edf", None))
        self.pushButton.setText(QCoreApplication.translate("Look", u"\u641c\u7d22", None))
        self.pushButton_2.setText(QCoreApplication.translate("Look", u"\u63a8\u8350", None))
        self.pushButton_3.setText("退出")
    # retranslateUi


class sub1(Ui_Look, QWidget):
    def __init__(self, name, par):
        self.parent = par
        self.name = name
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置为无边框窗口
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明
        self.setFixedSize(500, 420)
        self.retranslateUi(self)
        self.pushButton_6.clicked.connect(self.onroad)
        self.pushButton_5.clicked.connect(self.ghew)
        self.pushButton_4.clicked.connect(self.shew)
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.display2)
        self.pushButton_7.clicked.connect(self.display7)
        QMetaObject.connectSlotsByName(self)
        self.setWindowTitle('HangEat')
        self.setStyleSheet("QPushButton {"
                          "border-radius: 10px;"
                          "background-color: white;"
                          "}"
                          "QPushButton:hover {"
                          "background-color: lightGray;"
                          "}")
    def display(self):
        from sub2 import sub2
        self.sub = sub2(self, self.name)
        self.sub.show()
        self.hide()

    def display2(self):
        from sub3 import sub3
        self.sub = sub3(self, self.name)
        self.sub.show()
        self.hide()

    def display7(self):
        from subfenlei import subfen
        self.subfen = subfen(self, self.name)
        self.subfen.show()
        self.hide()

    def shew(self):
        from subbc import subbc
        self.bi = subbc(self.name, self)
        self.bi.show()
        self.hide()

    def onroad(self):
        from onroad import subChi
        self.subChi = subChi(self.name, self)
        self.subChi.show()
        self.hide()
        #self.subChi.set()

    def ghew(self):
        from subzx import subzx
        self.zx = subzx(self.name, self)
        self.zx.show()
        self.hide()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            button = self.focusWidget()  # 获取当前拥有焦点的部件
            if isinstance(button, QPushButton) and button.isEnabled():
                button.click()

    def close(self):
        super().close()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setBrush(QColor("lightblue"))
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        rounded_rect = QRectF(self.rect()).adjusted(1, 1, -1, -1)  # 调整为内部矩形，以防止绘制超出边界
        pen = QPen(Qt.NoPen)  # 创建无边框画笔
        painter.setPen(pen)
        painter.drawRoundedRect(rounded_rect, 10, 10)  # 绘制圆角矩形
