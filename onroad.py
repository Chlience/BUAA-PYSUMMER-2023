# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '吃PJpsGz.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QLabel, QPushButton, QToolButton, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 500)
        Form.setStyleSheet(u"background: rgb(255, 170, 127)")
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(170, 200, 181, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_0 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_0.setObjectName(u"pushButton")
        self.pushButton_0.setStyleSheet(u"background:rgb(85, 170, 255)")

        self.verticalLayout.addWidget(self.pushButton_0)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background:rgb(85, 255, 0)")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background:rgb(255, 255, 127)")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background:rgb(170, 255, 0)")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background:rgb(170, 255, 255)")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 179, 71))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 20, 151, 121))
        self.label_2.setPixmap(QPixmap(u"resources/chi.png"))
        self.toolButton = QToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(430, 440, 24, 22))
        self.toolButton.setStyleSheet(u"background:rgb(255, 255, 255)")

        self.retranslateUi(Form)
        self.toolButton.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u53bb\u98df\u5802\u7684\u8def\u4e0a", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"\u5b66\u4e8c\u98df\u5802", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5408\u4e00\u98df\u5802", None))
        self.pushButton_5.setText("新北食堂")
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u7f8e\u98df\u82d1", None))
        self.pushButton_4.setText("wings")
        self.label.setText(QCoreApplication.translate("Form",
                                                      u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u4eca\u5929\u53bb\u54ea\u91cc\u5403\uff1f</span></p></body></html>",
                                                      None))
        self.label_2.setText("")
        self.toolButton.setText(QCoreApplication.translate("Form", u"<-", None))
    # retranslateUi


class subChi(QWidget, Ui_Form):
    def __init__(self, name, parent):
        super().__init__()
        self.parent = parent
        self.name = name
        self.setupUi(self)
        self.pushButton_0.clicked.connect(self.open_sub_window_0)
        self.pushButton_3.clicked.connect(self.open_sub_window_3)
        self.pushButton_5.clicked.connect(self.open_sub_window_5)
        self.pushButton_2.clicked.connect(self.open_sub_window_2)
        self.pushButton_4.clicked.connect(self.open_sub_window_4)

    def open_sub_window_0(self):
        from sub2 import sub22
        self.s0 = sub22(self, self.name, 0)
        self.s0.show()

    def open_sub_window_3(self):
        from sub2 import sub22
        self.s3 = sub22(self, self.name, 3)
        self.s3.show()

    def open_sub_window_5(self):
        from sub2 import sub22
        self.s5 = sub22(self, self.name, 5)
        self.s5.show()

    def open_sub_window_2(self):
        from sub2 import sub22
        self.s2 = sub22(self, self.name, 2)
        self.s2.show()

    def open_sub_window_4(self):
        from sub2 import sub22
        self.s4 = sub22(self, self.name, 4)
        self.s4.show()

    def closeEvent(self, event):
        self.parent.show()
        event.accept()

