# controller.py

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableView, QVBoxLayout, QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # 連接視圖的按鈕到控制器的槽
        self.view.button.clicked.connect(self.increment_count)

    def increment_count(self):
        # 更新模型的數據
        self.model.increment()
        # 更新視圖
        self.view.update_label(self.model.get_count())
