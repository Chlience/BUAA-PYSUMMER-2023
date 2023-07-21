# coding:utf-8
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QGridLayout
from qfluentwidgets import DatePicker, TimePicker, AMTimePicker, ZhDatePicker, CalendarPicker

from .gallery_interface import GalleryInterface, ToolBar
from ..common.translator import Translator


class DateTimeInterface(GalleryInterface):
    """ Date time interface """

    def __init__(self, parent=None):
        self.title = ''
        t = Translator()
        super().__init__(
            title='某食堂',
            subtitle='点击主页图标直达特定食堂',
            parent=parent
        )
        self.setObjectName('dateTimeInterface')
        self.layout = QGridLayout(self)
        from global_ import name
        from .common_food_page import canting_view
        self.widget = canting_view(name, "肯德基？")
        self.layout.addWidget(self.widget, 1, 0)
        self.layout.layout()
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 5)

    def change(self, canting_name):
        self.title = canting_name
        self.toolBar.changeTitle(canting_name)
        self.layout.removeWidget(self.widget)
        self.widget.deleteLater()
        from global_ import name
        from .common_food_page import canting_view
        self.widget = canting_view(name, canting_name)
        self.layout.addWidget(self.widget)
        self.layout.layout()




