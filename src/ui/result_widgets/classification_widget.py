from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton
from ui.results import results

class ClassificationWidget:
    def __init__(self, show_results_group_box):
        self.layout = QVBoxLayout()
        self.show_results_button = QPushButton("Show results")
        self.show_results_button.clicked.connect(show_results_group_box)
        
        self.layout.addWidget(self.show_results_button)


    def get_layout(self):
        return self.layout
