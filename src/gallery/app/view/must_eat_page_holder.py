# coding:utf-8
from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QGridLayout
from qfluentwidgets import (Action, RoundMenu)

from .gallery_interface import GalleryInterface


from ..common.translator import Translator


class MustEat(GalleryInterface):
    """ Basic input interface """

    def __init__(self, parent=None):
        self.mother = parent
        super().__init__(
            title='Must eat',
            subtitle='It would be a pity if we missed it',
            parent=parent
        )
        self.setObjectName('basicInputInterface')
        layout = QGridLayout(self)
        from .must_eat_page import must_eat_form
        from global_ import name
        self.bottom_widget = must_eat_form(name, self)
        layout.addWidget(self.bottom_widget, 1, 0)  # 放置在第 1 行，第 0 列

        # 设置行的伸展因子，让下方部件占据2/3的高度
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 8)

    def refresh11(self):
        self.bottom_widget.refresh()
        print('refresh!!!')

    def createStandMenu(self, button):
        menu = RoundMenu(parent=self)
        menu.addActions([
            Action(self.tr('Star Platinum'), triggered=lambda b=button: b.setText(self.tr('Star Platinum'))),
            Action(self.tr('Crazy Diamond'), triggered=lambda b=button: b.setText(self.tr('Crazy Diamond'))),
            Action(self.tr("Gold Experience"), triggered=lambda b=button: b.setText(self.tr("Gold Experience"))),
            Action(self.tr('Sticky Fingers'), triggered=lambda b=button: b.setText(self.tr('Sticky Fingers'))),
        ])
        return menu

    def switch_to_food(self, t,d,f):
        self.mother.switch_to_food(f,d,t)