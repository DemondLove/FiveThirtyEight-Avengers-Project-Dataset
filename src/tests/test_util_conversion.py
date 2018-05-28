if __name__ == '__main__':
    import unittest

    from util import get_value

    from util import to_int

    import msds510.utils

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
            self.assertAlmostEqual(get_value(x, 'q'), None)

        def test_dict_valid(self):
            self.assertAlmostEqual(get_value(x, 'a'), 1)

        def test_dict_valid(self):
            self.assertAlmostEqual(get_value(x, 'b'), 52)

        def test_list_NoValue(self):
            self.assertAlmostEqual(get_value(y, 'b'), None)

        def test_list_value(self):
            self.assertAlmostEqual(get_value(y, 'd'), 2)

        def test_missinginputs(self):
            self.assertRaises(NameError, get_value())
