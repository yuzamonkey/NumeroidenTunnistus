class Results:
    def __init__(self):
        self.correct_count = 0
        self.errors_count = 0
        self.errors = [] # (result, index)

    def get_correct_count(self):
        return self.correct_count

    def set_correct_count(self, count):
        self.correct_count = count

    def get_errors_count(self):
        return self.errors_count

    def set_errors_count(self, count):
        self.errors_count = count

    def get_errors(self):
        return self.errors

    def set_errors(self, errors):
        self.errors = errors

    def get_correct_percentage(self):
        return round((self.correct_count / self.get_total_count()) * 100, 2)

    def get_error_percentage(self):
        return round((self.errors_count / self.get_total_count()) * 100, 2)

    def get_total_count(self):
        return max((self.correct_count + self.errors_count), 0.000000001)



results = Results()
