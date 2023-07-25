# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fanshitangshitangxFmZXZ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout,
                               QListWidget, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget, QListWidgetItem)
from qfluentwidgets import CaptionLabel, ComboBox, PushButton, ListWidget, LineEdit


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(777, 590)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = LineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 80))

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.listWidget = ListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = PushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer_3)
        self.pushButton = PushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 1, 1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = CaptionLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout.addWidget(self.label_2)
        self.label = CaptionLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout.addWidget(self.label)
        self.label_3 = CaptionLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout.addWidget(self.label_3)
        self.comboBox = PushButton(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 80))
        self.gridLayout.addWidget(self.widget, 1, 2, 1, 1)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        font = QFont('宋体')
        font.setPointSize(16)
        self.lineEdit.setPlaceholderText("输入关键词就能查找啦\U0001F600")
        self.label_2.setText('评分')
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('营业时间')
        self.label_3.setText('位置')
        self.pushButton_2.setText('价格排序')
        self.pushButton_2.setFont(font)
        self.pushButton.setFont(font)
        self.comboBox.setFont(QFont('宋体', 14))
        self.comboBox.setText('进入分档口')
        self.pushButton.setText('查找')

    # retranslateUi


class canting_view(QListWidget, Ui_Form):
    def __init__(self, t_name, mother):
        super().__init__()
        self.font = QFont("宋体", 12)
        self.setupUi(self)
        from global_ import dic_canting_time,dic_canting_position
        self.label.setText('营业时间'+dic_canting_time.get(t_name,''))
        self.label_3.setText('位置' + dic_canting_position.get(t_name,''))
        self.mother = mother
        self.t_name = t_name
        self.count_times = 0
        self.food = []
        self.put_items()
        if t_name!='':
            self.comboBox.clicked.connect(self.goto_sub)
        self.pushButton_2.clicked.connect(self.sortByCost)
        self.pushButton.clicked.connect(self.sortByKeyword)
        self.listWidget.itemClicked.connect(
            lambda item: self.mother.switch_to_food(item.text().split()[0], item.text().split()[8],
                                                    item.text().split()[6]))

    def goto_sub(self):
        self.mother.goto_sub(self.t_name)

    def put_items(self):
        from dbconnect import getplacefood
        self.data = getplacefood(self.t_name)
        for da in self.data:
            item = QListWidgetItem(
                "{} - ￥{} - {} - {} - {}".format(da['菜名'], da['价格'], da['类别'], da['食堂'], da['档口'])
            )
            item.setFont(self.font)
            self.listWidget.addItem(item)

    def sortByCost(self):
        sorted_items = sorted(self.data, key=lambda x: float(x['价格']), reverse=bool(self.count_times & 1))
        self.listWidget.clear()
        # 根据排序结果重新创建标签
        for da in sorted_items:
            item = QListWidgetItem(
                "{} - ￥{} - {} - {} - {}".format(da['菜名'], da['价格'], da['类别'], da['食堂'], da['档口'])
            )
            item.setFont(self.font)
            self.listWidget.addItem(item)
        self.count_times += 1

    def sortByKeyword(self):
        keyword = self.lineEdit.text()
        # 计算关键词与每个条目的相关度
        scores = {}
        for item in self.data:
            score = self.calculateScore(item, keyword)
            scores[item['菜名']] = score

        # 根据相关度对条目排序
        sorted_items = sorted(self.data, key=lambda x: scores[x['菜名']], reverse=True)
        self.listWidget.clear()
        # 根据排序结果重新创建标签
        for da in sorted_items:
            item = QListWidgetItem(
                "{} - ￥{} - {} - {} - {}".format(da['菜名'], da['价格'], da['类别'], da['食堂'], da['档口'])
            )
            item.setFont(self.font)
            self.listWidget.addItem(item)

    def calculateScore(self, item, keyword):
        # 实现自定义的相关度计算逻辑
        # 这里可以使用各种方法来计算关键词和条目之间的相关度得分
        # 返回得分值，得分越高表示相关度越高
        pric = float(item['价格'])
        if keyword in item['档口'] or keyword in item['食堂']:
            return 20 + pric
        if keyword in item['菜名']:
            return 15 + pric
        elif keyword in item['类别']:
            return 12 + pric
        elif keyword in item['时间']:
            return 20 + pric
        elif keyword in str(item['价格']):
            return 10
        else:
            l1 = self.longest_common_substring(keyword, item['菜名'])
            l2 = self.longest_common_substring(keyword, item['类别'])
            l3 = self.longest_common_substring(keyword, str(item['价格']))
            l4 = self.longest_common_substring(keyword, item['时间'])
            l5 = self.longest_common_substring(keyword, item['档口'])
            l6 = self.longest_common_substring(keyword, item['食堂'])
            return max(l1, l2, l3, l4, l5, l6)

    def longest_common_substring(self, str1, str2):
        # 创建一个二维数组来记录最长公共子串的长度
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        max_length = 0  # 最长公共子串长度
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])

        return max_length
