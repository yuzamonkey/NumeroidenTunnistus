from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
                             QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
                             QSlider, QSpinBox, QStyleFactory, QTableWidget, QGroupBox, QTextEdit,
                             QVBoxLayout, QWidget)
from ui.result_widgets.results_widget import ResultsWidget
from ui.param_selection.params_widget import ParamsWidget
from ui.result_widgets.foobaar import Foobaar

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.foobar_widget = Foobaar()
        self.results_widget = ResultsWidget(self.updateResultsGroupBox)
        self.params_widget = ParamsWidget(self.results_widget.update_image)

        self.createParametersGroupBox()
        self.createResultsGroupBox()
        self.createFoobaarGroupBox()
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
        self.resultsGroupBox.setLayout(self.results_widget.get_layout())

    def createFoobaarGroupBox(self):
        self.foobarGroupBox = QGroupBox()
        self.foobarGroupBox.setLayout(self.foobar_widget.get_layout())

    def updateResultsGroupBox(self):
        print("UPDATE CALLED")
        #self.mainLayout.removeWidget(self.resultsGroupBox)
        self.resultsGroupBox.setParent(None)
        self.mainLayout.addWidget(self.foobarGroupBox, 0, 1)