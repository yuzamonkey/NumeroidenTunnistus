class Results:
    def __init__(self):
        self.correct = 0
        self.errors = 0

    def get_correct_count(self):
        return self.correct

    def set_correct_count(self, count):
        self.correct = count

    def get_errors_count(self):
        return self.errors

    def set_errors_count(self, count):
        self.errors = count


results = Results()
