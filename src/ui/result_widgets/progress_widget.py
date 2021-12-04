from PyQt5.QtWidgets import QVBoxLayout, QPushButton


class ProgressWidget:
    def __init__(self, show_results_group_box, update_results_widget):
        self.update_results_widget = update_results_widget
        self.show_results_group_box = show_results_group_box

        self.layout = QVBoxLayout()
        self.show_results_button = QPushButton("Show results")
        self.show_results_button.setDefault(True)
        self.show_results_button.clicked.connect(
            self.handle_show_results_button_press)

        self.layout.addWidget(self.show_results_button)

    def handle_show_results_button_press(self):
        self.update_results_widget()
        self.show_results_group_box()

    def get_layout(self):
        return self.layout
