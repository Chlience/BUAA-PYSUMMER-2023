# coding:utf-8
import json

from PySide6.QtCore import Qt, Signal, QRectF
from PySide6.QtGui import QPixmap, QPainter, QColor, QBrush, QPainterPath
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from qfluentwidgets import ScrollArea, isDarkTheme, FluentIcon
from ..common.config import cfg, HELP_URL, REPO_URL, EXAMPLE_URL, FEEDBACK_URL
from ..common.icon import Icon, FluentIconBase
from ..components.link_card import LinkCardView
from ..components.sample_card import SampleCardView
from ..common.style_sheet import StyleSheet


class BannerWidget(QWidget):
    """ Banner widget """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(336)

        self.vBoxLayout = QVBoxLayout(self)
        self.galleryLabel = QLabel('Hang__Eat!!!', self)
        self.banner = QPixmap(':/gallery/images/chidanta.jpg')
        self.banner = QPixmap(':/gallery/images/kunkun.png')
        self.linkCardView = LinkCardView(self)

        self.galleryLabel.setObjectName('galleryLabel')

        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(0, 20, 0, 0)
        self.vBoxLayout.addWidget(self.galleryLabel)
        self.vBoxLayout.addWidget(self.linkCardView, 1, Qt.AlignBottom)
        self.vBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.linkCardView.addCard(
            ':/gallery/images/kunkun.png',
            self.tr('造就完了！开造'),
            self.tr("please eat in hang with this app's help"),
            None
        )

        self.linkCardView.addCard(
            FluentIcon.GITHUB,
            self.tr('GitHub repo'),
            self.tr(
                'Get our source code and development process on this github site'),
            REPO_URL
        )

        self.linkCardView.addCard(
            ':/gallery/images/shoko.png',
            self.tr('Food samples'),
            self.tr(
                'Find samples that you can eat more.'),
            EXAMPLE_URL
        )

        self.linkCardView.addCard(
            FluentIcon.FEEDBACK,
            self.tr('Send feedback'),
            self.tr('Help us improve HangEat by providing feedback.'),
            FEEDBACK_URL
        )

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform | QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        w, h = self.width(), 200
        path.addRoundedRect(QRectF(0, 0, w, h), 10, 10)
        path.addRect(QRectF(0, h-50, 50, 50))
        path.addRect(QRectF(w-50, 0, 50, 50))
        path.addRect(QRectF(w-50, h-50, 50, 50))
        path = path.simplified()

        # draw background color
        if not isDarkTheme():
            painter.fillPath(path, QColor(206, 216, 228))
        else:
            painter.fillPath(path, QColor(0, 0, 0))

        # draw banner image
        pixmap = self.banner.scaled(
            self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        path.addRect(QRectF(0, h, w, self.height() - h))
        painter.fillPath(path, QBrush(pixmap))


class HomeInterface(ScrollArea):
    """ Home interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.banner = BannerWidget(self)
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)

        self.__initWidget()
        self.loadSamples()

    def __initWidget(self):
        self.view.setObjectName('view')
        self.setObjectName('homeInterface')
        StyleSheet.HOME_INTERFACE.apply(self)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 36)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.addWidget(self.banner)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

    def loadSamples(self):
        """ load samples """
        # basic input samples
        basicInputView = SampleCardView(
            self.tr("选择你喜欢的食堂"), self.view)
        b1 = basicInputView.addSampleCard(
            icon=":/gallery/images/controls/Button.png",
            title="学二",
            content=self.tr(
                "实惠方便"),
            routeKey="date_time_interface",
            index=1
        )
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/Checkbox.png",
            title="合一",
            content=self.tr("品种多样"),
            routeKey="DateTimeInterface",
            index=2
        )
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/ComboBox.png",
            title="新北",
            content=self.tr(
                "最新建成的食堂"),
            routeKey="DateTimeInterface",
            index=3
        )
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/DropDownButton.png",
            title="Wings",
            content=self.tr(
                "空调很凉快"),
            routeKey="DateTimeInterface",
            index=4
        )
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/HyperlinkButton.png",
            title="美食苑",
            content=self.tr(
                "据说半数北航人没去过"),
            routeKey="DateTimeInterface",
            index=5
        )
        self.vBoxLayout.addWidget(basicInputView)

