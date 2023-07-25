# coding:utf-8
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QGridLayout
from qfluentwidgets import DatePicker, TimePicker, AMTimePicker, ZhDatePicker, CalendarPicker

from .gallery_interface import GalleryInterface, ToolBar
from ..common.translator import Translator


class DateTimeInterface(GalleryInterface):
    """ Date time interface """

    def __init__(self, parent=None):
        self.parent = parent
        self.title = ''
        t = Translator()
        super().__init__(
            title='某食堂',
            subtitle='点击主页图标直达特定食堂',
            parent=parent
        )
        self.setObjectName('dateTimeInterface')
        from .new_canting_page import canting_view
        self.widget = canting_view('', self)
        self.vBoxLayout.addWidget(self.widget)

    def change(self, canting_name):
        self.title = canting_name
        self.toolBar.changeTitle(canting_name)
        self.vBoxLayout.removeWidget(self.widget)
        self.widget.deleteLater()
        from .new_canting_page import canting_view
        self.widget = canting_view(canting_name, self)
        self.vBoxLayout.addWidget(self.widget)

    def switch_to_food(self, food_name, count_name, house_name):
        self.parent.switch_to_food(food_name, count_name, house_name)

    def goto_sub(self, t):
        self.parent.goto_sub(t)





