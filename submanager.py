# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'designerYCazlI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            )
from PySide6.QtGui import QFont, QPainter, QColor
from PySide6.QtWidgets import (QLabel, QPushButton, QVBoxLayout, QWidget, QPlainTextEdit, QHBoxLayout, QApplication)

import global1


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(529, 380)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 30, 211, 71))
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u5f69\u4e91"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 210, 181, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.shanhao = QPushButton(self.layoutWidget)
        self.shanhao.setObjectName(u"shanhao")
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(12)
        self.shanhao.setFont(font1)
        self.shanhao.clicked.connect(self.func1)
        self.verticalLayout.addWidget(self.shanhao)

        self.jiacai = QPushButton(self.layoutWidget)
        self.jiacai.setObjectName(u"jiacai")
        self.jiacai.setFont(font1)
        self.jiacai.clicked.connect(lambda: self.process_info(1))
        self.verticalLayout.addWidget(self.jiacai)
        self.shancai = QPushButton(self.layoutWidget)
        self.shancai.setObjectName(u"shancai")
        self.shancai.setFont(font1)
        self.shancai.clicked.connect(self.delcai)
        self.verticalLayout.addWidget(self.shancai)
        self.gaicai = QPushButton(self.layoutWidget)
        self.gaicai.clicked.connect(lambda: self.process_info(0))
        self.gaicai.setObjectName(u"gaicai")
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.gaicai.setFont(font2)
        self.verticalLayout.addWidget(self.gaicai)
        self.yonghu = QPushButton(self.layoutWidget)
        self.yonghu.setObjectName(u"yonghu")
        self.yonghu.setFont(font1)
        self.verticalLayout.addWidget(self.yonghu)
        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(163, 110, 201, 71))
        font3 = QFont()
        font3.setFamilies([u"\u5b8b\u4f53"])
        font3.setPointSize(12)
        self.plainTextEdit.setFont(font3)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def func1(self):
        global1.Data = {}
        self.plainTextEdit.setPlainText('成功删除普通账号')

    def delcai(self):
        info = self.plainTextEdit.toPlainText().strip()
        food_info_list = global1.Data2
        if any(item.get('name') == info for item in food_info_list):
            food_info_list = [item for item in food_info_list if item.get('name') != info]
            self.plainTextEdit.setPlainText(f'您以后吃不到{info}了\U0001F613')
            global1.Data2 = food_info_list
        else:
            self.plainTextEdit.setPlainText(f'没有这道菜\U0001F613')

    def process_info(self, type):
        times = 0
        from ui import is_all_chinese
        info = self.plainTextEdit.toPlainText().strip().split(" ")
        self.plainTextEdit.setPlaceholderText("例如： 饭 0.5 主食 全天 新北")
        food_info_list = global1.Data2
        if len(info) == 5:
            food_name = info[0]
            price = info[1]
            category = info[2]
            meal_time = info[3]
            place = info[4]
            if not is_all_chinese(place) or not is_all_chinese(food_name[-1]):
                self.plainTextEdit.setPlainText("你需要输入更多的中文")
                return
            if not ('.' in str(price)):
                self.plainTextEdit.setPlainText("价格必须是一位小数")
                return
            else:
                price = str(round(float(price), 1))
            if meal_time not in ["早餐", "午餐", "晚餐", "全天", "午餐晚餐"]:
                self.plainTextEdit.setPlainText("建议用餐时间只能为早/中/晚餐")
                return
            # 检查JSON文件中是否已经存在相同食物名的信息
            if any(item.get('name') == food_name for item in food_info_list):
                if type:
                    self.plainTextEdit.setPlainText("已经有这种食物了，你是否在寻找“修改食物信息”功能？")
                    return
                else:
                    try:
                        x = [item for item in food_info_list if item.get('name') == food_name]
                        times = x[0]['times']
                    except:
                        times = 0
                    food_info_list = [item for item in food_info_list if item.get('name') != food_name]

            else:
                if type == 0:
                    self.plainTextEdit.setPlainText("不能修改没有的东西")
                    return
            if type:
                times = 0
            dict = {
                "name": food_name,
                "price": price,
                "category": category,
                "time": meal_time,
                "place": place,
                "times": times
            }
            food_info_list.append(dict)
        else:
            self.plainTextEdit.setPlainText("信息格式不正确\n必须是名字 钱 种类 时间 食堂名字")
            return
        global1.Data2 = food_info_list
        if type:
            self.plainTextEdit.setPlainText(f"北航的同学有福了！\n可以品尝{food_name}了！")
        else:
            self.plainTextEdit.setPlainText(f"{food_name}的信息被修改了")

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7ba1\u7406\u5458\u754c\u9762", None))
        self.label.setText(
            QCoreApplication.translate("Form", u"\u60a8\u597d\uff01  \u8d85\u7ea7\u7ba1\u7406\u5458", None))
        self.shanhao.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u5df2\u6ce8\u518c\u8d26\u53f7", None))
        self.jiacai.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u83dc\u54c1", None))
        self.shancai.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u83dc\u54c1", None))
        self.gaicai.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u83dc\u54c1", None))
        self.yonghu.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u4e2d\u5fc3", None))


class submanger(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('管理中心')
        button = QPushButton('退出', self)
        button.clicked.connect(self.close)
        # 创建垂直布局
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(button)
        # 创建水平布局
        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addLayout(layout)
        self.setLayout(hlayout)
        self.setStyleSheet("QPushButton {"
                           "border-radius: 5px;"
                           "background-color: white;"
                           "text-align: center;"
                           "font-family: '华文中宋';}"
                           "vertical-align: bottom;"
                           "QPushButton:hover {"
                           "background-color: lightGray;"
                           "}"
                           )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor("lightblue"))
        painter.drawRect(self.rect())
