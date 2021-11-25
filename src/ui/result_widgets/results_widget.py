from services.classification_service import classification_service as cs
from ui.params import params
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from ui.results import results


class ResultsWidget:
    def __init__(self):
        self.layout = QVBoxLayout()
        self.label = QLabel(
            f"Done. Correct {results.get_correct_count()}, errors {results.get_errors_count()}")
        self.layout.addWidget(self.label)

    def update(self):
        self.label.setText(
            f"Done. Correct {results.get_correct_count()}, errors {results.get_errors_count()}")

    def get_layout(self):
        return self.layout
