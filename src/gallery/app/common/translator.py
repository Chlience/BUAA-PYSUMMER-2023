# coding: utf-8
from PySide6.QtCore import QObject


class Translator(QObject):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.text = self.tr('管理中心')
        self.view = self.tr('个人中心')
        self.menus = self.tr('待定')
        self.icons = self.tr('搜索')
        self.layout = self.tr('档口')
        self.dialogs = self.tr('推荐')
        self.scroll = self.tr('待定2')
        self.material = self.tr('菜品')
        self.dateTime = self.tr('食堂')
        self.navigation = self.tr('待定3')
        self.basicInput = self.tr('必吃')
        self.statusInfo = self.tr('待定4')