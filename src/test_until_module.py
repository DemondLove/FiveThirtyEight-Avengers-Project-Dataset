records = [
    dict(year='1988', intro='Jun-88'),
    dict(year='1989', intro='May-89'),
    dict(year='2005', intro='5-May'),
    dict(year='2013', intro='13-Nov'),
    dict(year='2014', intro='14-Jan'),
]


import msds510.utils

for loop in records:
    print('Input Record - %s' % loop)
    print ('Date joined - %s' % msds510.utils.get_date_joined(loop['year'], loop['intro']))
    print ('Days since joined - %s' % msds510.utils.days_since_joined(loop['year'], loop['intro']))
