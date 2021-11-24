import random

class Params:
    def __init__(self):
        self.k = 4
        self.distance_measure = "D22"
        self.grayscale_threshold = 150
        self.test_data_size = 20
        self.train_data_size = 50
        self.rand_int = random.randint(0, 1000)

    def get_k(self):
        return self.k

    def set_k(self, val):
        self.k = val

    def get_distance_measure(self):
        return self.distance_measure

    def set_distance_measure(self, distance_measure):
        self.distance_measure = distance_measure

    def get_grayscale_threshold(self):
        return self.grayscale_threshold

    def set_grayscale_threshold(self, threshold):
        self.grayscale_threshold = threshold

    def get_test_data_size(self):
        return self.test_data_size

    def set_test_data_size(self, size):
        self.test_data_size = size

    def get_train_data_size(self):
        return self.train_data_size

    def set_train_data_size(self, size):
        self.train_data_size = size

    def get_random_integer(self):
        return self.rand_int

    



params = Params()