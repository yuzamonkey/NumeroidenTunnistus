import unittest
from repositories.data_repository import DataRepository


class TestDataRepository(unittest.TestCase):
    def setUp(self):
        self._dr = DataRepository()

    def test_get_training_imgs_returns_60_000_images(self):
        imgs = self._dr.get_training_imgs()
        self.assertEqual(len(imgs), 60_000)

    def test_get_training_labels_returns_60_000_labels(self):
        labels = self._dr.get_training_labels()
        self.assertEqual(len(labels), 60_000)

    def test_get_testing_imgs_returns_10_000_images(self):
        imgs = self._dr.get_testing_imgs()
        self.assertEqual(len(imgs), 10_000)

    def test_get_testing_labels_returns_10_000_labels(self):
        labels = self._dr.get_testing_labels()
        self.assertEqual(len(labels), 10_000)

    def test_get_all_data_returns_all_data(self):
        tr_imgs, tr_labels, te_imgs, te_labels = self._dr.get_all_data()
        self.assertEqual(len(tr_imgs), 60_000)
        self.assertEqual(len(tr_labels), 60_000)
        self.assertEqual(len(te_imgs), 10_000)
        self.assertEqual(len(te_labels), 10_000)
