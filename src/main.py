from PySide6.QtCore import QLocale
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator

from login.demo import LoginWindow
import dbconnect
if __name__ == '__main__':
    app = QApplication([])

    # Internationalization
    translator = FluentTranslator(QLocale())
    app.installTranslator(translator)
    w = LoginWindow(app)
    w.show()
    app.exec()
