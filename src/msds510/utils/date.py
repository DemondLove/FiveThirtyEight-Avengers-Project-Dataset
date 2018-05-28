'''
Module with functions used to covert dates.
'''
from time import strptime

import datetime


def get_month(month, year):
    '''
    Function to pull the month from a formatted date field
    :param month: formatted date
    :param year: full year string
    :return: month of formatted date
    '''
    if int(year) == 1900:
        return ''
    elif int(year) <= 2000:
        return strptime(month, '%b-%y').tm_mon
    else:
        return strptime(month, '%d-%b').tm_mon


def get_date_joined(year, intro):
    '''
    Function to pull the month and year, using get_month function
    :param year: full date string
    :param intro: formatted date
    :return: year and month
    '''
    y = int(year)
    m = get_month(intro, year)
    return str(datetime.date(y, m, 1))
