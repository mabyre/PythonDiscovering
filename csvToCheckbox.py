import csv

fileName = r'C:\Users\Mabyre\Documents\Ionbird\FlyingDatas\2021-0907\temp-007.csv'

with open(fileName, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    #     print(row['first_name'], row['last_name'])

    # rows = reader.
    # print(rows)
