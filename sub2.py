# -*- coding: utf-8 -*-
from random import choice

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QListWidget, QWidget, QVBoxLayout, QLineEdit, QPushButton, QSpacerItem,
                               QSizePolicy)

import global1


################################################################################
## Form generated from reading UI file 'designerxaOMVi.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_eating(object):
    def setupUi(self, eating):
        if not eating.objectName():
            eating.setObjectName(u"eating")
        eating.resize(532, 695)
        self.listWidget = QListWidget(eating)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(130, 100, 256, 451))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setBold(True)
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.label = QLabel(eating)
        self.label.setObjectName(u"label")
        self.label.setGeometry(10, 15, 500, 100)
        self.label.setMaximumWidth(1000)
        # 将标签水平居中对齐
        self.label.setAlignment(Qt.AlignCenter)
        font1 = QFont()
        font1.setPointSize(22)
        self.label.setFont(font1)

        self.retranslateUi(eating)

        QMetaObject.connectSlotsByName(eating)

    # setupUi

    def retranslateUi(self, eating):
        eating.setWindowTitle(QCoreApplication.translate("eating", u"Form", None))
        self.label.setText(QCoreApplication.translate("eating", u"\u98df\u54c1\u5217\u8868", None))
    # retranslateUi


class sub2(QWidget, Ui_eating):
    def __init__(self, parent, neme, count=True):
        super().__init__()
        self.neme = neme
        self.parent = parent
        self.setupUi(self)
        self.label.setText("食品列表")
        self.setWindowTitle(neme + "吃点什么好呢")
        self.food = []
        self.ope()
        self.load()
        self.listWidget.itemClicked.connect(
            lambda item: self.open_new_window(item.text(), item.text().split()[0],
                                              item.text().split()[2].split('￥')[1], item.text().split()[4],
                                              item.text().split()[6], item.text().split()[8]))
        self.layout = QVBoxLayout(self)
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addSpacerItem(spacer_item)
        # 创建输入框
        self.input_edit = QLineEdit(self)
        self.input_edit.setPlaceholderText("输入关键词就能查找啦\U0001F600")
        self.layout.addWidget(self.input_edit)
        # 创建按钮
        self.button1 = QPushButton("查找", self)
        self.button1.clicked.connect(self.sortByKeyword)
        self.layout.addWidget(self.button1, alignment=Qt.Alignment(Qt.AlignRight | Qt.AlignBottom))
        self.button2 = QPushButton("价格排序", self)
        self.button2.clicked.connect(self.sortByCost)
        self.layout.addWidget(self.button2, alignment=Qt.Alignment(Qt.AlignRight | Qt.AlignBottom))
        self.button3 = QPushButton("返回", self)
        self.button3.clicked.connect(self.close)
        self.layout.addWidget(self.button3, alignment=Qt.Alignment(Qt.AlignRight | Qt.AlignBottom))
        self.setLayout(self.layout)
        self.count = 0
        self.show()

    def load(self):
        for da in self.data:
            self.listWidget.addItem(
                "{} - ￥{} - {} - {} - {}".format(da['菜名'], da['价格'], da['类别'], da['食堂'], da['档口']))

    def ope(self):
        import dbconnect
        self.data = dbconnect.findAllFood()

    def sortByCost(self):
        sorted_items = sorted(self.data, key=lambda x: float(x['价格']), reverse=bool(self.count & 1))
        self.listWidget.clear()
        # 根据排序结果重新创建标签
        for dish in sorted_items:
            label = "{} - ￥{} - {}".format(dish['菜名'], dish['价格'], dish['类别'])
            self.listWidget.addItem(label)
        self.count += 1

    def sortByKeyword(self):
        keyword = self.input_edit.text()
        # 计算关键词与每个条目的相关度
        scores = {}
        for item in self.data:
            score = self.calculateScore(item, keyword)
            scores[item['菜名']] = score

        # 根据相关度对条目排序
        sorted_items = sorted(self.data, key=lambda x: scores[x['菜名']], reverse=True)
        self.listWidget.clear()
        # 根据排序结果重新创建标签
        for dish in sorted_items:
            label = "{} - ￥{} - {}".format(dish['菜名'], dish['价格'], dish['类别'])
            self.listWidget.addItem(label)

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

    def open_new_window(self, item, food, cost, kind, count, house):
        # 获取所选项的文本
        selected_item_text = item
        global new_window
        # 创建新窗口并显示
        new_window = NewWindow(selected_item_text, food, cost, self.neme, kind, count, house)
        new_window.show()

    def closeEvent(self, event):
        self.parent.show()  # 关闭子窗口时显示母窗口
        event.accept()


