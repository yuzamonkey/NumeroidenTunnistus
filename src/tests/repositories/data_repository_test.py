import unittest
from repositories import data_repository

class TestDataRepository(unittest.TestCase):
    def setUp(self):
        pass

    def test_something_about_something(self):
        siib = 12
        duub = 4
        self.assertEqual(siib - duub, 8)
