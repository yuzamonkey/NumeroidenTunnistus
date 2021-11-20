import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class UI:
    def __init__(self):
        pass

    def start(self):
        app = QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(300, 100, 1200, 900)
        win.setWindowTitle("Number classifier")

        label = QtWidgets.QLabel(win)
        label.setText("LABEL text")
        label.move(50, 50)
        win.show()
        app.exec_()
        # sys.exit(app.exec_())


ui = UI()
