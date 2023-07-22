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
        self.trie = Trie()
        self.hBoxLayout = QHBoxLayout(self)
        from global_ import name
        from .common_food_page import food_list_view
        self.hBoxLayout.addWidget(food_list_view(name))
        self.hBoxLayout.layout()


class IconInterface(GalleryInterface):
    """ Icon interface """

    def __init__(self, parent=None):
        # focu = Translator()
        super().__init__(
            title="搜索",  # focu.icons,
            subtitle="hangeat.cn",
            #parent=parent
        )
        self.setObjectName('searchInterface')

        self.iconView = IconCardView(self)
        self.vBoxLayout.addWidget(self.iconView)
