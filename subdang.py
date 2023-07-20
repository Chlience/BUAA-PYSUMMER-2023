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
                               QPushButton, QVBoxLayout, QWidget, QGridLayout)

from sub2 import sub24


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(735, 682)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")

        self.layou = QGridLayout(Form)
        self.verticalLayout = QVBoxLayout()
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.layou.addLayout(self.verticalLayout, 0,0,1,1)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("分档窗口")
        self.label.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6863\u53e3", None))
        self.pushButton.setText("举报")
        self.pushButton_2.setText("返回")

    # retranslateUi


class subdang(QWidget, Ui_Form):
    def __init__(self, parent, tname, uname, dataspe):
        super().__init__()
        self.setupUi(self)
        self.Widget_2 = sub24(uname, [], "未选择")
        self.layou.addWidget(self.Widget_2,0,1,1,4)
        self.layou.setColumnStretch(1, 5)
        self.setLayout(self.layou)
        self.tname = tname
        self.parent = parent
        self.uname = uname
        self.setObjectName("选一个想吃的窗口")
        self.data = dataspe
        self.pushButton_2.clicked.connect(self.close)
        fendang = {}
        # 遍历字典数组中的每个字典
        for dic in self.data:
            if str(dic["档口"]) not in fendang:
                fendang[str(dic["档口"])] = []
            fendang[str(dic["档口"])].append(dic)
        for item in fendang.keys():
            # 创建一个QListWidgetItem对象
            list_item = QListWidgetItem()
            # 设置该项的文本为数组中的元素
            list_item.setText(item)
            # 将该项添加到QListWidget中
            self.listWidget.addItem(list_item)
        self.listWidget.itemClicked.connect(
            lambda item: self.flush(fendang[item.text()], item.text()))

    def flush(self, data, dang):
        self.Widget_2.reload(data, dang)
        pass

    def close(self):
        super().close()
        self.parent.show()
