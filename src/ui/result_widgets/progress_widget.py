from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel


class ProgressWidget:
    def __init__(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Classifying...")
        self.layout.addWidget(self.label)

    def get_layout(self):
        return self.layout
