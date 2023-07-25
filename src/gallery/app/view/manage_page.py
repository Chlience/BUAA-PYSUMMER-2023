# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manage_pageNqEzJK.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QPlainTextEdit,
                               QSizePolicy, QSpacerItem, QTextBrowser,
                               QWidget)
from qfluentwidgets import CaptionLabel, PushButton, PlainTextEdit


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(862, 623)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.plainTextEdit_cate = QPlainTextEdit(Form)
        self.plainTextEdit_cate.setObjectName(u"plainTextEdit_cate")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(14)
        self.plainTextEdit_cate.setFont(font)

        self.gridLayout.addWidget(self.plainTextEdit_cate, 2, 1, 1, 1)

        self.label_category = CaptionLabel(Form)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(16)
        self.label_category.setFont(font1)
        self.label_category.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_category, 2, 0, 1, 1)

        self.label_cost = CaptionLabel(Form)
        self.label_cost.setObjectName(u"label_cost")
        self.label_cost.setFont(font1)
        self.label_cost.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_cost, 1, 0, 1, 1)

        self.pushButton_af = PushButton(Form)
        self.pushButton_af.setObjectName(u"pushButton_af")
        self.pushButton_af.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setFamilies([u"\u5b8b\u4f53"])
        font2.setPointSize(12)
        self.pushButton_af.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_af, 3, 3, 1, 1)

        self.plainTextEdit_count = PlainTextEdit(Form)
        self.plainTextEdit_count.setObjectName(u"plainTextEdit_count")
        self.plainTextEdit_count.setFont(font)

        self.gridLayout.addWidget(self.plainTextEdit_count, 5, 1, 1, 1)

        self.plainTextEdit_cost = PlainTextEdit(Form)
        self.plainTextEdit_cost.setObjectName(u"plainTextEdit_cost")
        self.plainTextEdit_cost.setFont(font)

        self.gridLayout.addWidget(self.plainTextEdit_cost, 1, 1, 1, 1)

        self.pushButton_cf = PushButton(Form)
        self.pushButton_cf.setObjectName(u"pushButton_cf")
        self.pushButton_cf.setMinimumSize(QSize(0, 100))
        self.pushButton_cf.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_cf, 5, 3, 1, 1)

        self.label_house = CaptionLabel(Form)
        self.label_house.setObjectName(u"label_house")
        self.label_house.setFont(font1)
        self.label_house.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_house, 4, 0, 1, 1)

        self.pushButton_cc = PushButton(Form)
        self.pushButton_cc.setObjectName(u"pushButton_cc")
        self.pushButton_cc.setMinimumSize(QSize(0, 100))
        self.pushButton_cc.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_cc, 5, 4, 1, 1)

        self.label_food = CaptionLabel(Form)
        self.label_food.setObjectName(u"label_food")
        self.label_food.setFont(font1)
        self.label_food.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_food, 0, 0, 1, 1)

        self.pushButton_dc = PushButton(Form)
        self.pushButton_dc.setObjectName(u"pushButton_dc")
        self.pushButton_dc.setMinimumSize(QSize(0, 100))
        self.pushButton_dc.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_dc, 4, 4, 1, 1)

        self.pushButton_df = PushButton(Form)
        self.pushButton_df.setObjectName(u"pushButton_df")
        self.pushButton_df.setMinimumSize(QSize(0, 100))
        self.pushButton_df.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_df, 4, 3, 1, 1)

        self.label_time = CaptionLabel(Form)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setFont(font1)
        self.label_time.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_time, 3, 0, 1, 1)

        self.plainTextEdit_food = PlainTextEdit(Form)
        self.plainTextEdit_food.setObjectName(u"plainTextEdit_food")
        self.plainTextEdit_food.setFont(font)

        self.gridLayout.addWidget(self.plainTextEdit_food, 0, 1, 1, 1)

        self.label_count = CaptionLabel(Form)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setFont(font1)
        self.label_count.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_count, 5, 0, 1, 1)

        self.plainTextEdit_time = PlainTextEdit(Form)
        self.plainTextEdit_time.setObjectName(u"plainTextEdit_time")
        self.plainTextEdit_time.setFont(font)

        self.gridLayout.addWidget(self.plainTextEdit_time, 3, 1, 1, 1)

        self.plainTextEdit_house = PlainTextEdit(Form)
        self.plainTextEdit_house.setObjectName(u"plainTextEdit_house")
        self.plainTextEdit_house.setFont(font)

        self.gridLayout.addWidget(self.plainTextEdit_house, 4, 1, 1, 1)

        self.pushButton_ac = PushButton(Form)
        self.pushButton_ac.setObjectName(u"pushButton_ac")
        self.pushButton_ac.setMinimumSize(QSize(0, 100))
        self.pushButton_ac.setFont(font2)

        self.gridLayout.addWidget(self.pushButton_ac, 3, 4, 1, 1)

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        font3 = QFont()
        font3.setFamilies([u"\u9ed1\u4f53"])
        font3.setPointSize(16)
        self.textBrowser.setFont(font3)

        self.gridLayout.addWidget(self.textBrowser, 0, 3, 3, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_category.setText(QCoreApplication.translate("Form", u"\u79cd\u7c7b", None))
        self.label_cost.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c", None))
        self.pushButton_af.setText(QCoreApplication.translate("Form", u"\u589e\u52a0\u83dc\u54c1", None))
        self.pushButton_cf.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u83dc\u54c1", None))
        self.label_house.setText(QCoreApplication.translate("Form", u"\u98df\u5802", None))
        self.pushButton_cc.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u6863\u53e3", None))
        self.label_food.setText(QCoreApplication.translate("Form", u"\u83dc\u540d", None))
        self.pushButton_dc.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u6863\u53e3", None))
        self.pushButton_df.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u83dc\u54c1", None))
        self.label_time.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
        self.label_count.setText(QCoreApplication.translate("Form", u"\u6863\u53e3", None))
        self.pushButton_ac.setText(QCoreApplication.translate("Form", u"\u589e\u52a0\u6863\u53e3", None))
    # retranslateUi


class manage_widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_af.clicked.connect(lambda: self.process_info(1))
        self.pushButton_ac.clicked.connect(self.jiadan)
        self.pushButton_cc.clicked.connect(self.gaidan)
        self.pushButton_dc.clicked.connect(self.shandan)
        self.pushButton_cf.clicked.connect(lambda: self.process_info(0))
        self.pushButton_dc.clicked.connect(self.delcai)

    def jiadan(self):
        self.textBrowser.setPlainText('在添加菜品时， 不存在的档口会被自动添加。')

    def shandan(self):
        from dbconnect import deldang
        deldang(self.plainTextEdit_house.toPlainText(), self.plainTextEdit_count.toPlainText())
        self.textBrowser.setPlainText('已经没有这个档口了')

    def gaidan(self):
        if '->' not in self.plainTextEdit_count.toPlainText():
            self.textBrowser.setPlainText('档口处应输入 原档口->新档口')
            return
        if self.plainTextEdit_house.toPlainText() == '':
            self.textBrowser.setPlainText('请输入食堂名字')
            return
        from dbconnect import gaidang
        yuan = self.plainTextEdit_count.toPlainText().split('->')[0].strip()
        xian = self.plainTextEdit_count.toPlainText().split('->')[1].strip()
        gaidang(yuan, xian, self.plainTextEdit_house.toPlainText())
        self.textBrowser.setPlainText('已修改')

    def func1(self):
        from dbconnect import delAll_user
        try:
            delAll_user()
        except:
            self.textBrowser.setPlainText('无权限')
            return
        self.textBrowser.setPlainText('成功删除普通账号')

    def delcai(self):
        food = self.plainTextEdit_food.toPlainText()
        place = self.plainTextEdit_house.toPlainText()
        count = self.plainTextEdit_count.toPlainText()
        from dbconnect import delafood
        ret = delafood(food, count, place)
        if ret:
            self.textBrowser.setPlainText(f'您以后吃不到{food}了\U0001F613')
        else:
            self.textBrowser.setPlainText(f'没有这道菜\U0001F613')
        pass

    def process_info(self, type):
        self.textBrowser.setPlaceholderText("例如： 饭 0.5 主食 全天 新北 一楼基本伙")
        food_name = self.plainTextEdit_food.toPlainText()
        price = self.plainTextEdit_cost.toPlainText()
        category = self.plainTextEdit_cate.toPlainText()
        meal_time = self.plainTextEdit_time.toPlainText()
        place = self.plainTextEdit_house.toPlainText()
        count = self.plainTextEdit_count.toPlainText()
        if '' in [food_name, place, price, category, count, meal_time]:
            self.textBrowser.setPlainText("请输入完整信息")
            return
        from global_ import arr, sett
        if not ('.' in str(price)):
            self.textBrowser.setPlainText("价格必须是一位小数")
            return
        else:
            price = str(round(float(price), 1))
        if meal_time not in ["早餐", "午餐", "晚餐", "全天", "午餐晚餐"]:
            self.textBrowser.setPlainText("建议用餐时间只能为早/中/晚餐")
            return
        if category not in arr.values():
            self.textBrowser.setPlainText("种类可以是" + str(arr.values()))
            return
        if place not in sett:
            self.textBrowser.setPlainText("地点只能是" + sett)
            return
        from dbconnect import hasthis
        # 检查JSON文件中是否已经存在相同食物名的信息食物 0.1 主食 午餐 wings 北区店
        if hasthis(food_name, count, place):
            if type:
                self.textBrowser.setPlainText("已经有这种食物了，你是否在寻找“修改食物信息”功能？")
                return
            else:
                from dbconnect import gaicai
                gaicai(food_name, count, place, price, category, meal_time)

        else:
            if type == 0:
                self.textBrowser.setPlainText("不能修改没有的东西")
                return
        if type:
            times = 0
            dict = {
                "name": food_name,
                "price": price,
                "category": category,
                "time": meal_time,
                "place": place,
                "times": times,
                "count": count,
                "comment": []
            }
            from dbconnect import jiacai
            jiacai(dict)

        if type:
            self.textBrowser.setPlainText(f"北航的同学有福了！\n可以品尝{food_name}了！")
        else:
            self.textBrowser.setPlainText(f"{food_name}的信息被修改了")
