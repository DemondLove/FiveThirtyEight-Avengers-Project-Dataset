'''
Module is used to open avengers.csv, from FiveThirtyEight GitHub: https://github.com/fivethirtyeight/data/tree/master/avengers, already decoded from ISO-8859-1 to UTF-8.
Then export it with proper heading formatting and data cleaning.
'''
if __name__ == '__main__':
    import sys

    sys.path.append('/Users/Love/Documents/GitHub/msds510/src/msds510')
    import utils
    utils.dict_writer(
        '/Users/Love/Documents/GitHub/msds510/data/interim/avengers_utf8.csv',
        '/Users/Love/Documents/GitHub/msds510/data/processed/avengers_processed.csv'
    )

    utils.python_friendly_headers()
