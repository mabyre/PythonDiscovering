"""
 Tree ways reading same CSV file 
"""
import csv

# fileName = r'.\datas\csv-000.csv'
# delim = ','
fileName = r'.\datas\csv-001.csv'
delim = ';'

with open(fileName, 'r') as file:
    reader = csv.reader(file, delimiter=delim)
    for row in reader:
        print(row)

with open(fileName, 'r') as file:
    csv_file = csv.DictReader(file, delimiter=delim)
    for row in csv_file:
        print(dict(row))

# Display Columns Names
# fieldnames : column names
for i in range(len(csv_file.fieldnames)):
    print(i, csv_file.fieldnames[i])

# ['SN', ' Name', ' City']
# ['1', ' Michael', ' New Jersey']
# ['2', ' Jack', ' California']
# {'SN': '1', ' Name': ' Michael', ' City': ' New Jersey'}
# {'SN': '2', ' Name': ' Jack', ' City': ' California'}
# 0 SN
# 1  Name
# 2  City
