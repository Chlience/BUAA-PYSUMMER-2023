# -*- coding: utf-8 -*-
###############################################################
## Form generated from reading UI file 'bcdqmvWaV.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QListWidget,
                               QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)

import global1


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 429)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 91, 51))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(28)
        self.label.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 390, 75, 24))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 20, 54, 51))
        pixmap = QPixmap("resources/1.png")  # 用你的图片路径和文件名替换
        width = self.label_4.width()
        height = self.label_4.height()
        # 将图片缩放到和 QLabel 相同的大小
        scaled_pixmap = pixmap.scaled(width, height)
        self.label_4.setPixmap(pixmap)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 40, 113, 261))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(130, 90, 241, 271))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.widget1)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.listView = QListWidget(self.widget1)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_2.addWidget(self.listView)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5fc5\u5403\uff01", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u60a8\u7684\u6536\u85cf\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6821\u957f\u63a8\u8350\uff1a", None))
    # retranslateUi


class subbc(Ui_Form, QWidget):
    def __init__(self, name, parent):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.name = name
        self.setWindowTitle(name + '的必吃')
        self.listWidget.clear()
        self.listView.clear()
        from dbconnect import getstar
        me = getstar(name)
        for entry in me:
            self.listWidget.addItem(entry)
        from dbconnect import findAllFood
        data = findAllFood()
        star_data = [(item, item['times']) for item in data if item["times"] > 0]
        star_data = sorted(star_data, key=lambda x: x[1], reverse=True)
        for i in star_data:
            self.listView.addItem(i[0]['菜名'] + "   被购买" + str(i[1]) + '次\n')

    def closeEvent(self, event):
        self.parent.show()  # 关闭子窗口时显示母窗口
        event.accept()
