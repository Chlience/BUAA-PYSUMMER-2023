from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import QListWidget, QMenu
from PySide6.QtWidgets import QVBoxLayout, QTextEdit, QPushButton, QWidget
from qfluentwidgets import TextEdit, PushButton, ListWidget


class comment_window(QWidget):
    def __init__(self, name="老王", food="？", count="", house=""):
        super().__init__()
        self.food = food
        self.count = count
        self.house = house
        self.focu = False
        self.load_comments()  # 加载评论
        self.comment_textedit = TextEdit()
        self.submit_button = PushButton("提交评论")
        font = QFont()
        font.setBold(True)  # 设置字体为粗体
        font.setPointSize(12)  # 设置字体大小
        self.submit_button.setFont(font)
        self.submit_button.clicked.connect(self.submit_comment)
        self.name = name
        self.comment_list = ListWidget()  # 新增的评论列表
        self.comment_list.itemClicked.connect(self.select_comment)
        self.comment_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.comment_list.customContextMenuRequested.connect(self.show_menu)
        self.create_actions()
        self.create_menu()
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.comment_textedit)
        vlayout.addWidget(self.submit_button)
        self.submit_button.setFixedWidth(0.4*self.width())
        vlayout.addWidget(self.comment_list)
        vlayout.addLayout(vlayout)
        vlayout.setStretchFactor(self.comment_textedit, 1)
        vlayout.setStretchFactor(self.comment_list, 2)
        self.setLayout(vlayout)

    def submit_comment(self):
        if self.food == '':
            return
        comment = self.comment_textedit.toPlainText().replace("\t", " ")
        selected_item = self.comment_list.currentItem()
        if selected_item is not None:
            selected_comment = selected_item.text()
            index = selected_comment.index("\x1d")
            andex = selected_comment.index(":")
            username = selected_comment[andex:index]
            current_time = datetime.now().strftime("(%m-%d)%Hh%Mm")  # 获取当前时间
            trimmed_string = selected_comment.strip()
            last_space_index = trimmed_string.rfind(":")
            cas = trimmed_string[last_space_index + 1:]
            cas = cas[:min(len(trimmed_string) - 1, 5)] + "..."
            full_comment = f"{current_time}\x1d{self.name}回复{username} {cas}:{comment}"
        else:
            comment.replace("\x1d", "")
            full_comment = f"{datetime.now().strftime('(%m-%d)%Hh%Mm')}\x1d{self.name}:{comment}"  # 整体评论内容，包含时间
        print("提交评论:", full_comment)
        self.comments.insert(0, full_comment)  # 在列表开头添加新评论
        self.comment_list.addItem(full_comment)
        self.comment_textedit.clear()
        from dbconnect import savecomments
        savecomments(self.house, self.count, self.food, self.comments)
        self.comments = []

    def select_comment(self):
        if self.food == '':
            return
        if self.focu == False:
            self.comment_textedit.setFocus()
            self.focu = True
        else:
            self.comment_list.setCurrentItem(None)
            self.focu = False

    def load_comments(self):
        if self.food == '':
            return
        from dbconnect import loadcomment
        self.comments = loadcomment(self.house, self.count, self.food)
        for text in self.comments:
            self.comment_list.addItem(text)
        self.comments = []

    def create_actions(self):
        self.action_delete = QAction("删除", self)
        self.action_delete.triggered.connect(self.delete_item)

    def create_menu(self):
        self.context_menu = QMenu(self)
        self.context_menu.addAction(self.action_delete)

    def show_menu(self, position):
        index = self.comment_list.indexAt(position)
        if index.isValid():
            self.context_menu.exec_(self.comment_list.viewport().mapToGlobal(position))

    def delete_item(self):
        from dbconnect import del_comment
        del_comment(self.house, self.count, self.food, self.comment_list.currentItem().text())
        item = self.comment_list.currentItem()
        row = self.comment_list.row(item)
        self.comment_list.takeItem(row)

    def checkout(self, username, foodname, countname, housename):
        self.comment_list.clear()
        self.comments = []
        self.food = foodname
        self.count = countname
        self.house = housename
        self.name = username
        self.load_comments()
