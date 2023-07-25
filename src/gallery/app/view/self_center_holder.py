# coding:utf-8

from .gallery_interface import GalleryInterface
from ..common.translator import Translator


class ViewInterface(GalleryInterface):
    """ View interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title='个人中心',
            subtitle="fix yourself",
            parent=parent
        )
        self.mother = parent
        self.setObjectName('viewInterface')
        from .self_center import self_manage_center
        from global_ import name
        self.center = self_manage_center(name,self)
        self.vBoxLayout.addWidget(self.center)


    def refresh11(self):
        self.center.refresh12()

    def switch_to_food(self, t,d,f):
        self.mother.switch_to_food(f,d,t)
