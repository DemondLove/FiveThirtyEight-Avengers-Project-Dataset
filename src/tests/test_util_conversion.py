import unittest

import sys

sys.path.append('/Users/Love/Documents/GitHub/msds510/src/msds510')

from utils.conversion import get_value

from utils.conversion import to_int


class TestToInt(unittest.TestCase):

    def test_float(self):
        self.assertEqual(to_int(4.0), 4)

    def test_invalid_str(self):
        self.assertAlmostEqual(to_int('nine'), None)

    def test_int_input(self):
        self.assertAlmostEqual(to_int(8), 8)


class TestGetValue(unittest.TestCase):
    x = {'a': 1, 'b': 52, 'd': 6}
    y = ['a', 'c', 'd']

    def test_dict_NoValue(self):
        x = {'a': 1, 'b': 52, 'd': 6}
        y = ['a', 'c', 'd']
        self.assertAlmostEqual(get_value(x, 'q'), None)

    def test_dict_valid(self):
        x = {'a': 1, 'b': 52, 'd': 6}
        y = ['a', 'c', 'd']
        self.assertAlmostEqual(get_value(x, 'a'), 1)

    def test_dict_valid(self):
        x = {'a': 1, 'b': 52, 'd': 6}
        y = ['a', 'c', 'd']
        self.assertAlmostEqual(get_value(x, 'b'), 52)

    def test_list_NoValue(self):
        x = {'a': 1, 'b': 52, 'd': 6}
        y = ['a', 'c', 'd']
        self.assertAlmostEqual(get_value(y, 'b'), None)

    def test_list_value(self):
        x = {'a': 1, 'b': 52, 'd': 6}
        y = ['a', 'c', 'd']
        self.assertAlmostEqual(get_value(y, 'd'), 2)
