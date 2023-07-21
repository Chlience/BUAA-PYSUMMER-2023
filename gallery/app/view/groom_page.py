# coding:utf-8
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QGridLayout

from qfluentwidgets import (PushButton, Dialog, MessageBox, ColorDialog, TeachingTip, TeachingTipTailPosition,
                            InfoBarIcon, Flyout, FlyoutView, TeachingTipView, FlyoutAnimationType)
from ..common.translator import Translator
from .gallery_interface import GalleryInterface


class DialogInterface(GalleryInterface):
    """ Dialog interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title='智能推荐',
            subtitle='快来试试吧',
            parent=parent
        )
        self.setObjectName('dialogInterface')
        layout = QGridLayout(self)
        from .groom_base import groom_page
        from global_ import name
        self.groom = groom_page(name)
        layout.addWidget(self.groom, 1, 0)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 5)
        self.setLayout(layout)

    def refresh11(self):
        self.groom.refresh12()
        print('tuijian gengxinleshuju!!!!')



