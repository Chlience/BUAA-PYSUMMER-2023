# coding:utf-8
from PySide6.QtCore import Qt, QSize, QUrl
from PySide6.QtWidgets import QWidget, QVBoxLayout, QButtonGroup, QHBoxLayout, QGridLayout
from qfluentwidgets import (Action, DropDownPushButton, DropDownToolButton, PushButton, ToolButton, PrimaryPushButton,
                            HyperlinkButton, ComboBox, RadioButton, CheckBox, Slider, SwitchButton, EditableComboBox,
                            ToggleButton, RoundMenu, FluentIcon, SplitPushButton, SplitToolButton, PrimarySplitToolButton,
                            PrimarySplitPushButton, PrimaryDropDownPushButton, PrimaryToolButton, PrimaryDropDownToolButton,
                            ToggleToolButton, TransparentDropDownPushButton, TransparentPushButton, TransparentToggleToolButton,
                            TransparentTogglePushButton, TransparentDropDownToolButton, TransparentToolButton,
                            PillPushButton, PillToolButton)

from .gallery_interface import GalleryInterface
from ..common.translator import Translator


class BasicInputInterface(GalleryInterface):
    """ Basic input interface """

    def __init__(self, parent=None):
        super().__init__(
            title='必吃菜',
            subtitle='must eat！',
            parent=parent
        )
        self.setObjectName('basicInputInterface')
        layout = QGridLayout(self)
        from .must_eat_page import must_eat_form
        from global_ import name
        bottom_widget = must_eat_form(name)
        layout.addWidget(bottom_widget, 1, 0)  # 放置在第 1 行，第 0 列

        # 设置行的伸展因子，让下方部件占据2/3的高度
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 8)



    def createStandMenu(self, button):
        menu = RoundMenu(parent=self)
        menu.addActions([
            Action(self.tr('Star Platinum'), triggered=lambda b=button: b.setText(self.tr('Star Platinum'))),
            Action(self.tr('Crazy Diamond'), triggered=lambda b=button: b.setText(self.tr('Crazy Diamond'))),
            Action(self.tr("Gold Experience"), triggered=lambda b=button: b.setText(self.tr("Gold Experience"))),
            Action(self.tr('Sticky Fingers'), triggered=lambda b=button: b.setText(self.tr('Sticky Fingers'))),
        ])
        return menu