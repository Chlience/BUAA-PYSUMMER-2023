# coding: utf-8
from typing import List, Union
from PySide6.QtCore import Qt, Signal, QEasingCurve, QUrl, QSize
from PySide6.QtGui import QIcon, QDesktopServices, QPixmap
from PySide6.QtWidgets import QApplication, QHBoxLayout, QFrame, QWidget

from qfluentwidgets import NavigationAvatarWidget, NavigationItemPosition, MessageBox, FluentWindow, SplashScreen, \
    qrouter, FluentIconBase, NavigationTreeWidget
from qfluentwidgets import FluentIcon as FIF

from .gallery_interface import GalleryInterface
from .home_page import HomePage
from .must_eat_page_holder import MustEat
from .recommend import Recommend
from .layout_interface import Explore
from .search_food_holder import Search
from .food_item_page_holder import Food
from .manager_page_holder import TextInterface
from .self_center_holder import ViewInterface
from ..common.config import SUPPORT_URL
from ..common.icon import Icon
from ..common.signal_bus import signalBus
from ..common.translator import Translator
from ..common import resource
from gallery.app.view.cafeteria import Cafeteria

type(resource)


class MainWindow(FluentWindow):
    def __init__(self, name):
        super().__init__()
        self.initWindow()
        self.user_name = name
        # create sub interface
        self.home_page = HomePage(self)
        self.search = Search(self)
        self.must_eat = MustEat(self)
        self.recommend = Recommend(self)
        self.explore = Explore(self)
        self.canteen = Cafeteria(self)
        self.food = Food(self)
        self.manage = TextInterface(self)
        self.personal_home = ViewInterface(self)

        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()
        self.splashScreen.finish()

    def initLayout(self):
        signalBus.switchToSampleCard.connect(self.switchToSample)
        signalBus.supportSignal.connect(self.onSupport)

    def initNavigation(self):
        # add navigation items
        t = Translator()
        self.addSubInterface(self.home_page, FIF.HOME, "Home")
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.search, Icon.EMOJI_TAB_SYMBOLS, "Search")
        # pos = NavigationItemPosition.SCROLL
        self.addSubInterface(self.must_eat, FIF.CHECKBOX, "MustEat")
        self.addSubInterface(self.recommend, FIF.MESSAGE, "Recommend")
        self.addSubInterface(self.explore, FIF.LAYOUT, "Explore")
        # 目前应该是隐藏状态
        self.addSubInterface(self.canteen, FIF.DATE_TIME, "Canteen")
        self.addSubInterface(self.food, FIF.PALETTE, "Food")
        self.addSubInterface(self.manage, Icon.TEXT, "manage", NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.personal_home, Icon.GRID, "Personal Home", NavigationItemPosition.BOTTOM)
        # self.addSubInterface(
        #     self.settingInterface, FIF.SETTING, self.tr('Settings'), NavigationItemPosition.BOTTOM)

    def addSubInterface(self, interface: QWidget, icon: Union[FluentIconBase, QIcon, str], text: str,
                        position=NavigationItemPosition.TOP, parent=None) -> NavigationTreeWidget:
        if not interface.objectName():
            raise ValueError("The object name of `interface` can't be empty string.")
        if parent and not parent.objectName():
            raise ValueError("The object name of `parent` can't be empty string.")

        self.stackedWidget.addWidget(interface)

        # add navigation item
        routeKey = interface.objectName()
        item = None
        if interface != self.food:
            from global_ import name
            if not (interface == self.manage and name != 'admin'):
                item = self.navigationInterface.addItem(
                    routeKey=routeKey,
                    icon=icon,
                    text=text,
                    onClick=lambda: self.refresh12(interface),
                    position=position,
                    tooltip=text,
                    parentRouteKey=parent.objectName() if parent else None
                )

        # initialize selected item
        if self.stackedWidget.count() == 1:
            self.stackedWidget.currentChanged.connect(self._onCurrentInterfaceChanged)
            self.navigationInterface.setCurrentItem(routeKey)
            qrouter.setDefaultRouteKey(self.stackedWidget, routeKey)

        return item

    def refresh12(self, inter):
        self.switchTo(inter)
        if hasattr(inter, 'refresh11') and callable(inter.refresh11):
            inter.refresh11()

    def initWindow(self):
        self.resize(1000, 900)
        self.setMinimumWidth(660)
        self.setWindowIcon(QIcon('gallery/app/resource/images/logo.png'))
        self.setWindowTitle('Hangeat')

        # create splash screen
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()

    def onSupport(self):
        w = MessageBox(
            '喜欢我们航味系统吗',
            '🚀🚀🚀🚀🚀🚀',
            self
        )
        w.yesButton.setText('喜欢捏')
        w.cancelButton.setText('差不多得了')
        if w.exec():
            QDesktopServices.openUrl(QUrl(SUPPORT_URL))

    def switchToSample(self, routeKey, index):
        """ switch to sample """
        interfaces = self.findChildren(GalleryInterface)
        for w in interfaces:
            if w.objectName() == "dateTimeInterface":
                self.stackedWidget.setCurrentWidget(w, False)
                dic = {1: '学二', 2: '合一', 3: '新北', 4: 'Wings', 5: '美食苑'}
                w.change(dic[int(index)])
                # w.scrollToCard(index)

    def switch_to_food(self, food_name, count_name, house_name):
        interfaces = self.findChildren(GalleryInterface)
        for w in interfaces:
            if w.objectName() == "materialInterface":
                self.stackedWidget.setCurrentWidget(w, False)
                w.change(food_name, count_name, house_name)
                # self.parent.switch_to_food(food_name, count_name, house_name)

    def goto_sub(self, t):
        interfaces = self.findChildren(GalleryInterface)
        for w in interfaces:
            if w.objectName() == "layoutInterface":
                self.stackedWidget.setCurrentWidget(w, False)
                w.set_t(t)
