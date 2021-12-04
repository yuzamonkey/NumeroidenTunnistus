import time
from services.classification_service import classification_service as cs
from ui.params import params
from PyQt5.QtCore import Qt, QRunnable, QThreadPool, pyqtSlot
from PyQt5.QtWidgets import QPushButton, QGridLayout, QLabel, QWidget
from utils.constants import CLASSIFIERS


class ExampleNumberImage:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)

        self.label = QLabel("")
        self.img = cs.get_image_from_test_data(
            params.get_random_integer(),
            params.get_grayscale_threshold()
        )
        self.label.setText(self.img)
        self.label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.label)

    def get_widget(self):
        return self.widget

    def update(self):
        self.img = cs.get_image_from_test_data(
            params.get_random_integer(),
            params.get_grayscale_threshold()
        )
        self.label.setText(self.img)


class StartingWidget:
    def __init__(self, show_progress_widget, show_results_widget):
        self.threadpool = QThreadPool()

        self.show_progress_widget = show_progress_widget
        self.show_results_widget = show_results_widget

        self.example_number_image = ExampleNumberImage()

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self._handle_start_button_click)

        self.time_estimate_label = QLabel(
            f"Time estimate: {params.get_time_estimate()}")
        self.time_estimate_label.setAlignment(Qt.AlignCenter)

        self.layout = QGridLayout()
        self.layout.addWidget(self.example_number_image.get_widget(), 0, 0)
        self.layout.addWidget(self.start_button, 1, 0)
        self.layout.addWidget(self.time_estimate_label, 2, 0)

    def get_layout(self):
        return self.layout

    def _handle_start_button_click(self):
        print("START BUTTON CLICKED")
        self.show_progress_widget()
        if params.get_classifier() == CLASSIFIERS[0]:
            worker = KNNClassificationThread(self.show_results_widget)
            self.threadpool.start(worker)

    def update_image(self):
        self.example_number_image.update()

    def update_time_estimate(self):
        self.time_estimate_label.setText(
            f"Time estimate: {params.get_time_estimate()}")


class KNNClassificationThread(QRunnable):
    def __init__(self, show_results_widget):
        super().__init__()
        self.show_results_widget = show_results_widget

    @pyqtSlot()
    def run(self):
        #start_time = time.time()
        cs.start_knn_classification(
            params.get_k(),
            params.get_grayscale_threshold(),
            params.get_distance_measure(),
            params.get_test_data_size(),
            params.get_train_data_size()
        )
        #print(f"--- classification took {(time.time() - start_time)} seconds ---")
        self.show_results_widget()
