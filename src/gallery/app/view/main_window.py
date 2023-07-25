# coding: utf-8
from typing import List, Union
from PySide6.QtCore import Qt, Signal, QEasingCurve, QUrl, QSize
from PySide6.QtGui import QIcon, QDesktopServices, QPixmap
from PySide6.QtWidgets import QApplication, QHBoxLayout, QFrame, QWidget

from qfluentwidgets import NavigationAvatarWidget, NavigationItemPosition, MessageBox, FluentWindow, SplashScreen, \
    qrouter, FluentIconBase, NavigationTreeWidget
from qfluentwidgets import FluentIcon as FIF

from .gallery_interface import GalleryInterface
from .home_page import HomeInterface
from .must_eat_page_holder import BasicInputInterface
from .canting_page_holder import DateTimeInterface
from .groom_page import DialogInterface
from .layout_interface import LayoutInterface
from .search_food_holder import IconInterface
from .food_item_page_holder import MaterialInterface
from .menu_interface import MenuInterface
from .navigation_view_interface import NavigationViewInterface
from .scroll_interface import ScrollInterface
from .status_info_interface import StatusInfoInterface
from .setting_interface import SettingInterface
from .manager_page_holder import TextInterface
from .self_center_holder import ViewInterface
from ..common.config import SUPPORT_URL
from ..common.icon import Icon
from ..common.signal_bus import signalBus
from ..common.translator import Translator
from ..common import resource

type(resource)


class MainWindow(FluentWindow):

    def __init__(self, name):
        super().__init__()
        self.initWindow()
        self.user_name = name
        # create sub interface
        self.homeInterface = HomeInterface(self)
        self.iconInterface = IconInterface(self)
        self.basicInputInterface = BasicInputInterface(self)
        self.dateTimeInterface = DateTimeInterface(self)
        self.dialogInterface = DialogInterface(self)
        self.layoutInterface = LayoutInterface(self)
        self.menuInterface = MenuInterface(self)
        self.materialInterface = MaterialInterface(self)
        self.navigationViewInterface = NavigationViewInterface(self)
        self.scrollInterface = ScrollInterface(self)
        self.statusInfoInterface = StatusInfoInterface(self)
        self.settingInterface = SettingInterface(self)
        self.textInterface = TextInterface(self)
        self.viewInterface = ViewInterface(self)

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
        self.addSubInterface(self.homeInterface, FIF.HOME, self.tr('Home'))
        self.addSubInterface(self.iconInterface, Icon.EMOJI_TAB_SYMBOLS, t.icons)
        self.navigationInterface.addSeparator()
        pos = NavigationItemPosition.SCROLL
        self.addSubInterface(self.basicInputInterface, FIF.CHECKBOX, t.basicInput, pos)
        self.addSubInterface(self.dateTimeInterface, FIF.DATE_TIME, t.dateTime, pos)
        self.addSubInterface(self.dialogInterface, FIF.MESSAGE, t.dialogs, pos)
        self.addSubInterface(self.layoutInterface, FIF.LAYOUT, t.layout, pos)
        self.addSubInterface(self.materialInterface, FIF.PALETTE, t.material, pos)
        self.addSubInterface(self.menuInterface, Icon.MENU, t.menus, pos)
        self.addSubInterface(self.navigationViewInterface, FIF.MENU, t.navigation, pos)
        self.addSubInterface(self.scrollInterface, FIF.SCROLL, t.scroll, pos)
        self.addSubInterface(self.statusInfoInterface, FIF.CHAT, t.statusInfo, pos)
        self.addSubInterface(self.textInterface, Icon.TEXT, t.text, pos)
        self.addSubInterface(self.viewInterface, Icon.GRID, t.view, pos)
        pixmap = QPixmap("gallery/app/resource/images/logoo.png")
        if pixmap.isNull():
            print("无法创建 QPixmap 对象")
        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('', pixmap),
            onClick=self.onSupport,
            position=NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(
            self.settingInterface, FIF.SETTING, self.tr('Settings'), NavigationItemPosition.BOTTOM)

    def addSubInterface(self, interface: QWidget, icon: Union[FluentIconBase, QIcon, str], text: str,
                        position=NavigationItemPosition.TOP, parent=None) -> NavigationTreeWidget:
        """ add sub interface, the object name of `interface` should be set already
        before calling this method

        Parameters
        ----------
        interface: QWidget
            the subinterface to be added

        icon: FluentIconBase | QIcon | str
            the icon of navigation item

        text: str
            the text of navigation item

        position: NavigationItemPosition
            the position of navigation item

        parent: QWidget
            the parent of navigation item
        """
        if not interface.objectName():
            raise ValueError("The object name of `interface` can't be empty string.")
        if parent and not parent.objectName():
            raise ValueError("The object name of `parent` can't be empty string.")

        self.stackedWidget.addWidget(interface)

        # add navigation item
        routeKey = interface.objectName()
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
        self.setWindowIcon(QIcon('gallery/app/resource/images/logoo.png'))
        self.setWindowTitle('航味__吃在北航')

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
                #self.parent.switch_to_food(food_name, count_name, house_name)

    def goto_sub(self, t):
        interfaces = self.findChildren(GalleryInterface)
        for w in interfaces:
            if w.objectName() == "layoutInterface":
                self.stackedWidget.setCurrentWidget(w, False)
                w.set_t(t)
