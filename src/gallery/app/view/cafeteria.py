# coding:utf-8
from PySide6.QtCore import (QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout,
                               QListWidget, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget, QListWidgetItem)
from qfluentwidgets import CaptionLabel, ComboBox, PushButton, ListWidget, LineEdit
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QGridLayout
from gallery.app.view.gallery_interface import GalleryInterface, ToolBar
from gallery.app.common.translator import Translator


class Cafeteria(GalleryInterface):
    def __init__(self, parent=None):
        self.parent = parent
        self.title = ''
        t = Translator()
        super().__init__(
            title='A wasteland without knowledge',
            subtitle='Is it your favorite?',
            parent=parent
        )
        self.setObjectName('dateTimeInterface')
        self.widget = canting_view('', self)
        self.vBoxLayout.addWidget(self.widget)

    def change(self, canting_name):
        self.title = canting_name
        self.toolBar.changeTitle(canting_name)
        self.vBoxLayout.removeWidget(self.widget)
        self.widget.deleteLater()
        self.widget = canting_view(canting_name, self)
        self.vBoxLayout.addWidget(self.widget)

    def switch_to_food(self, food_name, count_name, house_name):
        self.parent.switch_to_food(food_name, count_name, house_name)

    def goto_sub(self, t):
        self.parent.goto_sub(t)


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
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.listWidget = ListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = PushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 1, 1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = CaptionLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout.addWidget(self.label)
        self.label_3 = CaptionLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        font = QFont('宋体')
        font.setPointSize(12)
        self.lineEdit.setPlaceholderText("Keyword for search")
        self.label_3.setFont(font)
        self.label.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('Business hours')
        self.label_3.setText('Position')
        self.pushButton.setFont(font)
        self.pushButton.setText('Search')


class canting_view(QListWidget, Ui_Form):
    def __init__(self, t_name, mother):
        super().__init__()
        self.font = QFont("宋体", 12)
        self.setupUi(self)
        from global_ import dic_canting_time, dic_canting_position
        self.label.setText('Business hours:\n' + dic_canting_time.get(t_name, ''))
        self.label_3.setText('Position:\n' + dic_canting_position.get(t_name, ''))
        self.mother = mother
        self.t_name = t_name
        self.count_times = 0
        self.food = []
        self.put_items()
        self.hasSet = False
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
