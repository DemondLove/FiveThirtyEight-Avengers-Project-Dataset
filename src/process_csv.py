if __name__ == '__main__':
    import sys


    sys.path.append('/Users/Love/Documents/GitHub/msds510/src/msds510')
    import utils
    utils.dict_writer(
        '/Users/Love/Documents/GitHub/msds510/data/interim/avengers_utf8.csv',
        '/Users/Love/Documents/GitHub/msds510/data/processed/avengers_processed.csv'
    )

    utils.python_friendly_headers()
