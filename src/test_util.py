if __name__ == '__main__':
    import unittest

    from util import get_value

    from util import to_int

    class Testto_int(unittest.TestCase):

        def test_float(self):
            #Test a float to return int
            self.assertEqual(to_int(4.0), 4)
        def test_invalid_str(self):
            self.assertAlmostEqual(to_int('nine'), None)
        def test_int_input(self):
            self.assertAlmostEqual(to_int(8), 8)
    #
    # class Testget_value(unittest.TestCase):
    #     x = {'a': 1, 'b': 52, 'd': 6}
    #     y = ['a', 'c', 'd']
    #     pass

# print(get_value(x, 'q'))
# # Out[1]:  None
#
# print(get_value(x, 'a'))
# # Out[2]:  1
#
# print(get_value(x, 'b'))
# # Out[3]:  52
#
# print(get_value(y, 'b'))
# # Out[4]:  None
#
# print(get_value(y, 'd'))
# Out[5]:  2
