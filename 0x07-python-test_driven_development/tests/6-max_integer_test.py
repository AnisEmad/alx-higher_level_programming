#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_none(self):
        self.assertEqual(max_integer([]), None)
    
    def test_max(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([-1, -2 -10]), -1)
        self.assertEqual(max_integer([-1, 1]), 1)
