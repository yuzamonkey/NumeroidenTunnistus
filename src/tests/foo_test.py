import unittest

class TestFoo(unittest.TestCase):
  def setUp(self):
    print("TEST SETUP")

  def test_something_about_something(self):
    foo = 3
    bar = 4
    sum = foo + bar
    self.assertEqual(sum, 7)