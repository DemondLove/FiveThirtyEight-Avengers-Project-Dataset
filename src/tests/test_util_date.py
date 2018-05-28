if __name__ == '__main__':
    import unittest

    import msds510.utils

    class TestGetDateJoined(unittest.TestCase):

        def test_correct(self):
            self.assertEquals((msds510.utils.get_date_joined('1968', 'Nov-68'), '1968-11-01')
