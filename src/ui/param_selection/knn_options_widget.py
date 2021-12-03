import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QComboBox, QLabel, QSlider, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QGroupBox)
from ui.params import params
from utils.constants import DISTANCE_MEASURES

class DistanceMeasureSelector:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)

        self.label = QLabel("Distance measure:")
        self.selector = QComboBox()
        self.selector.addItems(DISTANCE_MEASURES)
        self.selector.activated[str].connect(
            self._update_distance_measure)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.selector)

    def get_widget(self):
        return self.widget

    def _update_distance_measure(self):
        print("DIST MEASURE ", self.selector.currentText())
        params.set_distance_measure(self.selector.currentText())


class KValueSelector:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)

        self.label = QLabel("K: ")

        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self._update_k)
        self.slider.setMinimum(1)
        self.slider.setMaximum(10)
        self.slider.setSingleStep(1)
        params.set_k(4)
        self.slider.setValue(params.get_k())

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)

    def get_widget(self):
        return self.widget

    def _update_k(self):
        print("K ", self.slider.value())
        params.set_k(self.slider.value())
        self.label.setText(f"K: {params.get_k()}")


class ThresholdSelector:
    def __init__(self, update_img):
        self.update_img = update_img
        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)

        self.label = QLabel("")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(
            self._update_grayscale_threshold)
        self.slider.setMinimum(1)
        self.slider.setMaximum(255)
        self.slider.setSingleStep(1)
        self.slider.setValue(140)
        self.label.setText(
            f"Grayscale threshold: {self.slider.value()}")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)

    def get_widget(self):
        return self.widget

    def _update_grayscale_threshold(self):
        print("GRAYSCALE ", self.slider.value())
        params.set_grayscale_threshold(self.slider.value())
        self.label.setText(
            f"Grayscale threshold: {self.slider.value()}")
        self.update_img()


class TestDataSizeSelector:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)

        self.label = QLabel("")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self._update_test_data_size)
        self.slider.setMinimum(1)
        self.slider.setMaximum(10_000)
        self.slider.setSingleStep(1)
        self.slider.setValue(10)
        self.label.setText(
            f"Test dataset size: {params.get_test_data_size()}")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)

    def get_widget(self):
        return self.widget

    def _update_test_data_size(self):
        print("TEST DATA SIZE ", self.slider.value())
        params.set_test_data_size(self.slider.value())
        self.label.setText(
            f"Test dataset size: {params.get_test_data_size()}")


class TrainDataSizeSelector:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)

        self.label = QLabel("")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self._update_train_data_size)
        self.slider.setMinimum(1)
        self.slider.setMaximum(60_000)
        self.slider.setSingleStep(1)
        self.slider.setValue(50)
        self.label.setText(
            f"Train dataset size: {params.get_train_data_size()}")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)

    def get_widget(self):
        return self.widget

    def _update_train_data_size(self):
        print("TRAIN DATA SIZE ", self.slider.value())
        params.set_train_data_size(self.slider.value())
        self.label.setText(
            f"Train dataset size: {params.get_train_data_size()}")


class KNNOptionsWidget:
    def __init__(self, update_img):
        # update image function, used on threshold change
        update_img
        self.widget = QGroupBox()
        #self.layout.addWidget(QLabel("KNN OPTIONS WIDGET"))

        self.distance_measure_selector = DistanceMeasureSelector()
        self.k_value_selector = KValueSelector()
        self.grayscale_threshold_selector = ThresholdSelector(update_img)
        self.test_data_size_selector = TestDataSizeSelector()
        self.train_data_size_selector = TrainDataSizeSelector()

        self.distance_measures_link = QPushButton(
            "Distance measures (opens in browser)")
        self.distance_measures_link.clicked.connect(
            self._handle_browser_link_press)

        # add widgets to layout
        self.layout = QVBoxLayout(self.widget)

        self.layout.addWidget(self.distance_measure_selector.get_widget())
        self.layout.addWidget(self.k_value_selector.get_widget())
        self.layout.addWidget(self.grayscale_threshold_selector.get_widget())
        self.layout.addWidget(self.test_data_size_selector.get_widget())
        self.layout.addWidget(self.train_data_size_selector.get_widget())

        self.layout.addWidget(self.distance_measures_link)

    def get_widget(self):
        return self.widget

    def _handle_browser_link_press(self):
        webbrowser.open(
            "https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf")
