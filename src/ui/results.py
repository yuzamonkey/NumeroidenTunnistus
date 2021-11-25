class Results:
    def __init__(self):
        self.correct = 0
        self.wrong = 0

    def get_correct_count(self):
        return self.correct

    def set_correct_count(self, count):
        self.correct = count

    def get_wrong_count(self):
        return self.wrong

    def set_wrong_count(self, count):
        self.wrong = count
