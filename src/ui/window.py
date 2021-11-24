import random
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QGroupBox, QTextEdit,
                             QVBoxLayout, QWidget)
from services.classification_service import classification_service as cs


class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.originalPalette = QApplication.palette()
        self.example_img_label = QLabel("")
        self.rand_int = random.randint(0, 1000)

        #styleComboBox = QComboBox()
        # styleComboBox.addItems(QStyleFactory.keys())

        #styleLabel = QLabel("&Style:")
        # styleLabel.setBuddy(styleComboBox)

        # self.useStylePaletteCheckBox = QCheckBox(
        #     "&Use style's standard palette")
        # self.useStylePaletteCheckBox.setChecked(False)

        #disableWidgetsCheckBox = QCheckBox("&Disable widgets")

        self.createParametersGroupBox()
        self.createResultsGroupBox()
        #self.createTopRightGroupBox()
        #self.createBottomRightGroupBox()
        # self.createProgressBar()

        # styleComboBox.activated[str].connect(self.changeStyle)
        # self.useStylePaletteCheckBox.toggled.connect(self.changePalette)

        # disableWidgetsCheckBox.toggled.connect(
        #     self.parametersGroupBox.setDisabled)
        # disableWidgetsCheckBox.toggled.connect(
        #     self.topRightGroupBox.setDisabled)
        # disableWidgetsCheckBox.toggled.connect(
        #     self.resultsGroupBox.setDisabled)
        # disableWidgetsCheckBox.toggled.connect(
        #     self.bottomRightGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        # topLayout.addWidget(styleLabel)
        # topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        # topLayout.addWidget(self.useStylePaletteCheckBox)
        # topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 0, 0)
        mainLayout.addWidget(self.parametersGroupBox, 0, 0)
        mainLayout.addWidget(self.resultsGroupBox, 0, 1)
        #mainLayout.addWidget(self.topRightGroupBox, 2, 0)
        #mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        #mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        #mainLayout.setRowStretch(1, 1)
        #mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        QApplication.setStyle(QStyleFactory.create('Fusion'))
        # QApplication.setStyle(QStyleFactory.create('macos'))
        # self.changeStyle('Fusion')

    # def changePalette(self):
    #     if (self.useStylePaletteCheckBox.isChecked()):
    #         QApplication.setPalette(QApplication.style().standardPalette())
    #     else:
    #         QApplication.setPalette(self.originalPalette)

    # def advanceProgressBar(self):
    #     curVal = self.progressBar.value()
    #     maxVal = self.progressBar.maximum()
    #     self.progressBar.setValue(curVal + (maxVal - curVal) / 100)

    def _change_classifier(self):
        print("CLASSIFIER ", self.classifiers.currentText())

    def _change_k_value(self):
        print("K ", self.k_value.value())
        self.k_value_label.setText(str(self.k_value.value()))

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
            self.k_value.value(),
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
            self.k_value.setValue(4)
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

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Group 2")

        defaultPushButton = QPushButton("Default Push Button")
        defaultPushButton.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        layout = QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(togglePushButton)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        lineEdit = QLineEdit('s3cRe7')
        lineEdit.setEchoMode(QLineEdit.Password)

        spinBox = QSpinBox(self.bottomRightGroupBox)
        spinBox.setValue(50)

        dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
        dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        slider = QSlider(Qt.Horizontal, self.bottomRightGroupBox)
        slider.setValue(40)

        scrollBar = QScrollBar(Qt.Horizontal, self.bottomRightGroupBox)
        scrollBar.setValue(60)

        dial = QDial(self.bottomRightGroupBox)
        dial.setValue(30)
        dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(lineEdit, 0, 0, 1, 2)
        layout.addWidget(spinBox, 1, 0, 1, 2)
        layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        layout.addWidget(slider, 3, 0)
        layout.addWidget(scrollBar, 4, 0)
        layout.addWidget(dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.bottomRightGroupBox.setLayout(layout)

    # def createProgressBar(self):
    #     self.progressBar = QProgressBar()
    #     self.progressBar.setRange(0, 10000)
    #     self.progressBar.setValue(0)

    #     timer = QTimer(self)
    #     timer.timeout.connect(self.advanceProgressBar)
    #     timer.start(1000)
