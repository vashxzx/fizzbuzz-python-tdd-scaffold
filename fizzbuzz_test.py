import unittest

from fizzbuzz import fb

class TestFB(unittest.TestCase):

    def test_fb(self):

        self.assertEqual(fb(1),"1")

        self.assertEqual(fb(3),"Fizz")

        self.assertEqual(fb(5),"Buzz")

        self.assertEqual(fb(15),"FizzBuzz")
