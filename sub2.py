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
        self.load(count)
        self.listWidget.itemClicked.connect(
            lambda item: self.open_new_window(item.text(), item.text().split()[0],
                                              item.text().split()[2].split('￥')[1], item.text().split()[4]))
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

    def load(self, count):
        dishes = []
        for dish in self.data:
            name = dish['name']
            price = dish['price']
            time = dish['time']
            category = dish['category']
            yes = choice([1, 1, 1, 0.8, 0.9])
            if count:
                dishes.append({
                    'name': name,
                    'price': price,
                    'time': time,
                    'category': category
                })
            else:
                dishes.append({
                    'name': name,
                    'price': str(round(float(price) * yes, 2)),
                    'time': time,
                    'category': category
                })
        for dish in dishes:
            self.listWidget.addItem("{} - ￥{} - {}".format(dish['name'], dish['price'], dish['category']))

    def ope(self):
        self.data = global1.Data2

    def sortByCost(self):
        sorted_items = sorted(self.data, key=lambda x: float(x['price']), reverse=bool(self.count & 1))
        self.listWidget.clear()
        # 根据排序结果重新创建标签
        for dish in sorted_items:
            label = "{} - ￥{} - {}".format(dish['name'], dish['price'], dish['category'])
            self.listWidget.addItem(label)
        self.count += 1

    def sortByKeyword(self):
        keyword = self.input_edit.text()
        # 计算关键词与每个条目的相关度
        scores = {}
        for item in self.data:
            score = self.calculateScore(item, keyword)
            scores[item['name']] = score

        # 根据相关度对条目排序
        sorted_items = sorted(self.data, key=lambda x: scores[x['name']], reverse=True)
        self.listWidget.clear()
        # 根据排序结果重新创建标签
        for dish in sorted_items:
            label = "{} - ￥{} - {}".format(dish['name'], dish['price'], dish['category'])
            self.listWidget.addItem(label)

    def calculateScore(self, item, keyword):
        # 实现自定义的相关度计算逻辑
        # 这里可以使用各种方法来计算关键词和条目之间的相关度得分
        # 返回得分值，得分越高表示相关度越高
        pric = float(item['price'])
        if keyword in item['place']:
            return 20 + pric
        if keyword in item['name']:
            return 15 + pric
        elif keyword in item['category']:
            return 12 + pric
        elif keyword in item['time']:
            return 20 + pric
        elif keyword in str(item['price']):
            return 10
        else:
            l1 = self.longest_common_substring(keyword, item['name'])
            l2 = self.longest_common_substring(keyword, item['category'])
            l3 = self.longest_common_substring(keyword, str(item['price']))
            l4 = self.longest_common_substring(keyword, item['time'])
            l5 = self.longest_common_substring(keyword, item['place'])
            return max(l1, l2, l3, l4, l5)

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

    def open_new_window(self, item, food, cost, kind):
        # 获取所选项的文本
        selected_item_text = item
        global new_window
        # 创建新窗口并显示
        new_window = NewWindow(selected_item_text, food, cost, self.neme, kind)
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
        self.data = [q for q in global1.Data2 if q['place'] == self.tName]

    def inin(self):
        from subdang import subdang
        self.subdang = subdang(parent=self, tname=self.tName, uname=self.uname, dataspe=self.data)
        self.subdang.show()
        self.hide()


class sub23(sub2):
    def __init__(self, parent, uname, category):
        self.uname = uname
        self.kind = []
        if category == '蛋白质':
            self.kind = ["猪肉", "牛肉", "豆腐", "鱼肉", "鸭肉"]
        self.kind.append(category)
        super().__init__(parent, uname, False)
        self.label.setText(category + '类 菜单')
        self.setWindowTitle(uname + "想看看" + category + "种类的食物")
        self.parent = parent

    def ope(self):
        self.data = [q for q in global1.Data2 if q['category'] in self.kind]


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
        self.load(True)
        self.setWindowTitle(dang)


class NewWindow(QWidget):
    def __init__(self, item_text, food, cost, neme, kind):
        self.kind = kind
        self.neme = neme
        self.now = food
        self.cost = cost
        font = QFont()
        font.setBold(True)  # 设置字体为粗体
        font.setPointSize(12)  # 设置字体大小
        super().__init__()
        self.setWindowTitle("真的好吃的")
        self.setGeometry(700, 300, 300, 600)
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
        self.data = global1.Data
        self.data2 = global1.Data2
        from submit import wid
        self.subwid = wid(neme, food)
        self.subwid.setFont(font)
        layout.addWidget(self.subwid)
        self.setLayout(layout)

    def star(self):
        name = self.neme
        if 'star' not in self.data[name]:
            self.data[name]['star'] = []
        if self.now not in self.data[name]['star']:
            self.data[name]['star'].append(self.now)

    def eat(self):
        name = self.neme
        if 'cost' not in self.data[name]:
            self.data[name]['cost'] = 0
        self.data[name]['cost'] += float(self.cost)
        for i in range(len(self.data2)):
            if self.data2[i]['name'] == self.now:
                self.data2[i]['times'] += 1
                break
        if 'last' not in self.data[name]:
            self.data[name]['last'] = []
        self.data[name]['last'].append(self.kind)
        if len(self.data[name]['last']) > 5:
            self.data[name]['last'] = self.data[name]['last'][1:]
        pass

    def close(self):
        global1.Data = self.data
        global1.Data2 = self.data2
        self.subwid.save_comments_to_file()
        super().close()
