from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QPushButton, QWidget
from ui.results import results
from ui.params import params
from services.classification_service import classification_service as cs

class StatsWidget:
    def __init__(self):
        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)

        self.results_label = QLabel("")

        self.previous_button = QPushButton("<")
        self.previous_button.clicked.connect(self._handle_previous_click)
        self.next_button = QPushButton(">")
        self.next_button.clicked.connect(self._handle_next_click)
        self.current_error_index = 0
        self.index_of_error_label = QLabel(f"Error {self.current_error_index + 1}/{results.get_errors_count()}")
        
        self.image_label = QLabel("")

        self.layout.addWidget(self.results_label, 0, 0, 1, 0, Qt.AlignCenter)
        
        self.layout.addWidget(self.previous_button, 1, 0, 1, 1)
        self.layout.addWidget(self.index_of_error_label, 1, 1, 1, 1, Qt.AlignCenter)
        self.layout.addWidget(self.next_button, 1, 2, 1, 1)
        
        self.layout.addWidget(self.image_label, 2, 1, 5, 1, Qt.AlignCenter)

    def update(self):
        self.results_label.setText(
            f"""
            Correct: {results.get_correct_count()} / {results.get_total_count()} ({results.get_correct_percentage()}%) 
            Errors: {results.get_errors_count()} / {results.get_total_count()} ({results.get_error_percentage()}%)
            """
        )
        self.current_error_index = 0
        self.index_of_error_label.setText(f"Error {self.current_error_index + 1}/{results.get_errors_count()}")
        self._update_img_label()
        
    def get_widget(self):
        return self.widget
    
    def _handle_previous_click(self):
        if self.current_error_index > 0:
            self.current_error_index -= 1
            self.index_of_error_label.setText(f"Error {self.current_error_index + 1}/{results.get_errors_count()}")
            self._update_img_label()

    def _handle_next_click(self):
        if self.current_error_index < results.get_errors_count() - 1:
            self.current_error_index += 1
            self.index_of_error_label.setText(f"Error {self.current_error_index + 1}/{results.get_errors_count()}")
            self._update_img_label()

    def _update_img_label(self):
        if results.get_errors_count() > 0:
            e = results.get_errors()[self.current_error_index]
            img_text = cs.get_image_from_test_data(e[1], params.get_grayscale_threshold())
            result_text = f"This image of {cs.get_label_from_test_data(e[1])} was classified as {e[0]}."
            self.image_label.setText(f"{img_text}\n{result_text}")


class ResultsWidget:
    def __init__(self, show_starting_widget):
        self.layout = QGridLayout()

        self.stats_widget = StatsWidget()

        self.end_button = QPushButton("End")
        self.end_button.clicked.connect(show_starting_widget)
        self.end_button.setDefault(True)

        self.layout.addWidget(self.stats_widget.get_widget(), 0, 0, 7, 0)
        self.layout.addWidget(self.end_button, 8, 0)

    def update(self):
        self.stats_widget.update()

    def get_layout(self):
        return self.layout
