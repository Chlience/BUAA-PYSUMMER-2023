# -*- coding: utf-8 -*-
from random import choice

from PySide6.QtCore import (QMetaObject, Qt)
from PySide6.QtGui import (QFont, QContextMenuEvent, QAction)
from PySide6.QtWidgets import (QLabel, QWidget, QVBoxLayout, QHBoxLayout, QListWidgetItem)
from qfluentwidgets import ListWidget, PushButton, LineEdit, DWMMenu


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
        self.listWidget = ListWidget(eating)
        self.listWidget.setObjectName(u"listWidget")
        # self.listWidget.setGeometry(QRect(100, 100, 400, 250))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setBold(True)
        font.setPointSize(12)
        self.listWidget.setFont(font)
        font1 = QFont()
        font1.setPointSize(22)
        # self.label.setFont(font1)
        QMetaObject.connectSlotsByName(eating)


class simple_search_view(QWidget, Ui_eating):
    def __init__(self, user, mother):
        super().__init__()
        self.setupUi(self)
        self.font = QFont("宋体", 12)
        self.put_items()
        self.mother = mother
        self.user = user
        self.layout = QVBoxLayout()
        self.input_edit = LineEdit(self)
        self.input_edit.setPlaceholderText("输入关键词就能查找啦\U0001F600")
        self.listWidget.itemClicked.connect(
            lambda item: self.mother.switch_to_food(item.text().split()[0], item.text().split()[8],
                                                    item.text().split()[6]))
        self.layout.addWidget(self.input_edit)
        self.layout.addWidget(self.listWidget)
        # 创建按钮
        self.button1 = PushButton("查找", self)
        self.button1.clicked.connect(self.sortByKeyword)
        self.layout.addWidget(self.button1, alignment=Qt.Alignment(Qt.AlignRight | Qt.AlignBottom))
        self.button2 = PushButton("价格排序", self)
        self.button2.clicked.connect(self.sortByCost)
        self.layout.addWidget(self.button2, alignment=Qt.Alignment(Qt.AlignRight | Qt.AlignBottom))
        self.count_times = 0
        self.layout.setContentsMargins(200, 50, 200, 30)
        self.setLayout(self.layout)

    def put_items(self):
        import dbconnect
        self.data = dbconnect.findAllFood()
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


class food_list_view(QWidget, Ui_eating):
    def __init__(self, user):
        super().__init__()
        self.setupUi(self)
        self.user = user
        self.stack = NewWindow('', '', 0, 0, 0, 0, 0)
        # self.stack.setGeometry(500, 0, 400, 250)
        self.food = []
        self.put_items()
        self.listWidget.itemClicked.connect(
            lambda item: self.open_new_window(self, item.text().split()[0],
                                              item.text().split()[2].split('￥')[1], item.text().split()[4],
                                              item.text().split()[6], item.text().split()[8]))
        self.layout = QVBoxLayout()
        self.input_edit = LineEdit(self)
        self.input_edit.setPlaceholderText("输入关键词就能查找啦\U0001F600")
        wid = QWidget()
        wid.setFixedHeight(22)
        self.layout.addWidget(wid)
        self.layout.addWidget(self.input_edit)
        self.layout.addWidget(self.listWidget)
        # 创建按钮
        self.button1 = PushButton("查找", self)
        self.button1.clicked.connect(self.sortByKeyword)
        self.layout.addWidget(self.button1, alignment=Qt.Alignment(Qt.AlignRight | Qt.AlignBottom))
        self.button2 = PushButton("价格排序", self)
        self.button2.clicked.connect(self.sortByCost)
        self.layout.addWidget(self.button2, alignment=Qt.Alignment(Qt.AlignRight | Qt.AlignBottom))
        self.hLayout = QHBoxLayout()
        self.hLayout.addLayout(self.layout)
        self.hLayout.addWidget(self.stack)
        self.setLayout(self.hLayout)
        self.count_times = 0

    def put_items(self):
        import dbconnect
        self.data = dbconnect.findAllFood()
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

    def open_new_window(self, item, food, cost, kind, count, house):
        self.stack.check(food, cost, self.user, kind, count, house)
        print('check to' + food)


