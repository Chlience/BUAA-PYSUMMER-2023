import random
import sys

from PySide6.QtCore import Qt, QLocale, QTimer
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication
from qfluentwidgets import setThemeColor, FluentTranslator, SplitTitleBar, Dialog, InfoBarIcon, InfoBar, PushButton, \
    InfoBarPosition
from qframelesswindow import AcrylicWindow

import global_
from .Ui_LoginWindow import Ui_Form
from src.login import user_check


class LoginWindow(AcrylicWindow, Ui_Form):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        # setTheme(Theme.DARK)
        setThemeColor('#28afe9')

        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.app = app
        self.label.setScaledContents(False)
        self.setWindowTitle('HangEat')
        self.setWindowIcon(QIcon(":/images/logo.png"))
        self.resize(1000, 650)

        # self.windowEffect.setMicaEffect(self.winId(), isDarkMode=False)
        self.titleBar.titleLabel.setStyleSheet("""
            QLabel{
                background: transparent;
                font: 13px 'Segoe UI';
                padding: 0 4px;
                color: white
            }
        """)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap(":/images/background.jpg").scaled(
            self.label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)

    def createErrorInfoBar(self, title, content):
        w = InfoBar.error(
            title=title,
            content=content,
            orient=Qt.Vertical,  # vertical layout
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=4000,
            parent=self
        )
        w.show()

    def createInfoInfoBar(self, title, content):
        w = InfoBar.info(
            title=title,
            content=content,
            orient=Qt.Vertical,  # vertical layout
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=4000,
            parent=self
        )
        w.show()

    def login(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        from dbconnect import hasuser, getuserdata
        if user_check.username_check(username) is False:
            self.createErrorInfoBar("Login Error", user_check.username_error_message())
        elif user_check.password_check(password) is False:
            self.createErrorInfoBar("Login Error", user_check.password_error_message())
        elif hasuser(username):
            data = getuserdata(username)
            print(password)
            if str(data['password']) == password:
                from gallery import demo
                global_.name = username
                demo.mainLogic(username, self.app)
                QTimer.singleShot(800, self.close)
            else:
                self.createErrorInfoBar("Login Error", "Username or password incorrect")
        else:
            self.createErrorInfoBar("Login Error", "Username or password incorrect")

    def register(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        from dbconnect import hasuser, getuserdata
        if user_check.username_check(username) is False:
            self.createErrorInfoBar("Register Error", user_check.username_error_message())
        elif user_check.password_check(password) is False:
            self.createErrorInfoBar("Register Error", user_check.password_error_message())
        elif hasuser(username):
            self.createErrorInfoBar("Register Error", "Username has been used.")
        else:
            dic = {'username': username, 'password': password, 'cost': 0.0, 'star': [], 'last': []}
            from dbconnect import zhuce
            zhuce(dic)
            self.createInfoInfoBar("Register Success", "Now you can login.")