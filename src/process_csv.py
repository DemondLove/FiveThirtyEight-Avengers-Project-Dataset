'''
Module to input interim file and export processed file w/ correctly formatted headers
'''
if __name__ == '__main__':
    import sys
    sys.path.append('/Users/Love/Documents/GitHub/msds510/src/msds510')
    import utils
    utils.DictWriter('/Users/Love/Documents/GitHub/msds510/data/interim/avengers_utf8.csv', '/Users/Love/Documents/GitHub/msds510/data/processed/avengers_processed.csv')
    utils.PythonFriendlyHeaders()
