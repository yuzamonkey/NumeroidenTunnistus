import unittest
from math import sqrt
from services.knn import knn
from utils.utils import as_2d_arrays


class TestNumberClassifier(unittest.TestCase):
    def setUp(self):
        self._knn = knn
        self.test_set_imgs, self.test_set_labels = knn.get_test_set(
            3, True, 140)
        self.train_set_imgs, self.train_set_labels = knn.get_train_set(
            10, True, 140)

    def test_get_test_set_returns_correct_number_of_items_when_random(self):
        num_of_items = 200
        test_set_imgs, test_set_labels = knn.get_test_set(
            num_of_items, False, 140)
        self.assertEqual(len(test_set_imgs), num_of_items)
        self.assertEqual(len(test_set_labels), num_of_items)

    def test_get_train_set_returns_correct_number_of_items_when_random(self):
        num_of_items = 200
        train_set_imgs, train_set_labels = knn.get_train_set(
            num_of_items, False, 140)
        self.assertEqual(len(train_set_imgs), num_of_items)
        self.assertEqual(len(train_set_labels), num_of_items)

    def test_get_test_set_returns_correct_number_of_items_when_not_random(self):
        num_of_items = 200
        test_set_imgs, test_set_labels = knn.get_test_set(
            num_of_items, True, 140)
        self.assertEqual(len(test_set_imgs), num_of_items)
        self.assertEqual(len(test_set_labels), num_of_items)

    def test_get_train_set_returns_correct_number_of_items_when_not_random(self):
        num_of_items = 200
        train_set_imgs, train_set_labels = knn.get_train_set(
            num_of_items, True, 140)
        self.assertEqual(len(train_set_imgs), num_of_items)
        self.assertEqual(len(train_set_labels), num_of_items)

    def test_classify_set_returns_tuple(self):
        result = self._knn.classify_set_of_numbers(3, 144, 3, 10)
        self.assertEqual(type(result), tuple)

    def test_classify_number_returns_int_with_d22(self):
        k = 3
        test_image = as_2d_arrays(self.test_set_imgs[0])
        result = self._knn.classify_number(
            k, test_image, self.train_set_imgs, self.train_set_labels, "D22")
        self.assertEqual(type(result), int)

    def test_classify_number_returns_int_with_d23(self):
        k = 3
        test_image = as_2d_arrays(self.test_set_imgs[0])
        result = self._knn.classify_number(
            k, test_image, self.train_set_imgs, self.train_set_labels, "D23")
        self.assertEqual(type(result), int)

    def test_classify_number_raises_exception_with_invalid_dist_measure(self):
        k = 3
        test_image = as_2d_arrays(self.test_set_imgs[0])
        self.assertRaises(
            Exception, self._knn.classify_number, k, test_image, self.train_set_imgs, self.train_set_labels, "F00")

    def test_d22_returns_maximum_of_set_distances(self):
        set1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        set2 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        result = knn._compare_d22(set1, set2)
        expected = 1/9
        self.assertEqual(result, expected)

    def test_d23_returns_average_of_set_distances(self):
        set1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        set2 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        result = knn._compare_d23(set1, set2)
        expected = (1/9) / 2
        self.assertEqual(result, expected)

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
        result = self._knn._result_from_k_nearest(
            k_nearest, self.train_set_labels)
        self.assertEqual(type(result), int)

    def test_point_to_set_distance_returns_correct_distance(self):
        mock = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1]]
        result1 = self._knn._point_to_set_dist(4, 4, mock)
        result2 = self._knn._point_to_set_dist(4, 0, mock)
        result3 = self._knn._point_to_set_dist(3, 3, mock)
        self.assertEqual(result1, 0.0)
        self.assertEqual(result2, 4.0)
        self.assertEqual(result3, sqrt(2))
