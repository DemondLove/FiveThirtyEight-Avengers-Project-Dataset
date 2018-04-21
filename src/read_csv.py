import csv

with open ('/Users/Love/Documents/GitHub/msds510/data/interim/avengers_utf8.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    lines = []
    for line in csv_reader:
        lines.append(line)
    print (lines[161])
