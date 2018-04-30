from time import strptime
import datetime

def get_month(intro):
    if '88' in intro:
        return strptime(intro,'%b-%y').tm_mon
    elif '89' in intro:
        return strptime(intro,'%b-%y').tm_mon
    else:
        return strptime(intro,'%d-%b').tm_mon

def get_date_joined(year, intro):
    y = int(year)
    m = get_month(intro)
    return datetime.date(y, m, 1)

def days_since_joined(year, intro):
    d0 = get_date_joined(year, intro)
    d1 = datetime.date.today()
    delta = d1 - d0
    return delta.days

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

def PythonFriendlyHeaders():
    import csv
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
        fieldnames.append('month_joined')

        def get_month(month, year):
            if int(year) == 1900:
                return ''
            elif int(year) <=2000:
                return strptime(month,'%b-%y').tm_mon
            else:
                return strptime(month,'%d-%b').tm_mon
        def return_bool(input):
            if input == '':
                pass
            elif input == 'YES':
                return 'True'
            else:
                return 'False'

        with open('/Users/Love/Documents/GitHub/msds510/data/processed/avengers_processed.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')

            csv_writer.writerow(fieldnames)
            next(csv_reader)

            for line in csv_reader:
                line.append(get_month(line[6], line[7]))
                line[3] = return_bool(line[3])
                line[10] = return_bool(line[10])
                line[11] = return_bool(line[11])
                line[12] = return_bool(line[12])
                line[13] = return_bool(line[13])
                line[14] = return_bool(line[14])
                line[15] = return_bool(line[15])
                line[16] = return_bool(line[16])
                line[17] = return_bool(line[17])
                line[18] = return_bool(line[18])
                line[19] = return_bool(line[19])
                csv_writer.writerow(line)
