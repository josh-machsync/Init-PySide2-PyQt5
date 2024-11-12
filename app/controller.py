# controller.py

import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from . import logger  # 從同一個包導入 logger

class Controller:
    def __init__(self, model, view):
        logger.debug("Initializing Controller")
        self.model = model
        self.view = view

        # 連接視圖的按鈕到控制器的槽
        self.view.pushButton.clicked.connect(self.increment_count)

    def increment_count(self):
        # 更新模型的數據
        self.model.increment()
        # 更新視圖
        self.view.update_label(self.model.get_count())
