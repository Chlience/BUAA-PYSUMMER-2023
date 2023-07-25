# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'food_item_pageaHqKbX.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import re

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout,
                               QListWidgetItem, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QDialog)
from qfluentwidgets import PushButton, ComboBox, LineEdit, CaptionLabel, ListWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(964, 844)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 70))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = ComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 60))
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u4e2d\u5b8b"])
        font.setPointSize(16)
        self.comboBox.setFont(font)

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(180, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.make_comment_pushButton = PushButton(Form)
        self.make_comment_pushButton.setObjectName(u"make_comment_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.make_comment_pushButton.sizePolicy().hasHeightForWidth())
        self.make_comment_pushButton.setSizePolicy(sizePolicy1)
        self.make_comment_pushButton.setMinimumSize(QSize(0, 60))
        self.make_comment_pushButton.setFont(font)
        self.make_comment_pushButton.setIconSize(QSize(16, 20))

        self.horizontalLayout.addWidget(self.make_comment_pushButton)

        self.gridLayout.addLayout(self.horizontalLayout, 7, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.comments_listWidget = ListWidget(Form)
        self.comments_listWidget.setObjectName(u"comments_listWidget")

        self.gridLayout.addWidget(self.comments_listWidget, 2, 4, 4, 1)

        self.position_label = CaptionLabel(Form)
        self.position_label.setObjectName(u"position_label")
        self.position_label.setFont(font)
        self.position_label.setAlignment(Qt.AlignLeft)

        self.gridLayout.addWidget(self.position_label, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(120, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 2, 1, 1)

        self.star_num_label = CaptionLabel(Form)
        self.star_num_label.setObjectName(u"star_num_label")
        self.star_num_label.setFont(font)
        self.star_num_label.setAlignment(Qt.AlignLeft)

        self.gridLayout.addWidget(self.star_num_label, 5, 1, 1, 1)

        self.cost_label = CaptionLabel(Form)
        self.cost_label.setObjectName(u"cost_label")
        self.cost_label.setFont(font)
        self.cost_label.setAlignment(Qt.AlignLeft)

        self.gridLayout.addWidget(self.cost_label, 3, 1, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.widget_2, 4, 0, 2, 1)

        self.star_pushButton = PushButton(Form)
        self.star_pushButton.setObjectName(u"star_pushButton")
        self.star_pushButton.setMinimumSize(QSize(0, 60))
        self.star_pushButton.setFont(font)

        self.gridLayout.addWidget(self.star_pushButton, 7, 1, 1, 1)

        self.buy_pushButton = PushButton(Form)
        self.buy_pushButton.setObjectName(u"star_pushButton")
        self.buy_pushButton.setMinimumSize(QSize(0, 60))
        self.buy_pushButton.setMaximumSize(QSize(90, 60))
        self.buy_pushButton.setFont(font)

        self.gridLayout.addWidget(self.buy_pushButton, 7, 2, 1, 1)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.widget_3, 2, 5, 1, 1)

        self.level_label = CaptionLabel(Form)
        self.level_label.setObjectName(u"level_label")
        self.level_label.setMinimumSize(QSize(141, 0))
        self.level_label.setMaximumSize(QSize(16777215, 117))
        font1 = QFont()
        font1.setFamilies([u"\u534e\u6587\u4e2d\u5b8b"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.level_label.setFont(font1)
        self.level_label.setAlignment(Qt.AlignLeft)

        self.gridLayout.addWidget(self.level_label, 2, 1, 1, 1)

        self.label = CaptionLabel(Form)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"\u534e\u6587\u4e2d\u5b8b"])
        font2.setPointSize(22)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 4)

        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"None", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"5", None))

        self.comboBox.setPlaceholderText("评分")
        self.make_comment_pushButton.setText(QCoreApplication.translate("Form", u"\u589e\u52a0\u8bc4\u8bba", None))
        self.position_label.setText(QCoreApplication.translate("Form", u"\u4f4d\u7f6e", None))
        self.star_num_label.setText(QCoreApplication.translate("Form", u"\u6536\u85cf\u4eba\u6570", None))
        self.cost_label.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c", None))
        self.star_pushButton.setText(QCoreApplication.translate("Form", u"\u6536\u85cf", None))
        self.level_label.setText(QCoreApplication.translate("Form", u"\u8bc4\u5206", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u83dc\u540d", None))
        self.buy_pushButton.setText('购买')


class food_item(Ui_Form, QWidget):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
        self.user = name
        self.info = {}
        self.hasSet = False
        self.focu = False
        self.comments_listWidget.itemClicked.connect(self.select_comment)

    def set_food(self, info_dic):
        self.comments_listWidget.clear()
        if not self.hasSet:
            self.hasSet = True
            self.star_pushButton.clicked.connect(self.star_move)  # 连接 clicked 信号与 star_move() 槽函数
            self.make_comment_pushButton.clicked.connect(self.cm_show)
            self.buy_pushButton.clicked.connect(self.buyOne)
            self.comboBox.currentIndexChanged.connect(self.handle_combo_box_changed)
        self.cost_label.setText('价格：' + str(info_dic['价格']))
        self.position_label.setText('位置：' + info_dic['食堂'])
        self.label.setText(info_dic['菜名'] + '(' + info_dic['档口'] + '档口' + ')')
        self.level_label.setText('评分：' + str(info_dic['评分']))
        self.star_num_label.setText('收藏人数：' + str(info_dic['收藏人数']))
        self.info = info_dic
        from dbconnect import getrank
        score = getrank(self.user, self.info['菜名'], self.info['档口'], self.info['食堂'])
        if score != "None":
            self.comboBox.setPlaceholderText("我的评分：" + str(score - 1))
        else:
            self.comboBox.setPlaceholderText("评分")
        from dbconnect import getstar
        star_list = getstar(self.user)
        if str(self.info['食堂'] + '-' + self.info['档口'] + '-' + self.info['菜名']) in star_list:
            print('已收藏' + self.info['菜名'])
            self.star_pushButton.setText('已收藏')
            self.star_pushButton.setStyleSheet("background-color: yellow;")
        else:
            self.star_pushButton.setText('收藏')
            self.star_pushButton.setStyleSheet("background-color: white;")
        from dbconnect import loadcomment
        self.comments = loadcomment(info_dic['食堂'], info_dic['档口'], info_dic['菜名'])
        for text in self.comments:
            item = QListWidgetItem(text)
            font = QFont("宋体", 12)
            item.setFont(font)
            self.comments_listWidget.addItem(item)

    def select_comment(self):
        if self.focu == True:
            self.comments_listWidget.setCurrentItem(None)
            self.focu = False
        else:
            self.focu = True

    def cm_show(self):
        selected_item = self.comments_listWidget.currentItem()
        tip = (self.info['食堂'], self.info['档口'], self.info['菜名'])
        if selected_item == None:
            self.subwindow = SubWindow(0, '', self.user, self, tip)
        else:
            self.subwindow = SubWindow(1, selected_item.text(), self.user, self, tip)
        self.subwindow.exec_()

    def star_move(self):
        if self.star_pushButton.text() == '收藏':
            print('进行收藏')
            self.star_pushButton.setText('已收藏')
            self.star_pushButton.setStyleSheet("background-color: yellow;")
            self.star_num_label.setText('收藏人数：' + str(int(self.star_num_label.text().split('：')[1]) + 1))
            from dbconnect import addstar
            addstar(self.user, self.info['菜名'], self.info['档口'], self.info['食堂'])
        else:
            print('进行取消收藏')
            self.star_pushButton.setText('收藏')
            self.star_num_label.setText('收藏人数：' + str(int(self.star_num_label.text().split('：')[1]) - 1))
            self.star_pushButton.setStyleSheet("background-color: white;")
            from dbconnect import changestar
            changestar(self.user, self.info['菜名'] + '-' + self.info['档口'] + '-' + self.info['食堂'])

    def handle_combo_box_changed(self, index):
        selected_text = self.comboBox.currentText()
        selected_index = index
        print(f"选择项改变：{selected_text} (索引：{selected_index})")
        from dbconnect import addrank
        addrank(self.user, self.info['菜名'], self.info['档口'], self.info['食堂'], index + 1)

    def buyOne(self):
        from dbconnect import eatchange, lastchange, addcost
        eatchange(self.info['食堂'], self.info['档口'], self.info['菜名'])
        lastchange(self.user, self.info['类别'])
        addcost(self.user, self.info['价格'])


from datetime import datetime


class SubWindow(QDialog):
    def __init__(self, type, text, name, mother, tup):
        super().__init__()
        self.tup = tup
        self.mother = mother
        self.name = name
        self.type = type
        self.text = text
        self.setWindowTitle("子窗口")
        self.setGeometry(1200, 700, 200, 150)
        # 创建文本框和按钮
        self.text_edit = LineEdit()
        if type == 0:
            self.setWindowTitle('提交评论页面')
            self.button = PushButton("提交")
        else:
            self.setWindowTitle('回复评论页面')
            self.button = PushButton("回复")
        self.button.clicked.connect(self.button_clicked)
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.setWindowFlags(self.windowFlags() | Qt.Tool)
        self.text_edit.setFocus()

    def button_clicked(self):
        # 按钮的槽函数
        make_text = self.text_edit.text()
        comment = make_text.replace("\t", " ")
        print("按钮被点击，文本框内容为:", make_text)

        if self.type == 1:
            selected_comment = self.text
            reply_comment_pattern = re.compile("\[[0-9]*-[0-9]* [0-9]*:[0-9]*] (.*) 回复 (.*): (.*)")
            single_comment_pattern = re.compile("\[[0-9]*-[0-9]* [0-9]*:[0-9]*] (.*): (.*)")

            comment_match = re.match(reply_comment_pattern, selected_comment)
            if comment_match is None:
                comment_match = re.match(single_comment_pattern, selected_comment)
                name = comment_match.group(1)
            else:
                name = comment_match.group(1)
            current_time = datetime.now().strftime("%m-%d %H:%M")  # 获取当前时间
            full_comment = f"[{current_time}] {self.name} 回复 {name}: {comment}"
        else:
            current_time = datetime.now().strftime("%m-%d %H:%M")  # 获取当前时间
            full_comment = f"[{current_time}] {self.name}: {comment}"
        print("提交评论:", full_comment)
        item = QListWidgetItem(full_comment)
        font = QFont("宋体", 12)
        item.setFont(font)
        self.mother.comments_listWidget.addItem(item)
        from dbconnect import add_comment
        add_comment(full_comment, self.tup[0], self.tup[1], self.tup[2])
        self.close()
