import csv

def DictWriter(input, output):
    with open(input, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(output, 'w') as new_file:
            fieldnames = ['URL', 'Name/Alias', 'Appearances', 'Current?', 'Gender', 'Probationary Introl', 'Full/Reserve Avengers Intro', 'Year', 'Years since joining', 'Honorary', 'Death1', 'Return1', 'Death2', 'Return2', 'Death3', 'Return3', 'Death4', 'Return4', 'Death5', 'Return5', 'Notes']


            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

            csv_writer.writeheader()

            for line in csv_reader:
                csv_writer.writerow(line)

DictWriter('/Users/Love/Documents/GitHub/msds510/data/interim/avengers_utf8.csv', '/Users/Love/Documents/GitHub/msds510/data/processed/avengers_processed.csv')
