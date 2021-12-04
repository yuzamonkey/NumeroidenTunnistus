from PyQt5.QtWidgets import (
    QApplication, QDialog, QGridLayout, QGroupBox, QStyleFactory)
from ui.result_widgets.results_widget import ResultsWidget
from ui.result_widgets.starting_widget import StartingWidget
from ui.param_selection.params_widget import ParamsWidget
from ui.result_widgets.progress_widget import ProgressWidget


class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.results_widget = ResultsWidget(self.showStartingWidget)
        self.progress_widget = ProgressWidget(
            self.showResultsWidget, self.results_widget.update)
        self.starting_widget = StartingWidget(self.showProgressWidget)

        self.params_widget = ParamsWidget(self.starting_widget.update_image)

        self.createParametersGroupBox()
        self.createResultsGroupBox()
        self.createClassificationGroupBox()
        self.createStartingGroupBox()

        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.parametersGroupBox, 0, 0)
        self.mainLayout.addWidget(self.startingGroupBox, 0, 1)
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

    def createStartingGroupBox(self):
        self.startingGroupBox = QGroupBox()
        self.startingGroupBox.setLayout(self.starting_widget.get_layout())

    def createClassificationGroupBox(self):
        self.classificationGroupBox = QGroupBox()
        self.classificationGroupBox.setLayout(
            self.progress_widget.get_layout())

    def showStartingWidget(self):
        self.clearRightGroupBox()
        self.mainLayout.addWidget(self.startingGroupBox, 0, 1)

    def showProgressWidget(self):
        self.clearRightGroupBox()
        self.mainLayout.addWidget(self.classificationGroupBox, 0, 1)

    def showResultsWidget(self):
        self.clearRightGroupBox()
        self.mainLayout.addWidget(self.resultsGroupBox, 0, 1)

    def clearRightGroupBox(self):
        self.startingGroupBox.setParent(None)
        self.classificationGroupBox.setParent(None)
        self.resultsGroupBox.setParent(None)
