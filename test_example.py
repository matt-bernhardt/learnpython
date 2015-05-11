#!/usr/env/python

# Test class for Example class
# Author: matt.j.bernhardt@gmail.com
# Version 0.1

# Modules
import unittest
from example import Example

# Variables

# Classes


class TestExample(unittest.TestCase):

    def setUp(self):
        self.foo = Example(1)

    def test_Increment(self):
        self.assertEqual(self.foo.Increment(1), 2)
        self.assertEqual(self.foo.Increment(2), 4)

    def test_Decrement(self):
        self.assertEqual(self.foo.Decrement(1), 0)
        self.assertEqual(self.foo.Decrement(2), -2)

if __name__ == "__main__":
    unittest.main()
