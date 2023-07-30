# coding:utf-8

from PySide6.QtWidgets import QWidget, QHBoxLayout

from gallery.app.view.gallery_interface import GalleryInterface
from gallery.app.common.trie import Trie
from gallery.app.view.common_food_page import SimpleSearchView

class IconCardView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.trie = Trie()
        self.hBoxLayout = QHBoxLayout(self)
        from global_ import name

        self.hBoxLayout.addWidget(SimpleSearchView(name, self))
        self.hBoxLayout.layout()

    def switch_to_food(self, food_name, count_name, house_name):
        self.parent.switch_to_food(food_name, count_name, house_name)


class Search(GalleryInterface):
    def __init__(self, parent=None):
        self.parent = parent
        super().__init__(
            title="Search",
            subtitle="Search for your favorite food."
        )
        self.setObjectName('searchInterface')
        self.iconView = IconCardView(self)
        self.vBoxLayout.addWidget(self.iconView)

    # 奇妙的切换到菜品页面的功能
    def switch_to_food(self, food_name, count_name, house_name):
        self.parent.switch_to_food(food_name, count_name, house_name)
