import random
import sys

from PySide6.QtCore import Qt, QLocale, QTimer
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication
from qfluentwidgets import setThemeColor, FluentTranslator, SplitTitleBar
from qframelesswindow import AcrylicWindow

import global_
from .Ui_LoginWindow import Ui_Form


class LoginWindow(AcrylicWindow, Ui_Form):

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        # setTheme(Theme.DARK)
        setThemeColor('#28afe9')
        self.setTitleBar(SplitTitleBar(self))
        self.titleBar.raise_()

        self.label.setScaledContents(False)
        self.setWindowTitle('航味_吃在北航')
        self.setWindowIcon(QIcon(":/images/logo.png"))
        self.resize(900, 650)

        self.windowEffect.setMicaEffect(self.winId(), isDarkMode=False)
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
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        self.pushButton.clicked.connect(self.display)
        quotes = [
            "活着就是为了吃饭，难道还有其他原因吗？",
            "勇气不是没有恐惧，而是能够面对恐惧并战胜它。",
            "想象力比知识更重要，因为知识是有限的，而想象力概括着世界的一切。",
            "你不能选择如何开始你的人生，但你可以选择如何结束。",
            "成功的关键在于始终保持积极的态度。",
            "人生不是等待风暴过去，而是学会在雨中跳舞。",
            "不要问别人做了什么，问问自己可以吃什么。",
            "生活中最大的冒险就是决心去追逐自己的梦想。"
        ]
        quote = random.choice(quotes)
        # 在文本浏览器中展示名言警句
        self.textBrowser.setPlainText("    欢迎您使用美食系统😃😃😃😃😃\n    " + quote)
        self.lineEdit_3.setText("老王")

    def resizeEvent(self, e):
        super().resizeEvent(e)
        pixmap = QPixmap(":/images/background.jpg").scaled(
            self.label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)


    def display(self):
        from global_ import is_all_chinese
        # 利用line Edit控件对象text()函数获取界面输入
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        # 利用text Browser控件对象setText()函数设置界面显示
        from dbconnect import hasuser, getuserdata
        if username == "admin" and password == '123456':
            #self.subman.show()
            pass
        elif username == 'admin':
            self.textBrowser.setText("你的用户名不正确！")
        elif not is_all_chinese(username):
            self.textBrowser.setText("你必须给自己取一个中文名字！")
        elif len(username) < 2:
            self.textBrowser.setText("用户名太短，建议长一点！")
        elif password == '123456':
            self.textBrowser.setText("密码太简单了吧\U0001F609")
        elif len(password) < 6:
            self.textBrowser.setText("密码不安全，试试其他密码吧！")
        elif hasuser(username):
            data = getuserdata(username)
            print(data['mi'])
            print(password)
            if str(data['mi']) == password:
                self.textBrowser.setText("登录成功!\n" + "用户名是: " + username)
                if username == '老王':
                    self.textBrowser.append("\U0001F613")
                from gallery import demo
                global_.name = username
                demo.mainLogic(username, self.app)
                QTimer.singleShot(800, self.close)
            else:
                self.textBrowser.setText("密码错误\U0001F613")
        else:
            self.textBrowser.setText(f"注册成功\U0001F613\n您好！{username}\n密码是 {password}")
            dic = {'name': username, 'mi': password, 'cost': 0.0, 'star': [], 'last': []}
            from dbconnect import zhuce
            zhuce(dic)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Internationalization
    translator = FluentTranslator(QLocale())
    app.installTranslator(translator)

    w = LoginWindow()
    w.show()
    app.exec()