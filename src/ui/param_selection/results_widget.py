from services.classification_service import classification_service as cs
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel
class ResultsWidget:
    def __init__(self):
        self.example_img_label = QLabel("")
        
        # image of example number
        self.example_img = cs.get_example_number(
            0, 144)
        self.example_img_label.setText(self.example_img)

        # start button
        self.start_button = QPushButton("Start")
        #self.start_button.clicked.connect(self._handle_start_button_click)

        # add widgets to layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.example_img_label)
        self.layout.addWidget(self.start_button)

        self.layout.addStretch(1)

    def get_layout(self):
        return self.layout