class sub22(sub2):
    def __init__(self, parent, uname, tName):
        ran = choice(['大酬宾', '促销', '正在营业'])
        if ran != '正在营业':
            self.count = True
        dic = {0: '学二', 3: '合一', 5: '新北', 2: '美食苑', 4: 'wings'}
        self.uname = uname
        self.tName = dic[tName]
        super().__init__(parent, uname, False)
        self.label.setText(self.tName + '食堂' + ran)
        self.setWindowTitle(uname + "走了20min路终于到" + self.tName + "食堂了。。吃点什么好呢")
        self.parent = parent
        self.resize(532, 780)
        self.button4 = QPushButton("切换视图", self)
        self.button4.clicked.connect(self.inin)
        self.layout.addWidget(self.button4, alignment=Qt.Alignment(Qt.AlignRight | Qt.AlignBottom))

    def ope(self):
        from dbconnect import getplacefood
        self.data = getplacefood(self.tName)

    def inin(self):
        from subdang import subdang
        self.subdang = subdang(parent=self, tname=self.tName, uname=self.uname, dataspe=self.data)
        self.subdang.show()
        self.hide()


class sub23(sub2):
    def __init__(self, parent, uname, category):
        self.uname = uname
        self.kind = category
        super().__init__(parent, uname, False)
        self.label.setText(category + '类 菜单')
        self.setWindowTitle(uname + "想看看" + category + "种类的食物")
        self.parent = parent

    def ope(self):
        from dbconnect import getkindfood
        self.data = getkindfood(self.kind)


class sub24(sub2):
    def __init__(self, uname, data, dangname):
        self.data = data
        self.uname = uname
        super().__init__(None, uname)
        self.setWindowTitle(dangname)
        self.button3.hide()

    def ope(self):
        pass

    def closeEvent(self, event):
        event.accept()

    def reload(self, data, dang):
        self.listWidget.clear()
        self.data = data
        self.load()
        self.setWindowTitle(dang)


class NewWindow(QWidget):
    def __init__(self, item_text, foodname, cost, username, kind, housename, countname):
        self.kind = kind
        self.username = username
        self.foodname = foodname
        self.countname = countname
        self.housename = housename
        self.cost = cost
        font = QFont()
        font.setBold(True)  # 设置字体为粗体
        font.setPointSize(12)  # 设置字体大小
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.setWindowTitle("真的好吃的")
        self.setGeometry(700, 170, 300, 600)
        layout = QVBoxLayout()
        label = QLabel(item_text)
        layout.addWidget(label)
        self.button = QPushButton("进食", self)
        self.button.setFont(font)  # 设置按钮字体
        layout.addWidget(self.button)
        self.button.clicked.connect(self.eat)
        self.button = QPushButton("收藏", self)
        self.button.setFont(font)  # 设置按钮字体
        self.button.clicked.connect(self.star)
        layout.addWidget(self.button)
        self.back_button = QPushButton("返回", self)
        self.back_button.setFont(font)  # 设置按钮字体
        self.back_button.clicked.connect(self.close)
        layout.addWidget(self.back_button)
        from submit import wid
        self.subwid = wid(username, foodname, countname, housename)
        self.subwid.setFont(font)
        layout.addWidget(self.subwid)
        self.setLayout(layout)

    def star(self):
        name = self.username
        from dbconnect import addstar
        addstar(name, self.foodname)

    def eat(self):
        name = self.username
        from dbconnect import eatchange, addcost
        eatchange(self.housename, self.countname, self.foodname)
        addcost(name, self.cost)
        from dbconnect import lastchange
        lastchange(name, self.kind)

    def close(self):
        self.subwid.save_comments()
        super().close()