'''class canting_view(food_list_view):
    def __init__(self, uname, tName):
        ran = choice(['大酬宾', '促销', '正在营业'])
        if ran != '正在营业':
            self.count = True
        self.uname = uname
        self.tName = tName
        super().__init__(uname)
        self.resize(532, 780)

    def put_items(self):
        from dbconnect import getplacefood
        self.data = getplacefood(self.tName)
        for da in self.data:
            item = QListWidgetItem(
                "{} - ￥{} - {} - {} - {}".format(da['菜名'], da['价格'], da['类别'], da['食堂'], da['档口'])
            )
            item.setFont(self.font)
            self.listWidget.addItem(item)

'''

'''class catagory_food(food_list_view):
    def __init__(self, uname, category):
        self.uname = uname
        self.kind = category
        super().__init__(uname)
        self.setWindowTitle(uname + "想看看" + category + "种类的食物")

    def put_items(self):
        from dbconnect import getkindfood
        self.data = getkindfood(self.kind)

'''
class count_list(food_list_view):
    def __init__(self, uname, data, count_name, mother):
        self.data = data
        self.uname = uname
        self.mother = mother
        self.font = QFont('宋体', 12)
        super().__init__(uname)
        self.setWindowTitle(count_name)
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(self.show_menu)
        self.create_actions()
        self.create_menu()
        self.input_edit.setPlaceholderText("输入关键词就能查找啦\U0001F600 / 右键进入特定菜品")

    def create_actions(self):
        self.action_delete = QAction("", self)
        if self.listWidget.currentItem():
            item_text = self.listWidget.currentItem().text()
            self.action_delete.triggered.connect(
                self.mother.switch_to_food(item_text.split()[0], item_text.split()[8],
                                                        item_text.split()[6]))

    def create_menu(self):
        self.context_menu = DWMMenu(self)
        self.context_menu.hide()
        self.context_menu.addAction(self.action_delete)

    def show_menu(self, position):
        index = self.listWidget.indexAt(position)
        if index.isValid():
            self.create_actions()



    def put_items(self):
        self.listWidget.clear()
        for da in self.data:
            item = QListWidgetItem(
                "{} - ￥{} - {} - {} - {}".format(da['菜名'], da['价格'], da['类别'], da['食堂'], da['档口'])
            )
            item.setFont(self.font)
            self.listWidget.addItem(item)

    def reload(self, data, count_name):
        self.listWidget.clear()
        self.count = count_name
        self.data = data
        self.put_items()

    def clear(self):
        self.listWidget.clear()


class NewWindow(QWidget):
    def __init__(self, item_text, foodname, cost, username, kind, housename, countname):
        super().__init__()
        self.kind = kind
        self.username = username
        self.food_name = foodname
        self.count_name = countname
        self.house_name = housename
        self.cost = cost
        font = QFont()
        font.setBold(True)  # 设置字体为粗体
        font.setPointSize(12)  # 设置字体大小
        self.layout = QVBoxLayout()
        label = QLabel(item_text)
        self.layout.addWidget(label)
        self.button = PushButton("进食", self)
        self.button.setFont(font)  # 设置按钮字体
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.eat)
        self.button = PushButton("收藏", self)
        self.button.setFont(font)  # 设置按钮字体
        self.button.clicked.connect(self.star)
        self.layout.addWidget(self.button)
        from .comment_page import comment_window
        self.comment_window = comment_window(username, foodname, countname, housename)
        self.comment_window.setFont(font)
        self.layout.addWidget(self.comment_window)
        self.setLayout(self.layout)

    def check(self, food_name, cost, username, kind, house_name, count_name):
        self.kind = kind
        self.username = username
        self.food_name = food_name
        self.count_name = count_name
        self.house_name = house_name
        self.cost = cost
        self.comment_window.checkout(username, food_name, count_name, house_name)

    def star(self):
        if self.food_name == '':
            return
        print('star' + self.food_name)
        name = self.username
        from dbconnect import addstar
        addstar(name, self.food_name, self.count_name, self.house_name)

    def eat(self):
        if self.food_name == '':
            return
        print('eat' + self.food_name)
        name = self.username
        from dbconnect import eatchange, addcost
        eatchange(self.house_name, self.count_name, self.food_name)
        addcost(name, self.cost)
        from dbconnect import lastchange
        lastchange(name, self.kind)
