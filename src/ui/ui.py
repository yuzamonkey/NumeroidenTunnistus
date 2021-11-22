import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QToolBar, QStatusBar, QApplication, QMainWindow, QGridLayout, QPushButton


class UI:
    def __init__(self):
        pass

    def start(self):
        app = QApplication(sys.argv)
        win = Window()
        win.show()
        app.exec_()

        # win = QMainWindow()
        # win.setGeometry(300, 100, 1200, 900)
        # win.setWindowTitle("Number classifier")

        # foo = QWidget()
        # layout = QGridLayout()
        # layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
        # layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
        # foo.setLayout(layout)
        # foo.show()
        # win.show()
        # app.exec_()
        # sys.exit(app.exec_())



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number classifier")
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self.setGeometry(300, 100, 1200, 900)

        layout = QGridLayout()
        layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
        layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
        self.setLayout(layout)

    #     self._createMenu()
    #     self._createToolBar()
    #     self._createStatusBar()

    # def _createMenu(self):
    #     self.menu = self.menuBar().addMenu("&Menu")
    #     self.menu.addAction('&Exit', self.close)

    # def _createToolBar(self):
    #     tools = QToolBar()
    #     self.addToolBar(tools)
    #     tools.addAction('Exit', self.close)

    # def _createStatusBar(self):
    #     status = QStatusBar()
    #     status.showMessage("I'm the Status Bar")
    #     self.setStatusBar(status)