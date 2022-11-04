import csv

fileName = r'D:\Mabyre\Ionbird\FlyingDatas\2021-0907\temp-005.csv'

with open(fileName, newline='') as csvfile:
    csv_file = csv.DictReader(csvfile)
    for row in csv_file:
        print(dict(row))
