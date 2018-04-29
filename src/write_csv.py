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

with open('/Users/Love/Documents/GitHub/msds510/data/interim/avengers_utf8.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    F = open('/Users/Love/Documents/GitHub/msds510/data/interim/avengers_utf8.csv', 'r')
    lines = F.readlines()

    rows = []
    for line in lines:
        row = line.split(',')
        if len(row) == 21:
            rows.append(row)

    fieldnames = rows[0]
    rows = rows[1:]

    fieldnames = [row.lower() for row in fieldnames]
    fieldnames = [row.rstrip() for row in fieldnames]
    fieldnames = [row.strip('?') for row in fieldnames]
    fieldnames = [row.replace('/','_') for row in fieldnames]
    fieldnames = [row.replace(' ','_') for row in fieldnames]

    with open('/Users/Love/Documents/GitHub/msds510/data/processed/avengers_processed.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')

        csv_writer.writerow(fieldnames)
        next(csv_reader)

        for line in csv_reader:
            csv_writer.writerow(line)
