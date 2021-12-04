
import time
from services.classification_service import classification_service as cs
from ui.params import params
from PyQt5.QtCore import Qt, QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QPushButton, QGridLayout, QLabel, QWidget
from utils.constants import CLASSIFIERS


class ExampleNumberImage:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)

        self.label = QLabel("")
        self.img = cs.get_example_number(
            params.get_random_integer(),
            params.get_grayscale_threshold()
        )
        self.label.setText(self.img)
        self.label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.label)

    def get_widget(self):
        return self.widget

    def update(self):
        self.img = cs.get_example_number(
            params.get_random_integer(),
            params.get_grayscale_threshold()
        )
        self.label.setText(self.img)


class StartingWidget:
    def __init__(self, show_progress_widget):
        self.threadpool = QThreadPool()

        self.show_progress_widget = show_progress_widget

        self.example_number_image = ExampleNumberImage()

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self._handle_start_button_click)

        note_label = QLabel("""
            Note!
            Pick small values for test and train data sizes.
            During calculation there's no threading (yet),
            so the program will freeze for a while.
        """)

        self.layout = QGridLayout()
        self.layout.addWidget(self.example_number_image.get_widget(), 0, 0)
        self.layout.addWidget(note_label, 1, 0)
        self.layout.addWidget(self.start_button, 2, 0)

    def get_layout(self):
        return self.layout

    def _handle_start_button_click(self):
        print("START BUTTON CLICKED")
        self.show_progress_widget()
        if params.get_classifier() == CLASSIFIERS[0]:
            worker = KNNClassificationThread()
            self.threadpool.start(worker)

    def update_image(self):
        self.example_number_image.update()


class KNNClassificationThread(QRunnable):
    @pyqtSlot()
    def run(self):
        cs.start_knn_classification(
            params.get_k(),
            params.get_grayscale_threshold(),
            params.get_distance_measure(),
            params.get_test_data_size(),
            params.get_train_data_size()
        )
