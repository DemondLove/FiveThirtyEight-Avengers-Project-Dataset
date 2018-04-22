import csv

def dark(knight):
    with open(knight, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lines = []
        for line in csv_reader:
            lines.append(line)
        print (lines[159])
