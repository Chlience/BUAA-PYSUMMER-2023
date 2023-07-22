# coding:utf-8
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QTreeWidgetItem, QHBoxLayout, QTreeWidgetItemIterator, QTableWidgetItem, \
    QListWidgetItem, QGridLayout
from qfluentwidgets import TreeWidget, TableWidget, ListWidget

from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from ..common.style_sheet import StyleSheet


class ViewInterface(GalleryInterface):
    """ View interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title='个人中心',
            subtitle="fix yourself",
            parent=parent
        )
        self.setObjectName('viewInterface')
        layout = QGridLayout(self)
        from .self_center import subzx
        from global_ import name
        self.center = subzx(name,self)
        layout.addWidget(self.center, 1, 0)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 5)
        self.setLayout(layout)

    def refresh11(self):
        self.center.refresh12()
