import webbrowser
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QComboBox, QLabel, QSlider, QVBoxLayout, QHBoxLayout, QWidget, QGroupBox)
from ui.params import params
from utils.constants import DISTANCE_MEASURES, DISTANCE_MEASURES_ADDRESS


class KNNOptionsWidget:
    def __init__(self, update_img, update_time_estimate):
        self.widget = QGroupBox()

        self.distance_measure_selector = DistanceMeasureSelector()
        self.k_value_selector = KValueSelector()
        self.grayscale_threshold_selector = ThresholdSelector(update_img)
        self.test_data_size_selector = TestDataSizeSelector(update_time_estimate)
        self.train_data_size_selector = TrainDataSizeSelector(update_time_estimate)

        self.layout = QVBoxLayout(self.widget)

        self.layout.addWidget(self.distance_measure_selector.get_widget())
        self.layout.addWidget(self.k_value_selector.get_widget())
        self.layout.addWidget(self.grayscale_threshold_selector.get_widget())
        self.layout.addWidget(self.test_data_size_selector.get_widget())
        self.layout.addWidget(self.train_data_size_selector.get_widget())

    def get_widget(self):
        return self.widget


class HyperlinkLabel:
    def __init__(self, text, address):
        self.address = address

        self.label = QLabel(text)
        self.label.setStyleSheet(
            "QLabel { color : #0033aa; text-decoration : underline;}")
        self.label.setMouseTracking(True)
        self.label.mousePressEvent = self._handle_browser_link_press
        self.label.setCursor(QCursor(Qt.PointingHandCursor))

    def _handle_browser_link_press(self, widget):
        webbrowser.open(self.address)

    def get_label(self):
        return self.label


class DistanceMeasureSelector:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)

        self.selector = QComboBox()
        self.selector.addItems(DISTANCE_MEASURES)
        self.selector.activated[str].connect(
            self._update_distance_measure)

        self.link_label = HyperlinkLabel(
            "Distance measure: ", DISTANCE_MEASURES_ADDRESS)

        self.layout.addWidget(self.link_label.get_label())
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
    def __init__(self, update_time_estimate):
        self.update_time_estimate = update_time_estimate
        
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
        self.update_time_estimate()


class TrainDataSizeSelector:
    def __init__(self, update_time_estimate):
        self.update_time_estimate = update_time_estimate
        
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
        self.update_time_estimate()
