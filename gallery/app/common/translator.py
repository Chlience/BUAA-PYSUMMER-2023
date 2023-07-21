# coding: utf-8
from PySide6.QtCore import QObject


class Translator(QObject):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.text = self.tr('Text')
        self.view = self.tr('View')
        self.menus = self.tr('Menus & toolbars')
        self.icons = self.tr('搜索')
        self.layout = self.tr('档口')
        self.dialogs = self.tr('推荐')
        self.scroll = self.tr('Scrolling')
        self.material = self.tr('Material')
        self.dateTime = self.tr('食堂')
        self.navigation = self.tr('Navigation')
        self.basicInput = self.tr('必吃')
        self.statusInfo = self.tr('Status & info')