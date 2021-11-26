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

    def get_correct_percentage(self):
        return round((self.correct / self.get_total_count()) * 100, 2)

    def get_error_percentage(self):
        return round((self.errors / self.get_total_count()) * 100, 2)

    def get_total_count(self):
        return max((self.correct + self.errors), 0.000000001)



results = Results()
