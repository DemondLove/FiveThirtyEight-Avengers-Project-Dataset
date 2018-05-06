'''
Use the csv module ot read in csv file using dictionary
'''
import csv

def DictReader(input):
    with open(input, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lines = []
        for line in csv_reader:
            lines.append(line)
