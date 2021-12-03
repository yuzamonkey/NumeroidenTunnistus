from PyQt5.QtWidgets import (
    QComboBox, QLabel, QVBoxLayout)
from ui.param_selection.knn_options_widget import KNNOptionsWidget


class ParamsWidget:
    def __init__(self, update_img):
        self.knn_options = KNNOptionsWidget(update_img)

        # select classifier
        self.classifier_label = QLabel("Select classifier")
        self.classifiers = QComboBox()
        self.classifiers.addItems(["KNN"])
        self.classifiers.activated[str].connect(self._update_classifier)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.classifier_label)
        self.layout.addWidget(self.classifiers)

        self.classifier_options = self.knn_options.get_widget()
        self.layout.addWidget(self.classifier_options)

    def get_layout(self):
        return self.layout

    def _update_classifier(self):
        print("CLASSIFIER ", self.classifiers.currentText())
        self._remove_current_classifier_options()
        if self.classifiers.currentText() == "KNN":
            self.classifier_options = self.knn_options.get_widget()
        self.layout.addWidget(self.classifier_options)

    def _remove_current_classifier_options(self):
        if self.layout.itemAt(2) is not None:
            self.layout.itemAt(2).widget().setParent(None)
