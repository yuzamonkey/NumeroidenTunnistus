from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QGroupBox, QTextEdit,
                             QVBoxLayout, QWidget)

from ui.result_widgets.starting_widget import StartingWidget
from ui.param_selection.params_widget import ParamsWidget
from ui.result_widgets.classification_widget import ClassificationWidget


class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.classification_widget = ClassificationWidget()
        self.starting_widget = StartingWidget(self.updateResultsGroupBox)
        self.params_widget = ParamsWidget(self.starting_widget.update_image)
        self.createParametersGroupBox()
        self.createResultsGroupBox()
        self.createClassificationGroupBox()

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.parametersGroupBox, 0, 0)
        self.mainLayout.addWidget(self.resultsGroupBox, 0, 1)
        self.mainLayout.setColumnStretch(0, 1)
        self.mainLayout.setColumnStretch(1, 1)
        self.setLayout(self.mainLayout)

        QApplication.setStyle(QStyleFactory.create('Fusion'))

    def createParametersGroupBox(self):
        self.parametersGroupBox = QGroupBox()
        self.parametersGroupBox.setLayout(self.params_widget.get_layout())

    def createResultsGroupBox(self):
        self.resultsGroupBox = QGroupBox()
        self.resultsGroupBox.setLayout(self.starting_widget.get_layout())

    def createClassificationGroupBox(self):
        self.classificationGroupBox = QGroupBox()
        self.classificationGroupBox.setLayout(
            self.classification_widget.get_layout())

    def updateResultsGroupBox(self):
        print("UPDATE CALLED")
        # self.mainLayout.removeWidget(self.resultsGroupBox)
        self.resultsGroupBox.setParent(None)
        self.mainLayout.addWidget(self.classificationGroupBox, 0, 1)
