from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QPushButton, QWidget
from ui.results import results
from ui.params import params
from services.classification_service import classification_service as cs

class ErrorsWidget:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)
        
        self.label = QLabel("")

        self.layout.addWidget(self.label)
        
    def get_widget(self):
        return self.widget
    
    def update(self):
        text = ""
        errors = results.get_errors()
        for e in errors:
            img_text = cs.get_example_number(e[1], params.get_grayscale_threshold())
            text += img_text

        self.label.setText(text)


class ResultsWidget:
    def __init__(self, show_starting_widget):
        self.layout = QVBoxLayout()
        self.label = QLabel("")

        self.errors_widget = ErrorsWidget()

        self.end_button = QPushButton("End")
        self.end_button.clicked.connect(show_starting_widget)
        self.end_button.setDefault(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.errors_widget.get_widget())
        self.layout.addWidget(self.end_button)

    def update(self):
        self.label.setText(
            f"""
            Correct: {results.get_correct_count()} / {results.get_total_count()} ({results.get_correct_percentage()}%) 
            Errors: {results.get_errors_count()} / {results.get_total_count()} ({results.get_error_percentage()}%)
            """
        )
        self.errors_widget.update()

    def get_layout(self):
        return self.layout
