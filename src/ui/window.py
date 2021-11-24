import random
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QGroupBox, QTextEdit,
                             QVBoxLayout, QWidget)
from services.classification_service import classification_service as cs
from ui.param_selection.results_widget import ResultsWidget

from ui.params import params

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.example_img_label = QLabel("")
        self.rand_int = random.randint(0, 1000)

        self.results_widget = ResultsWidget()

        self.createParametersGroupBox()
        self.createResultsGroupBox()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.parametersGroupBox, 0, 0)
        mainLayout.addWidget(self.resultsGroupBox, 0, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        QApplication.setStyle(QStyleFactory.create('Fusion'))

    def _change_classifier(self):
        print("CLASSIFIER ", self.classifiers.currentText())

    def _change_k_value(self):
        print("K ", self.k_value.value())
        params.set_k(self.k_value.value())
        self.k_value_label.setText(str(params.get_k()))

    def _change_dist_measure(self):
        print("DIST MEASURE ", self.distance_measures.currentText())

    def _change_grayscale_threshold(self):
        print("GRAYSCALE ", self.grayscale_threshold.value())
        self.grayscale_threshold_label.setText(
            str(self.grayscale_threshold.value()))
        self.example_img = cs.get_example_number(
            self.rand_int, self.grayscale_threshold.value())
        self.example_img_label.setText(self.example_img)

    def _change_test_data_size(self):
        print("TEST DATA SIZE ", self.test_data_size.value())
        self.test_data_size_label.setText(str(self.test_data_size.value()))

    def _change_train_data_size(self):
        print("TRAIN DATA SIZE ", self.train_data_size.value())
        self.train_data_size_label.setText(str(self.train_data_size.value()))

    def _handle_start_button_click(self):
        print("START BUTTON CLICKED")
        cs.start_knn_classification(
            params.get_k(),
            self.grayscale_threshold.value(),
            self.distance_measures.currentText(),
            self.test_data_size.value(),
            self.train_data_size.value()
        )

    def createParametersGroupBox(self):
        self.parametersGroupBox = QGroupBox()

        # select classifier
        self.classifiers = QComboBox()
        self.classifiers.addItems(
            ["KNN", "Neural network", "Some other example"])
        self.classifiers.activated[str].connect(self._change_classifier)

        self.k_value_label = QLabel("")
        self.grayscale_threshold_label = QLabel("")
        self.test_data_size_label = QLabel("")
        self.train_data_size_label = QLabel("")
        layout = QVBoxLayout()
        if self.classifiers.currentText() == "KNN":
                
            # for now, KNN options

            # k
            self.k_value = QSlider(Qt.Horizontal, self.parametersGroupBox)
            self.k_value.valueChanged.connect(self._change_k_value)
            self.k_value.setMinimum(1)
            self.k_value.setMaximum(10)
            self.k_value.setSingleStep(1)
            self.k_value.setValue(params.get_k())
            print("•••", params.get_k())
            self.k_value_label.setText(str(self.k_value.value()))

            # distance measure (d22, d23)
            self.distance_measures = QComboBox()
            self.distance_measures.addItems(["D22", "D23"])
            #self.distance_measures.valueChanged.connect(self._change_dist_measure)
            self.distance_measures.activated[str].connect(self._change_dist_measure)

            # grayscale threshold (1-255)
            self.grayscale_threshold = QSlider(Qt.Horizontal, self.parametersGroupBox)
            self.grayscale_threshold.valueChanged.connect(
                self._change_grayscale_threshold)
            self.grayscale_threshold.setMinimum(1)
            self.grayscale_threshold.setMaximum(255)
            self.grayscale_threshold.setSingleStep(1)
            self.grayscale_threshold.setValue(140)
            self.grayscale_threshold_label.setText(
                str(self.grayscale_threshold.value()))

            # test data size (1-10_000)
            self.test_data_size = QSlider(Qt.Horizontal, self.parametersGroupBox)
            self.test_data_size.valueChanged.connect(self._change_test_data_size)
            self.test_data_size.setMinimum(1)
            self.test_data_size.setMaximum(10_000)
            self.test_data_size.setSingleStep(1)
            self.test_data_size.setValue(10)
            self.test_data_size_label.setText(str(self.test_data_size.value()))

            # train data size (1-60_000)
            self.train_data_size = QSlider(Qt.Horizontal, self.parametersGroupBox)
            self.train_data_size.valueChanged.connect(self._change_train_data_size)
            self.train_data_size.setMinimum(1)
            self.train_data_size.setMaximum(60_000)
            self.train_data_size.setSingleStep(1)
            self.train_data_size.setValue(50)
            self.train_data_size_label.setText(str(self.train_data_size.value()))

            # add widgets to layout
            # layout = QVBoxLayout()
            layout.addWidget(self.classifiers)

            layout.addWidget(self.distance_measures)

            layout.addWidget(self.k_value)
            layout.addWidget(self.k_value_label)

            layout.addWidget(self.grayscale_threshold)
            layout.addWidget(self.grayscale_threshold_label)

            layout.addWidget(self.test_data_size)
            layout.addWidget(self.test_data_size_label)

            layout.addWidget(self.train_data_size)
            layout.addWidget(self.train_data_size_label)

            # layout.addStretch(1)
        self.parametersGroupBox.setLayout(layout)

    def createResultsGroupBox(self):
        self.resultsGroupBox = QGroupBox()

        # image of example number
        self.example_img = cs.get_example_number(
            self.rand_int, self.grayscale_threshold.value())
        self.example_img_label.setText(self.example_img)

        # start button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self._handle_start_button_click)

        # add widgets to layout
        layout = QVBoxLayout()
        layout.addWidget(self.example_img_label)
        layout.addWidget(self.start_button)

        layout.addStretch(1)
        self.resultsGroupBox.setLayout(layout)
        self.resultsGroupBox.setLayout(layout)
