#!/usr/bin/env python
#
# Filtrer les fichiers issus des données de vol
#
# v1.0.1
import csv
import re

fileSource = r'C:\Users\Mabyre\Nextcloud\TEAM PRODUITS\CUSTOMER SERVICE\FlightDatas\Test-KO-DimancheMatin-2021-09-07-09-16.log'
fileDestination = r'C:\Users\Mabyre\Documents\Ionbird\FlyingDatas\2021-0907\temp-000.csv'

firstLine = False

regEx1 = r'Date Time;Seconds;Milli-seconds;'  # Line with columns
regEx2 = r'^[0-9]{4}-[0-9]{2}-[0-9]{2}'  # Date Time

fs = open(fileSource, 'r')
fd = open(fileDestination, 'w')

nbLine = 0
nbLineSkiped = 0

elements = ['mainAutomat_loop;',
            'Stand by;',
            ';CanBus reset KO FAIL',
            ';RunnableCanBus OK',
			';Stop;',
			';Setup;']


def contains(line, elements):
    i = 0
    while i < len(elements):
        if line.__contains__(elements[i]):
            return True
        i += 1
    return False


while 1:
    line = fs.readline()

    skypeLine = False
    if contains(line, elements):
        skypeLine = True
        nbLineSkiped += 1

    if re.match(regEx1, line):
        firstLine = True
        fd.write(line)

    if bool(firstLine):
        if re.match(regEx2, line):
            firstLine = True
            if not skypeLine:
                fd.write(line)
                nbLine += 1

    # End Of file
    if line == "":
        break

fs.close()
fd.close()

print("File Source: " + fileSource)
print("File Destination: " + fileDestination)
print(" - nb lines: " + str(nbLine))
print(" - skyped lines: " + str(nbLineSkiped))

wait = input("Press <ENTER> to continue")
