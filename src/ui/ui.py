import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class UI:
    def __init__(self):
        pass

    def window(self):
        app = QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(200, 200, 300, 300)
        win.setWindowTitle("HELLO WORLD")

        label = QtWidgets.QLabel(win)
        label.setText("LABEL text")
        label.move(50, 50)
        win.show()
        app.exec_()
        # sys.exit(app.exec_())


ui = UI()
