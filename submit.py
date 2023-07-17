from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QListWidget, QMenu
from PySide6.QtWidgets import QVBoxLayout, QTextEdit, QPushButton, QWidget

import global1


class wid(QWidget):
    def __init__(self, name="老王", food="？"):
        super().__init__()
        self.food = food
        self.setWindowTitle("评论窗口")
        self.t = False
        self.load_comments_from_file()  # 从文件加载评论

        self.comment_textedit = QTextEdit()
        self.submit_button = QPushButton("提交评论")
        self.submit_button.clicked.connect(self.submit_comment)
        self.name = name
        self.comment_list = QListWidget()  # 新增的评论列表
        self.comment_list.itemClicked.connect(self.select_comment)
        self.comment_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.comment_list.customContextMenuRequested.connect(self.show_menu)
        self.create_actions()
        self.create_menu()
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.comment_textedit)
        vlayout.addWidget(self.submit_button)
        vlayout.addWidget(self.comment_list)
        self.but = QPushButton("Button", self)
        self.but.setText("确定修改？")
        self.but.setVisible(False)  # 初始状态隐藏按钮
        vlayout.addWidget(self.but)
        vlayout.addLayout(vlayout)
        # 设置comment_textedit的高度为comment_list的一半
        vlayout.setStretchFactor(self.comment_textedit, 1)
        vlayout.setStretchFactor(self.comment_list, 2)

        self.setLayout(vlayout)
        self.update_comments()  # 更新评论列表显示

    def submit_comment(self):
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
        self.update_comments()  # 更新评论列表显示
        self.comment_textedit.clear()

    def select_comment(self):
        if self.t == False:
            self.comment_textedit.setFocus()
            self.t = True
        else:
            self.comment_list.setCurrentItem(None)
            self.t = False

    def update_comments(self):
        # 更新评论列表
        self.comment_list.clear()
        for comment in self.comments:
            self.comment_list.addItem(comment)

    def load_comments_from_file(self):
        for i in global1.Data2:
            if i['name'] == self.food:
                self.comments = i.get('comment', [])

    def save_comments_to_file(self):
        my_list = []
        for i in range(self.comment_list.count()):
            item = self.comment_list.item(i)
            my_list.append(item.text())
        self.comments = my_list
        for i in range(len(global1.Data2)):
            if global1.Data2[i]['name'] == self.food:
                global1.Data2[i]['comment'] = self.comments

    def create_actions(self):
        self.action_modify = QAction("修改", self)
        self.action_delete = QAction("删除", self)

        self.action_modify.triggered.connect(self.modify_item)
        self.action_delete.triggered.connect(self.delete_item)

    def create_menu(self):
        self.context_menu = QMenu(self)
        self.context_menu.addAction(self.action_modify)
        self.context_menu.addAction(self.action_delete)

    def show_menu(self, position):
        index = self.comment_list.indexAt(position)
        if index.isValid():
            self.context_menu.exec_(self.comment_list.viewport().mapToGlobal(position))

    def modify_item(self):
        item = self.comment_list.currentItem()
        self.comment_textedit.setText(item.text())
        self.but.setVisible(True)
        self.but.clicked.connect(lambda: self.doit(item))

        # 处理修改项的逻辑

    def doit(self, item):
        item.setText(self.comment_textedit.toPlainText())
        self.but.setVisible(False)

    def delete_item(self):
        item = self.comment_list.currentItem()
        row = self.comment_list.row(item)
        self.comment_list.takeItem(row)
        # 处理删除项的逻辑
