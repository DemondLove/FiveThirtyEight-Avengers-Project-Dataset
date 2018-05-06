'''
File to read in a csv file
'''
import csv


def list_reader(inputvalue):
    with open(inputvalue, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = []
        for line in csv_reader:
            lines.append(line)
        print(lines[161])
