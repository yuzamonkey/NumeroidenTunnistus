import unittest
from math import sqrt
from services.knn import knn


class TestNumberClassifier(unittest.TestCase):
    def setUp(self):
        self._knn = knn

    def test_classify_set_returns_float(self):
        percentage = self._knn.classify_set_of_numbers(3, 3, 10)
        self.assertEqual(type(percentage), float)

    def test_classify_number_returns_int(self):
        result = self._knn.classify_number(3, 0, 10)
        self.assertEqual(type(result), int)

    def test_update_k_nearest_returns_longer_list(self):
        k_nearest = [(0.8, 8)]
        new_distance = (0.4, 4)
        new_list = self._knn._update_k_nearest(3, k_nearest, new_distance)
        self.assertEqual(len(new_list), 2)

    def test_update_k_nearest_updates_shorter_distance(self):
        d1 = (0.7, 1)
        d2 = (0.8, 2)
        d3 = (0.9, 3)
        k_nearest = [d1, d2, d3]
        new_d = (0.4, 4)
        new_list = sorted(self._knn._update_k_nearest(3, k_nearest, new_d))
        expected = [new_d, d1, d2]
        self.assertEqual(new_list, expected)

    def test_update_k_nearest_returns_same_values_when_greater_distance(self):
        d1 = (0.7, 1)
        d2 = (0.8, 2)
        d3 = (0.9, 3)
        k_nearest = [d1, d2, d3]
        new_d = (0.95, 4)
        new_list = sorted(self._knn._update_k_nearest(3, k_nearest, new_d))
        expected = [d1, d2, d3]
        self.assertEqual(new_list, expected)

    def test_result_from_k_nearest_returns_int(self):
        d1 = (0.7, 1)
        d2 = (0.8, 2)
        d3 = (0.9, 3)
        k_nearest = [d1, d2, d3]
        result = self._knn._result_from_k_nearest(k_nearest)
        self.assertEqual(type(result), int)

    def test_point_to_set_distance_returns_correct_distance(self):
        mock = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
        result1 = self._knn._point_to_set_dist(4, 4, mock)
        result2 = self._knn._point_to_set_dist(4, 0, mock)
        result3 = self._knn._point_to_set_dist(3, 3, mock)
        self.assertEqual(result1, 0.0)
        self.assertEqual(result2, 4.0)
        self.assertEqual(result3, sqrt(2))
