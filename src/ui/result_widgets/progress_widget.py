import datetime
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QProgressBar
from ui.params import params

class ProgressWidget:
    def __init__(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Classifying...")
        self.time_estimate_label = QLabel("")
        
        self.time_passed = 0
        self.time_passed_label = QLabel("")
        self._update_time_labels()

        self.timer = QTimer()
        self.timer.timeout.connect(self._update_time_passed)
        #self.timer.start(1000)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.time_estimate_label)
        self.layout.addWidget(self.time_passed_label)

    def _update_time_passed(self):
        print("UPDATE TIME")
        self.time_passed += 1
        self._update_time_labels()

    def _update_time_labels(self):
        self.time_estimate_label.setText(f"Time estimate: {params.get_time_estimate()}")
        self.time_passed_label.setText(f"Time passed: {str(datetime.timedelta(seconds=self.time_passed))}")

    def start_timer(self):
        self.time_passed = 0
        self._update_time_labels()
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def get_layout(self):
        return self.layout
