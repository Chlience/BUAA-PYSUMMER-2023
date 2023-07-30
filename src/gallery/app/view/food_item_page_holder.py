# coding:utf-8
from PySide6.QtWidgets import QVBoxLayout

from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from ..common.config import cfg


class Food(GalleryInterface):
    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title="Food",
            subtitle='Do you like it?',
            parent=parent
        )
        self.setObjectName('materialInterface')
        from .food_item_page import food_item
        from global_ import name
        self.food_page = food_item(name)
        layout = QVBoxLayout(self)
        layout.addWidget(self.food_page)
        self.setLayout(layout)

    def change(self, food_name, count_name, house_name):
        from dbconnect import findFood
        result = findFood(house_name, count_name, food_name)
        self.food_page.set_food(result[0])
