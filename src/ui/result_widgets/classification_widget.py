from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import QLabel, QVBoxLayout


class ClassificationWidget:
    def __init__(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Started"))

    def get_layout(self):
        return self.layout
