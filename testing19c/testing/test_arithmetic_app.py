import unittest
from testing19c.arithmetic.arithmetic_app import *


class Test_Arithmetic(unittest.TestCase):
    def test_add(self):
         a=arithmetic()
         actual=a.add(2,3)
         expected=5
         self.assertEqual(expected,actual)


    def test_sub(self):
        b = arithmetic()
        actual = b.sub(5, 3)
        expected = 2
        self.assertEqual(expected, actual)

    def test_mul(self):
        c = arithmetic()
        actual = c.mul(2, 3)
        expected = 6
        self.assertEqual(expected, actual)
    def test_div(self):
        d = arithmetic()
        actual = d.div(2, 2)
        expected = 1
        self.assertEqual(expected, actual)