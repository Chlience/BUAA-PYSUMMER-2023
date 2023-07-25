# coding:utf-8
from typing import List

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel, QWidget, QHBoxLayout
from qfluentwidgets import (FluentIcon, IconWidget, FlowLayout, isDarkTheme,
                            Theme, applyThemeColor, SmoothScrollArea, SearchLineEdit, StrongBodyLabel,
                            BodyLabel)

from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from ..common.config import cfg
from ..common.style_sheet import StyleSheet
from ..common.trie import Trie
class IconCardView(QWidget):
    """ Icon card view """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.trie = Trie()
        self.hBoxLayout = QHBoxLayout(self)
        from global_ import name
        from .common_food_page import simple_search_view
        self.hBoxLayout.addWidget(simple_search_view(name, self))
        self.hBoxLayout.layout()
    def switch_to_food(self, food_name, count_name, house_name):
        self.parent.switch_to_food(food_name, count_name, house_name)
        pass


class IconInterface(GalleryInterface):
    """ Icon interface """

    def __init__(self, parent=None):
        self.parent = parent
        # focu = Translator()
        super().__init__(
            title="搜索",  # focu.icons,
            subtitle="hangeat.cn",
            #parent=parent
        )
        self.setObjectName('searchInterface')

        self.iconView = IconCardView(self)
        self.vBoxLayout.addWidget(self.iconView)
    def switch_to_food(self, food_name, count_name, house_name):
        self.parent.switch_to_food(food_name, count_name, house_name)
