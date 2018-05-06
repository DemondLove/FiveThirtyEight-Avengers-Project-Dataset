import csv


def dict_reader(inputvalue):
    with open(inputvalue, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lines = []
        for line in csv_reader:
            lines.append(line)
