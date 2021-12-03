import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QComboBox, QLabel, QSlider, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QGroupBox)
from ui.params import params

DISTANCE_MEASURES = ["D22", "D23"]

class DistanceMeasureSelection:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)
        
        self.label = QLabel("Distance measure:")
        self.selector = QComboBox()
        self.selector.addItems(DISTANCE_MEASURES)
        self.selector.activated[str].connect(
            self._change_dist_measure)
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.selector)

    def get_widget(self):
        return self.widget

    def _change_dist_measure(self):
        print("DIST MEASURE ", self.selector.currentText())
        params.set_distance_measure(self.selector.currentText())



class KNNOptionsWidget:
    def __init__(self, update_img):
        # update image function, used on threshold change
        self.update_img = update_img
        self.widget = QGroupBox()
        #self.layout.addWidget(QLabel("KNN OPTIONS WIDGET"))
        
        self.distance_measure_selection = DistanceMeasureSelection()
        # distance measure (d22, d23)
        # self.distance_measure_label = QLabel("Distance measure:")
        # self.distance_measures = QComboBox()
        # self.distance_measures.addItems(["D22", "D23"])
        # self.distance_measures.activated[str].connect(
        #     self._change_dist_measure)

        # k
        self.k_value_label = QLabel("K: ")
        self.grayscale_threshold_label = QLabel("")
        self.test_data_size_label = QLabel("")
        self.train_data_size_label = QLabel("")
        self.layout = QVBoxLayout()

        self.k_value = QSlider(Qt.Horizontal)
        self.k_value.valueChanged.connect(self._change_k_value)
        self.k_value.setMinimum(1)
        self.k_value.setMaximum(10)
        self.k_value.setSingleStep(1)
        self.k_value.setValue(params.get_k())
        self.k_value_label.setText(f"K: {self.k_value.value()}")

        # grayscale threshold (1-255)
        self.grayscale_threshold = QSlider(Qt.Horizontal)
        self.grayscale_threshold.valueChanged.connect(
            self._change_grayscale_threshold)
        self.grayscale_threshold.setMinimum(1)
        self.grayscale_threshold.setMaximum(255)
        self.grayscale_threshold.setSingleStep(1)
        self.grayscale_threshold.setValue(140)
        self.grayscale_threshold_label.setText(
            f"Grayscale threshold: {self.grayscale_threshold.value()}")

        # test data size (1-10_000)
        self.test_data_size = QSlider(Qt.Horizontal)
        self.test_data_size.valueChanged.connect(self._change_test_data_size)
        self.test_data_size.setMinimum(1)
        self.test_data_size.setMaximum(10_000)
        self.test_data_size.setSingleStep(1)
        self.test_data_size.setValue(10)
        self.test_data_size_label.setText(
            f"Test dataset size: {params.get_test_data_size()}")

        # train data size (1-60_000)
        self.train_data_size = QSlider(Qt.Horizontal)
        self.train_data_size.valueChanged.connect(self._change_train_data_size)
        self.train_data_size.setMinimum(1)
        self.train_data_size.setMaximum(60_000)
        self.train_data_size.setSingleStep(1)
        self.train_data_size.setValue(50)
        self.train_data_size_label.setText(
            f"Train dataset size: {params.get_train_data_size()}")

        self.distance_measures_link = QPushButton(
            "Distance measures (opens in browser)")
        self.distance_measures_link.clicked.connect(
            self._handle_browser_link_press)

        # add widgets to layout
        self.layout = QVBoxLayout(self.widget)

        self.layout.addWidget(self.distance_measure_selection.get_widget())

        self.layout.addWidget(self.k_value)
        self.layout.addWidget(self.k_value_label)

        self.layout.addWidget(self.grayscale_threshold)
        self.layout.addWidget(self.grayscale_threshold_label)

        self.layout.addWidget(self.test_data_size)
        self.layout.addWidget(self.test_data_size_label)

        self.layout.addWidget(self.train_data_size)
        self.layout.addWidget(self.train_data_size_label)

        self.layout.addWidget(self.distance_measures_link)

    def get_widget(self):
        return self.widget


    def _change_k_value(self):
        print("K ", self.k_value.value())
        params.set_k(self.k_value.value())
        self.k_value_label.setText(f"K: {params.get_k()}")

    def _change_grayscale_threshold(self):
        print("GRAYSCALE ", self.grayscale_threshold.value())
        params.set_grayscale_threshold(self.grayscale_threshold.value())
        self.grayscale_threshold_label.setText(
            f"Grayscale threshold: {self.grayscale_threshold.value()}")
        self.update_img()

    def _change_test_data_size(self):
        print("TEST DATA SIZE ", self.test_data_size.value())
        params.set_test_data_size(self.test_data_size.value())
        self.test_data_size_label.setText(
            f"Test dataset size: {params.get_test_data_size()}")

    def _change_train_data_size(self):
        print("TRAIN DATA SIZE ", self.train_data_size.value())
        params.set_train_data_size(self.train_data_size.value())
        self.train_data_size_label.setText(
            f"Train dataset size: {params.get_train_data_size()}")

    def _handle_browser_link_press(self):
        webbrowser.open(
            "https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf")
