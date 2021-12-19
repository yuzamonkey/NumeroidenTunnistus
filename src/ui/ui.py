import sys
from PyQt5.QtWidgets import QApplication
from ui.window import Window


class UI:
    def start(self):
        app = QApplication(sys.argv)
        win = Window()
        win.setGeometry(100, 100, 1200, 900)
        win.setWindowTitle("Number classifier")
        win.show()
        app.exec()
