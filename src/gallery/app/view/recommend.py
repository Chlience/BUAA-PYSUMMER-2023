# coding:utf-8
from gallery.app.common.translator import Translator
from gallery.app.view.gallery_interface import GalleryInterface
import datetime
import random

from PySide6.QtCore import (QCoreApplication, QDateTime, QMetaObject, QRect,
                            Slot, QTimer)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QWidget, QGridLayout)
from qfluentwidgets import TextEdit

import global_


class Recommend(GalleryInterface):
    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title='Recommend',
            subtitle='Just try it.',
            parent=parent
        )
        self.setObjectName('dialogInterface')
        layout = QGridLayout(self)
        from global_ import name
        self.groom = RecommendPage(name)
        layout.addWidget(self.groom, 1, 0)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 5)
        self.setLayout(layout)

    def refresh11(self):
        self.groom.refresh12()


class UiForm(object):
    def __init__(self):
        self.label = None
        self.TextEdit = None

    def setup_ui(self, form):
        if not form.objectName():
            form.setObjectName(u"Form")
        form.setEnabled(True)
        form.resize(1000, 700)
        self.label = QLabel(form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(100, 40, 700, 100))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(25)
        font.setBold(False)
        self.label.setFont(font)
        self.TextEdit = TextEdit(form)
        self.TextEdit.setObjectName(u"plainTextEdit")
        self.TextEdit.setGeometry(QRect(80, 180, 700, 300))
        font.setPointSize(18)
        self.TextEdit.setFont(font)
        # self.translate_ui(form)

        QMetaObject.connectSlotsByName(form)

    # def translate_ui(self, form):
    #     # form.setWindowTitle(QCoreApplication.translate("Form", u"\u4eca\u65e5\u63a8\u8350", None))
    #     form.setWindowTitle("test set")
    #     # self.label.setText(QCoreApplication.translate("Form", u"\u73b0\u5728\u662f", None))
    #     self.label.setText("test set")


class RecommendPage(QWidget, UiForm):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.setup_ui(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.timer = QTimer(self)
        self.timer.start(1000)  # 每秒触发一次 timeout 事件
        self.timer.timeout.connect(self.update_time)
        self.refresh12()

    @Slot()
    def update_time(self):
        current_time = 'Current time is:\n' + QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.label.setText(current_time)
        return current_time

    def refresh12(self):
        self.TextEdit.clear()
        now = datetime.datetime.now()
        from dbconnect import findTimeFood
        from dbconnect import getlast
        parray = getlast(self.name)
        most_frequent_food = global_.get_most_frequent(parray)
        recommendation = "考虑到您最近喜欢" + most_frequent_food + "\n" if most_frequent_food != -100 else "考虑到您最近没来食堂吃饭\n"
        filtered_food = []

        if 3 <= now.hour < 10:
            filtered_food = findTimeFood('早餐')
        elif 10 <= now.hour < 15:
            filtered_food = findTimeFood('午餐')
        elif 15 <= now.hour <= 24 or now.hour in range(0, 2):
            filtered_food = findTimeFood('晚餐')
        # 随机选择一道菜品
        __dict = {'鸡肉': '高蛋白，低脂肪，营养丰富。',
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
            recommendation += f"推荐您现在吃：<b>{chosen_food['菜名']}</b>" + '<br>'
            recommendation += "因为这种食品" + __dict.get(chosen_food['类别']) + "很适合这个时间点吃哦" + '<br>'
            if 3 <= now.hour < 10:
                recommendation += '而且现在是早上，早餐是一天中的第一餐，为身体提供所需的能量，帮助启动<b>新的一天</b>哦。' + '<br>'
            elif 10 <= now.hour < 15:
                recommendation += '而且现在是中午，适当的午餐可以提高<b>工作效率和专注力</b>，有助于应对下午的工作或学习任务。' + '<br>'
            elif 15 <= now.hour <= 24 or now.hour in range(0, 2):
                recommendation += '而且现在是晚上，晚餐可以帮助身体进行<b>恢复和修复</b>，为夜间的休息提供所需的营养和能量。' + '<br>'
            for info in filtered_food:
                if info['菜名'] == chosen_food['菜名']:
                    recommendation += f"价格：{info['价格']}元<br>类别：{info['类别']}"
                    break
        else:
            recommendation = "现在太晚了，食堂都关门了，好好休息吧"
        self.TextEdit.setHtml(recommendation)
