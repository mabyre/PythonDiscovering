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
# RegEx improuvement
#
# v1.2.1
#
import csv
from os import truncate
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
regExDatasLineToLog = r'^[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2};\d+;\d+;[A-Za-z]{2,}'


# Line with columns v1.9.x
# regExFirstLine = r'milliSeconds;workingTimeMs;currentState;'
# regExDatasLine = r'^[0-9]{1,};[0-9]{1,};[0-9]{1,}'

# -----------------------------------------------------------------------------

# Put these datas in log file
dataToLog = [';mainAutomat_loop;',
             ';RunnableCanBus',
             ';CanBus reset']

# Datas that are not recorded
dataToEvacuate = [';Stand by;',
                  ';Stop;']

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


def printInfoLogAndOtherFile():
    print("\nFile Log:\n" + fileLog)
    print(" - log lines total: " + str(nbLineLogTot))
    print(" - unicode error: " + str(nbUnicodeError))
    print(" - unknown error: " + str(nbUnknownError))

# -----------------------------------------------------------------------------


def readConfigurationFile():
    try:
        fp = open("filterAndSplitFlyingDatasConf.txt", 'r')
        tuple = fp.readline(), fp.readline()  # pack
        fp.close()
        return tuple
    except FileNotFoundError:
        print("Error: File filterAndSplitFlyingDatasConf.txt not founded!")
        quitScript()


def getDestinationNameFile(numFile):
    # Check if file's name is normalized
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
fileDestination, fileLog = getDestinationNameFile(numFile)  # unpack
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
# - Main Loop
# -----------------------------------------------------------------------------

nbLine = 0
nbLineTot = 0
nbLineLog = 0
nbLineLogTot = 0
nbFirstLineColumns = 0
nbUnicodeError = 0
nbUnknownError = 0

line = 'not the end'

while 1:
    while 1:

        #
        # Try to read a line
        #
        try:
            line = fs.readline()
            # if line.isascii():  # ne fonctionne pas
            #     print("is ascii")
            # else:
            #     print("not ascii")
        except UnicodeDecodeError:
            nbUnicodeError += 1
            continue
        except Exception as e:
            print("Exception ", e.__class__, "occurred.")
            print()
        except:
            nbUnknownError += 1
            continue

        if line.strip('\n') == "":
            break

        isLineBoxed = False

        if contains(line, dataToEvacuate):
            continue

        elif re.match(regExFirstLine, line) and isLineBoxed == False:
            if nbFirstLineColumns == 0:
                isLineBoxed = True
                fd.write(line)
                nbLine += 1
            nbFirstLineColumns += 1

        elif contains(line, dataToLog) and isLineBoxed == False:
            isLineBoxed = True
            fl.write(line)
            nbLineLog += 1

        elif nbFirstLineColumns == 1 and isLineBoxed == False:
            if re.match(regExDatasLine, line):
                if re.match(regExDatasLineToLog, line):
                    isLineBoxed = True
                    fl.write(line)
                    nbLineLog += 1
                else:
                    # Line File Datas
                    isLineBoxed = True
                    fd.write(line)
                    nbLine += 1

        elif nbFirstLineColumns == 1 and isLineBoxed == False:
            # Not boxed yet ? It's a Log
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
            fileDestination, unsused0 = getDestinationNameFile(numFile)
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
printInfoLogAndOtherFile()

wait = input("\nPress <ENTER> to continue\n")
