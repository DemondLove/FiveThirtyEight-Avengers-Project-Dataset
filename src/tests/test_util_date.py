import unittest

import sys

sys.path.append('/Users/Love/Documents/GitHub/msds510/src/msds510')

import utils.date


class TestGetDateJoined(unittest.TestCase):

    def test_correct(self):
        self.assertEqual(utils.date.get_date_joined('1968', 'Nov-68'), '1968-11-01')
