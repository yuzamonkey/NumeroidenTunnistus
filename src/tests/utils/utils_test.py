import unittest
from utils.utils import as_2d_arrays, image_as_2d_string, images_with_threshold, image_with_threshold


class TestUtils(unittest.TestCase):
    def setUp(self):
        self._arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                     10, 11, 12, 13, 14, 15, 16, 17, 18]

    def test_as_2d_array_returns_expected_arrays_with_parameters(self):
        new_arr = as_2d_arrays(self._arr, 9, 2)
        expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [10, 11, 12, 13, 14, 15, 16, 17, 18]]
        self.assertEqual(new_arr, expected)

    def test_as_2d_array_returns_28_by_28_without_parameters(self):
        new_arr = as_2d_arrays(self._arr)
        self.assertEqual(len(new_arr), 28)
        self.assertEqual(len(new_arr[0]), 28)

    def test_images_with_threshold_returns_expected_arrays(self):
        arr1 = self._arr
        arr2 = reversed(self._arr)
        expected1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        expected2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        input_arrays = [arr1, arr2]
        result = images_with_threshold(input_arrays, 10)
        expected_arrays = [expected1, expected2]
        self.assertEqual(result, expected_arrays)

    def test_image_with_threshold_returns_expected_array(self):
        new_arr = image_with_threshold(self._arr, 10)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(new_arr, expected)

    def test_image_as_2d_string_returns_expected_output(self):
        img = [[0, 0, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
        expected = " ○ ○ ● ● ●\n ○ ○ ○ ○ ○\n ● ● ● ● ●\n"
        self.assertEqual(image_as_2d_string(img), expected)
