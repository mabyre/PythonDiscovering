#!/usr/bin/env python
#
# Filtrer les fichiers issus des données de vol
# boucler pour créer les fichiers temp-001 002 003 ...
#
# v1.1
#
import csv
import re
from pathlib import Path

fileSource = r'C:\Users\Mabyre\Nextcloud\TEAM PRODUITS\CUSTOMER SERVICE\FlightDatas\0x3414B59254B6_2021-05-06_15-47-19_exomoOriginal.log'
pathDestination = r'C:\Users\Mabyre\Documents\Ionbird\FlyingDatas'

nbFirstLineColumns = 0

regExFirstLine = r'Date Time;Seconds;Milli-seconds;'  # Line with columns
regExDatasLine = r'^[0-9]{4}-[0-9]{2}-[0-9]{2}'  # Date Time

# ------------------------------------------------------------------------------


def quitScript():
    wait = input("\nPress <ENTER> to continue\n")


def nameFileDestination(numFile):
    fileName1 = Path(fileSource).name.split('_')
    fileDestination = pathDestination + '\\' + fileName1[0] + '\\' + \
        fileName1[0] + '-' + fileName1[1] + '-' + fileName1[2] + \
        "-{:03d}".format(numFile) + '.csv'
    return fileDestination


def contains(line, elements):
    i = 0
    while i < len(elements):
        if line.__contains__(elements[i]):
            return True
        i += 1
    return False


def printInfoFile():
    print("File Destination " + str(numFile) + ": " + fileDestination)
    print(" - skyped lines: " + str(nbLineSkiped))
    print(" - number lines: " + str(nbLine))


# ------------------------------------------------------------------------------

numFile = 1
fileDestination = nameFileDestination(numFile)

# ------------------------------------------------------------------------------
# Open files source and destination
# ------------------------------------------------------------------------------

fileNotFounded = True

try:
    fs = open(fileSource, 'r')
except FileNotFoundError:
    print("Error: File not founded " + fileSource)
    quitScript()

fd = open(fileDestination, 'w')

# ------------------------------------------------------------------------------

nbLine = 0
nbLineSkiped = 0

elements = ['mainAutomat_loop;',
            'Stand by;',
            ';CanBus reset KO FAIL',
            ';RunnableCanBus OK',
            ';Stop;',
            ';Setup;',
            ';Activity',
            ';MicroSd created']


while 1:
    while 1:
        line = fs.readline()

        skypeLine = False
        if contains(line, elements):
            skypeLine = True
            nbLineSkiped += 1

        if re.match(regExFirstLine, line):
            nbFirstLineColumns += 1
            if nbFirstLineColumns == 1:
                fd.write(line)
                nbLine += 1

        if nbFirstLineColumns == 1:
            if re.match(regExDatasLine, line):
                if not skypeLine:
                    fd.write(line)
                    nbLine += 1

        # End Of file intermediaire
        if nbFirstLineColumns == 2:
            fd.close()
            printInfoFile()
            nbLine = 0
            nbLineSkiped = 0
            nbFirstLineColumns = 0

            # Open new file
            numFile += 1
            fileDestination = nameFileDestination(numFile)
            fd = open(fileDestination, 'w')
            break

        # End Of file num #
        if line == "":
            fd.close()
            break

    # End Of file
    if line == "":
        break

fs.close()

printInfoFile()
print("\nFile Source: " + fileSource)
print(" - number of files: " + str(numFile))

wait = input("\nPress <ENTER> to continue\n")
