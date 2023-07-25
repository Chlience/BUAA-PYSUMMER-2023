# coding:utf-8
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCompleter
from qfluentwidgets import LineEdit, SpinBox, DoubleSpinBox, TimeEdit, DateTimeEdit, DateEdit, TextEdit, SearchLineEdit, \
    InfoBadge
from .gallery_interface import GalleryInterface
from ..common.translator import Translator


class TextInterface(GalleryInterface):
    """ Text interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title='管理中心',
            subtitle="crud",
            parent=parent
        )
        self.setObjectName('textInterface')
        from global_ import name
        if name == 'admin':
            from .manage_page import manage_widget
            wid = manage_widget()
            self.vBoxLayout.addWidget(wid)
        else:
            label = InfoBadge()
            label.setText("只有admin管理员能添加、修改、删除 菜品、食堂、档口")
            self.vBoxLayout.addWidget(label)


