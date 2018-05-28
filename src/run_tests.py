'''
Module to run Unit Tests.
'''
import unittest

import sys

sys.path.append('/Users/Love/Documents/GitHub/msds510/src/tests')

import test_util_date

import test_util_conversion

import test_avenger


def unittesting():
    '''
    Function to run test modules
    :return: Test results
    '''
    def suite():
        '''
        Consolidates all of the Tests folder contents.
        '''
        test_suite = unittest.TestSuite()
        test_suite.addTest(unittest.makeSuite(test_util_date.TestGetDateJoined))
        test_suite.addTest(unittest.makeSuite(test_util_conversion.TestToInt))
        test_suite.addTest(unittest.makeSuite(test_util_conversion.TestGetValue))
        test_suite.addTest(unittest.makeSuite(test_avenger.TestAvengerClass))
        return test_suite

    TestTime = suite()
    runner = unittest.TextTestRunner()
    runner.run(TestTime)


if __name__ == '__main__':
    unittesting()
