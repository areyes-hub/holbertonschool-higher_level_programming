#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_normal_case(self):
        arr = [1, 2, 3, 6, 5, 9, 4]
        self.assertEqual(max_integer(arr), 9)
    def test_negative_number(self):
        arr = [-1, -2, -3, -4, -5, -6]
        self.assertEqual(max_integer(arr), -1)
    def test_single_element(self):
        arr = [6]
        self.assertEqual(max_integer(arr), 6)
    def test_empty_list(self):
        arr = []
        self.assertEqual(max_integer(arr), None)
    def test_mixed_numbers(self):
        arr = [-1, -3, 6, -12, -76, 2]
        self.assertEqual(max_integer(arr), 6)

if __name__ == "__main__":
    unittest.main()