from PyQt5.QtWidgets import (
    QComboBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget)
from ui.param_selection.knn_options_widget import KNNOptionsWidget

CLASSIFIERS = ["KNN"]

class ClassifierOptionsWidget:
    def __init__(self, update_classifier):
        self.widget = QWidget()
        self.classifier_label = QLabel("Select classifier")
        self.classifiers = QComboBox()
        self.classifiers.addItems(CLASSIFIERS)
        self.classifiers.activated[str].connect(update_classifier)

        self.layout = QHBoxLayout(self.widget)
        self.layout.addWidget(self.classifier_label)
        self.layout.addWidget(self.classifiers)

    def get_widget(self):
        return self.widget

    def get_current_text(self):
        return self.classifiers.currentText()

class ParamsWidget:
    def __init__(self, update_img):
        self.classifier_options = ClassifierOptionsWidget(self._update_classifier)

        self.knn_options = KNNOptionsWidget(update_img)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.classifier_options.get_widget())

        self.current_classifier_options = self.knn_options.get_widget()
        self.layout.addWidget(self.current_classifier_options)

    def get_layout(self):
        return self.layout

    def _update_classifier(self):
        print("CLASSIFIER ", self.classifier_options.get_current_text())
        self._remove_current_classifier_options()
        selection = self.classifier_options.get_current_text()
        if selection == CLASSIFIERS[0]:
            self.current_classifier_options = self.knn_options.get_widget()
        self.layout.addWidget(self.current_classifier_options)

    def _remove_current_classifier_options(self):
        if self.layout.itemAt(2) is not None:
            self.layout.itemAt(2).widget().setParent(None)
