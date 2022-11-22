import csv

fileName = r'.\datas\temp-005.csv'

with open(fileName, newline='') as csvfile:
    csv_file = csv.DictReader(csvfile, delimiter=';')
    for row in csv_file:
        print(dict(row))
