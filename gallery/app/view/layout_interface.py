# coding:utf-8
from PySide6.QtWidgets import QWidget, QGridLayout
from qfluentwidgets import FlowLayout, PushButton

from .gallery_interface import GalleryInterface
from ..common.translator import Translator


class LayoutInterface(GalleryInterface):
    """ Layout interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title='分档口食堂',
            subtitle="更加细致的服务",
            parent=parent
        )
        self.setObjectName('layoutInterface')
        self.layout = QGridLayout(self)
        from global_ import name
        from .counter_select_page import counter_list_holder
        self.widget = counter_list_holder("肯德基？", name)
        self.layout.addWidget(self.widget, 1, 0)
        self.layout.layout()
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 5)



