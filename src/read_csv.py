import csv

def Reader(input):
    with open(input, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = []
        for line in csv_reader:
            lines.append(line)
        print (lines[161])
