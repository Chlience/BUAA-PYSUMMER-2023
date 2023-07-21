# -*- coding: utf-8 -*-
###############################################################
## Form generated from reading UI file 'bcdqmvWaV.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QGridLayout, QLabel, QSizePolicy, QSpacerItem, QWidget, QStyledItemDelegate,
                               QListWidgetItem)
from qfluentwidgets import ListWidget, LargeTitleLabel


# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'untitledSQZDdy.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'untitledixDXZO.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(795, 680)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(160, 140, 511, 401))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget_2 = ListWidget(self.gridLayoutWidget)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.gridLayout.addWidget(self.listWidget_2, 3, 1, 1, 1)

        self.label = LargeTitleLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.listWidget = ListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777214, 16777215))

        self.gridLayout.addWidget(self.listWidget, 0, 1, 1, 1)

        self.label_2 = LargeTitleLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6211\u7684\u6536\u85cf  ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u70ed\u5ea6\u6700\u9ad8  ", None))
    # retranslateUi



class must_eat_form(Ui_Form, QWidget):

    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
        font = QFont("宋体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.name = name
        self.setWindowTitle(name + '的必吃')
        self.listWidget.clear()
        self.listWidget_2.clear()
        from dbconnect import getstar
        me = getstar(name)
        for entry in me:
            lm = QListWidgetItem(entry)
            lm.setFont("黑体")
            self.listWidget.addItem(lm)
        from dbconnect import findAllFood
        data = findAllFood()
        star_data = [(item, item['times']) for item in data if item["times"] > 0]
        star_data = sorted(star_data, key=lambda x: x[1], reverse=True)
        for i in star_data:
            lm = QListWidgetItem(i[0]['菜名'] + "   被购买" + str(i[1]) + '次\n')
            lm.setFont("黑体")
            self.listWidget_2.addItem(lm)




