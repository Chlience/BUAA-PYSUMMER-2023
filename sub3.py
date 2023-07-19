# -*- coding: utf-8 -*-
import datetime
import random

from PySide6.QtCore import (QCoreApplication, QDateTime, QMetaObject, QRect,
                            Qt, Slot, QTimer)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QWidget, QTextEdit, QPushButton, QGridLayout)

import global1


################################################################################
## Form generated from reading UI file 'designerotFsVs.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(498, 548)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(100, 40, 291, 61))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(18)
        font.setBold(False)
        self.label.setFont(font)
        self.TextEdit = QTextEdit(Form)
        self.TextEdit.setObjectName(u"plainTextEdit")
        self.TextEdit.setGeometry(QRect(80, 180, 341, 251))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4eca\u65e5\u63a8\u8350", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u73b0\u5728\u662f", None))
    # retranslateUi


class sub3(QWidget, Ui_Form):
    def __init__(self, parent, name):
        super().__init__()
        self.name = name
        self.parent = parent
        self.setupUi(self)
        btn = QPushButton("返回", self)
        btn.clicked.connect(self.close)  # 点击按钮时退出应用程序
        # 创建一个水平布局
        layout = QGridLayout()
        layout.addWidget(btn, 0, 0, alignment=Qt.AlignBottom | Qt.AlignRight)  # 将按钮放置在第一行第一列，并向右下角对齐
        self.setLayout(layout)
        self.timer = QTimer(self)
        now = datetime.datetime.now()
        self.timer.start(1000)  # 每秒触发一次 timeout 事件
        self.timer.timeout.connect(self.update_time)
        from dbconnect import findAllFood
        food_data = findAllFood()
        from dbconnect import getlast
        parray = getlast(self.name)
        strr = global1.get_most_frequent(parray)
        recommendation = "考虑到您最近喜欢" + strr + "\n" if strr != -100 else "考虑到您最近没来食堂吃饭\n"
        filtered_food = []
        for food in food_data:
            if now.hour >= 3 and now.hour < 10 and "早餐" in food["time"]:
                filtered_food.append(food)
            elif now.hour >= 10 and now.hour < 15 and "午餐" in food["time"]:
                filtered_food.append(food)
            elif (now.hour >= 15 and now.hour <= 24 or now.hour in range(0, 2)) and "晚餐" in food['时间']:
                filtered_food.append(food)
        # 随机选择一道菜品
        dicc = {'鸡肉': '高蛋白，低脂肪，营养丰富。',
                '猪肉': '丰富营养，口感鲜美。',
                '蛋类': '含有优质蛋白，营养丰富。',
                '豆类': '富含植物蛋白，纤维丰富。',
                '牛肉': '含有丰富铁质，提供能量。',
                '蔬菜': '富含纤维，维生素多。',
                '鱼肉': '富含ω-3脂肪酸，有益心脑血管。',
                '咖啡': '提高警觉性和注意力，帮助人们保持清醒和专注。',
                '小吃': '在口味上丰富多样，能够满足人们对美食的需求，也是文化和地方特色的体现。',
                '西餐': '可以体验西方的文化风情。',
                '主食': '主食通常富含碳水化合物，是人体获取能量的重要来源。',
                '饮料': '不仅可以解渴，也具有独特的口味和香气，可以给人带来享受和放松的感觉',
                '甜品': '具有甜美的味道，满足人们对甜食的渴望和享受，带来愉悦和满足感。'
                }
        if len(filtered_food) > 0:
            chosen_food = random.choice(filtered_food)
            recommendation += f"推荐您现在吃<br> \\\\ <b>{chosen_food['菜名']}</b> //<br>"
            recommendation += "因为这种食品" + dicc.get(chosen_food['类别'],
                                                        "很适合这个时间点吃哦\U0001F604") + '<br>'
            if now.hour >= 3 and now.hour < 10:
                recommendation += '而且现在是早上，早餐是一天中的第一餐，为身体提供所需的能量，帮助启动<b>新的一天</b>哦。'
            elif now.hour >= 10 and now.hour < 15:
                recommendation += '而且现在是中午，适当的午餐可以提高<b>工作效率和专注力</b>，有助于应对下午的工作或学习任务。'
            elif (now.hour >= 15 and now.hour <= 24 or now.hour in range(0, 2)):
                recommendation += '而且现在是晚上，晚餐可以帮助身体进行<b>恢复和修复</b>，为夜间的休息提供所需的营养和能量。'
            for info in filtered_food:
                if info['菜名'] == chosen_food['菜名']:
                    additional_info = f"价格：{info['价格']}元<br>类别：{info['类别']}"
                    recommendation += "<br>" + additional_info
                    break

        else:
            recommendation = "现在太晚了，食堂都关门了，好好休息吧\U0001F604"

        # 将推荐的食物信息显示在 self.plainTextEdit 中
        self.TextEdit.setHtml(recommendation)

    def closeEvent(self, event):
        self.parent.show()  # 关闭子窗口时显示母窗口
        event.accept()

    @Slot()
    def update_time(self):
        current_time = '现在是北京时间：\n' + QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.label.setText(current_time)
        return current_time
