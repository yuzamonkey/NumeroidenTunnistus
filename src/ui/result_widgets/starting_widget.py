from services.classification_service import classification_service as cs
from ui.params import params
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel


class StartingWidget:
    def __init__(self, update):
        self.update = update

        self.example_img_label = QLabel("")
        self.update_image()
        # start button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self._handle_start_button_click)
        # add widgets to layout
        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.example_img_label)
        self.layout1.addWidget(self.start_button)
        self.layout1.addStretch(1)

        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(QLabel("Started"))

        self.layout = self.layout1

    def get_layout(self):
        return self.layout

    def _handle_start_button_click(self):
        print("START BUTTON CLICKED")
        cs.start_knn_classification(
            params.get_k(),
            params.get_grayscale_threshold(),
            params.get_distance_measure(),
            params.get_test_data_size(),
            params.get_train_data_size()
        )
        self.layout = self.layout2
        self.update()

    def update_image(self):
        self.example_img = cs.get_example_number(
            params.get_random_integer(),
            params.get_grayscale_threshold()
        )
        self.example_img_label.setText(self.example_img)
