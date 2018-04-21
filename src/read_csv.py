import csv

def job(robin):
    with open(robin, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = []
        for line in csv_reader:
            lines.append(line)
        print (lines[161])
