# main.py
import sys
from PySide2.QtWidgets import QApplication
from app.model import Model
from app.view import View
from app.controller import Controller

def main():
    app = QApplication(sys.argv)

    # 初始化模型、視圖和控制器
    model = Model()
    view = View()
    controller = Controller(model, view)

    # 顯示視圖
    view.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
