from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
# from qt_designer import Ui_Dialog  # 匯入生成的 UI 類
from PyQt5.QtGui import QStandardItemModel  # 用於創建表格模型
import sys
from PyQt5 import QtCore

class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter MVC Demo")
        self.setMinimumSize(300, 200)
        
        # 設置 UI 結構
        self.label = QLabel("Count: 0", self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button = QPushButton("Increment", self)

        # 添加布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        # 使用 QWidget 作為中央部件
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_label(self, count):
        self.label.setText(f"Count: {count}")