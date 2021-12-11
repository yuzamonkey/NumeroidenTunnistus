import random
import math
import datetime
from utils.constants import CLASSIFIERS


class Params:
    def __init__(self):
        self.classifier = CLASSIFIERS[0]
        self.k = 4
        self.distance_measure = "D22"
        self.grayscale_threshold = 150
        self.test_data_size = 20
        self.train_data_size = 50
        self.example_image_index = random.randint(0, 1000)
        self.use_random_test_set = False
        self.use_random_train_set = False

    def get_classifier(self):
        return self.classifier

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

    def get_use_random_test_set(self):
        return self.use_random_test_set
    
    def set_use_random_test_set(self, value):
        self.use_random_test_set = value

    def get_use_random_train_set(self):
        return self.use_random_train_set
    
    def set_use_random_train_set(self, value):
        self.use_random_train_set = value

    def get_example_image_index(self):
        return self.example_image_index

    def get_time_estimate(self):
        time_estimate = math.ceil(
            self.test_data_size * (0.007 * self.train_data_size))
        return str(datetime.timedelta(seconds=time_estimate))


params = Params()
