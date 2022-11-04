#!/usr/bin/env python
#
# Filter files comming from flying datas
# loop to create as many files
#
# The aim is to distinguish real flyingdatas to draw graphs
#
# Configuration file : filterAndSplitFlyingDatasConf.txt
# To specify path where are flying datas
# - first line the flynig datas path
# - second line the flying datas destination path
#
# v1.2
#
import csv
import re
from pathlib import Path
import argparse

# -----------------------------------------------------------------------------
# Parsing arguments
# -----------------------------------------------------------------------------

parser = argparse.ArgumentParser(description="Filter and Split Flying Datas")
parser.add_argument("flyingDatasFileName")
args = parser.parse_args()

# -----------------------------------------------------------------------------

# Line with columns v1.8.x
regExFirstLine = r'Date Time;Seconds;Milli-seconds;'
regExDatasLine = r'^[0-9]{4}-[0-9]{2}-[0-9]{2}'  # Date Time

# Line with columns v1.9.x
# regExFirstLine = r'milliSeconds;workingTimeMs;currentState;'
# regExDatasLine = r'^[0-9]{1,};[0-9]{1,};[0-9]{1,}'

# -----------------------------------------------------------------------------

# Put these lines in log file
elementsToLog = [';mainAutomat_loop;',
                 ';Stand by;',
                 ';Stop;',
                 ';RunnableCanBus',
                 ';CanBus reset']

elementsToLogFlying = [';RunnableCanBus',
                       ';CanBus reset',
                       ';JSON was readen',
                       ';CanBus setBitrate']

# -----------------------------------------------------------------------------


def quitScript():
    wait = input("\nPress <ENTER> to continue\n")


def contains(line, elements):
    i = 0
    while i < len(elements):
        if line.__contains__(elements[i]):
            return True
        i += 1
    return False


def substractLast(str, car):
    i = str.rfind(car)
    # car not founded in str
    if i == -1:
        return str
    end = len(str)
    s = str[0:i] + str[i+1:end]
    return s

# -----------------------------------------------------------------------------


def printInfoSourceFile():
    print("\nFile Source:\n" + fileSource)
    print(" - lines total: " + str(nbLineTot))
    print(" - number of files: " + str(numFile))


def printInfoDestinationFile():
    print("\nFile Destination " + str(numFile) + ": \n" + fileDestination)
    print(" - number of lines: " + str(nbLine))
    print(" - number of log lines: " + str(nbLineLog))


def printInfoLogFile():
    print("\nFile Log:\n" + fileLog)
    print(" - log lines total: " + str(nbLineLogTot))

# -----------------------------------------------------------------------------


def readConfigurationFile():
    try:
        fp = open("filterAndSplitFlyingDatasConf.txt", 'r')
        tuple = fp.readline(), fp.readline()  # pack
        return tuple
    except FileNotFoundError:
        print("Error: File pathToFlyingDatas.txt not founded!")
        quitScript()


def getNameFileDestination(numFile):
    fileName1 = Path(fileSource).name.split('_')
    lg = len(fileName1)
    if lg == 4:
        fileDestination = fileName1[0] + '-' + fileName1[1] + '-' + fileName1[2] + \
            "-{:03d}".format(numFile) + '.csv'
        fileLog = fileName1[0] + '-' + fileName1[1] + \
            '-' + fileName1[2] + "_exomo.log"
    else:
        fileName1 = Path(fileSource).stem
        fileDestination = fileName1 + "-{:03d}".format(numFile) + ".csv"
        fileLog = fileName1 + "_exomo.log"

    tuple = fileDestination, fileLog
    return tuple


# -----------------------------------------------------------------------------
# Open file source and file destination
# -----------------------------------------------------------------------------

pathSource, pathDestination = readConfigurationFile()  # unpack
pathSource = substractLast(pathSource, '\n')
pathDestination = substractLast(pathDestination, '\n')

fileSource = pathSource + args.flyingDatasFileName
try:
    fs = open(fileSource, 'r')
except FileNotFoundError:
    print("Error: File source not founded " + fileSource)
    quitScript()

numFile = 1
fileDestination, fileLog = getNameFileDestination(numFile)  # unpack
fileDestination = pathDestination + fileDestination
try:
    fd = open(fileDestination, 'w+')
except FileNotFoundError:
    print("Error: File destination not founded " + fileDestination)
    quitScript()

fileLog = pathDestination + fileLog
try:
    fl = open(fileLog, 'w+')
except FileNotFoundError:
    print("Error: File not founded " + fileLog)
    quitScript()

# -----------------------------------------------------------------------------

nbLine = 0
nbLineTot = 0
nbLineLog = 0
nbLineLogTot = 0
nbFirstLineColumns = 0

while 1:
    while 1:
        line = fs.readline()

        if line.strip('\n') == "":
            break

        isLineBoxed = False

        if re.match(regExFirstLine, line) and isLineBoxed == False:
            nbFirstLineColumns += 1
            if nbFirstLineColumns == 1:
                isLineBoxed = True
                fd.write(line)
                nbLine += 1

        elif nbFirstLineColumns == 1 and isLineBoxed == False:
            if re.match(regExDatasLine, line):
                if not contains(line, elementsToLogFlying):
                    isLineBoxed = True
                    fd.write(line)
                    nbLine += 1
                else:
                    isLineBoxed = True
                    fl.write(line)
                    nbLineLog += 1

        elif contains(line, elementsToLog) and isLineBoxed == False:
            isLineBoxed = True
            fl.write(line)
            nbLineLog += 1

        # Last thing to do is to Log line
        elif nbFirstLineColumns == 0 and isLineBoxed == False:
            isLineBoxed = True
            fl.write(line)
            nbLineLog += 1

        #
        # End Of intermediate file
        #
        if nbFirstLineColumns == 2:
            fd.close()
            printInfoDestinationFile()
            nbLine = 0
            nbLineLogTot += nbLineLog
            nbLineLog = 0
            nbFirstLineColumns = 0

            # Open new file destination
            numFile += 1
            fileDestination, tmp0 = getNameFileDestination(numFile)
            fileDestination = pathDestination + fileDestination
            fd = open(fileDestination, 'w+')
            continue

        nbLineTot += 1

    #
    # End Of file
    #
    if line == "":
        nbLineLogTot += nbLineLog
        fd.close()
        fl.close()
        break

fs.close()

printInfoDestinationFile()
printInfoSourceFile()
printInfoLogFile()

wait = input("\nPress <ENTER> to continue\n")
