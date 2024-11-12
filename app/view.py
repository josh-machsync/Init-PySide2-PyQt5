# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
# from PyQt5.QtGui import QStandardItemModel  # 用於創建表格模型
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from app.qt_designer import Ui_Dialog  # 匯入生成的 UI 類
from . import logger  # 從同一個包導入 logger


class View(QWidget, Ui_Dialog):
    def __init__(self):
        logger.debug("Initializing View")
        super().__init__()
        self.setupUi(self)  # 初始化 UI 元素

    def update_label(self, count):
        self.label.setText(f"Count: {count}")