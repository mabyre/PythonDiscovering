#!/usr/bin/env python3
# -------------------------------------------------------------------------------
# exomoTools : Some tools for Exomo stuff
# Librairy installation :
# >pip install timeout
# Windows : import in comment cause compilation error
# -------------------------------------------------------------------------------

import subprocess
import platform
import os
import re
from pathlib import Path
import json
import glob
from zipfile import ZipFile
import sys
import shutil
# from timeout import timeout
import time
import signal
from serial import Serial
import serial
from datetime import datetime


class runAndLogCommand(object):
    """
    # inspired from https://stackoverflow.com/a/4417735
    # Usage sample :
        cmd = runAndLogCommand()
        _logPath = os.path.join(os.getcwd(), "tmp.log")
        cmd.runAndLog(cmd="ping 127.0.0.1 -c 3", _logPath=_logPath)
        print(cmd.returnCode)  # should be 0
        with open(_logPath, 'r') as fRead:
            for line in fRead:
                print(line, '')
    """

    def __init__(self):
        self.process = None
        self.returnCode = 0
        self.cmd = ""

    def runAndLog(self, cmd, logPath):
        self.cmd = cmd
        with open(logPath, 'w') as fWrite:
            for line in self.run():
                print(line, end='')
                fWrite.write(line)

    def run(self):
        self.process = subprocess.Popen(
            self.cmd,
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        for stdoutLine in iter(self.process.stdout.readline, ''):
            yield stdoutLine
        self.process.stdout.close()
        self.returnCode = self.process.wait()


def getBuildInfos():
    """
    Read/store build ìnformationsas JSON text
    """
    jsonFile = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '.buildPaths' + platform.system() + '.json'
    )
    jsonObject = None

    _projectFolder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )

    if (os.path.exists(jsonFile)):
        # print("Reading previously found paths for shared folders")
        # Open and read JSON file
        with open(jsonFile, 'r') as fRead:
            jsonObject = json.load(fRead)

    else:
        # print("Looking for shared folders... (may take some time)")

        # Looking for directory "./scripts/maintenanceTools"
        _maintenanceToolsFolder = os.path.join(
            _projectFolder, 'scripts', 'maintenanceTools'
        )

        # Looking for directory "...../TEAM PRODUITS/CUSTOMER SUCCESS/FirmwareAndDocumentationHistory"
        _deliveryFolder = getFolderTree(
            "TEAM PRODUITS", "CUSTOMER SUCCESS", "FirmwareAndDocumentationHistory")
        if _deliveryFolder is None:
            print('Could not find folder ', os.path.join("TEAM PRODUITS",
                  "CUSTOMER SUCCESS", "FirmwareAndDocumentationHistory"))
            _deliveryFolder = os.path.join(
                _projectFolder, 'FirmwareAndDocumentationHistory')

        # Looking for directory "./firmware"
        _firmwareFolder = os.path.join(_projectFolder, 'firmware')

        # Data to be written
        jsonObject = {
            "_maintenanceToolsFolder": _maintenanceToolsFolder,
            "_deliveryFolder": _deliveryFolder,
            "_firmwareFolder": _firmwareFolder
        }

        # Serialize jsonand write to file
        with open(jsonFile, 'w') as fWrite:
            fWrite.write(json.dumps(jsonObject, indent=4))

    # print('Content of the file', jsonFile, ':', json.dumps(jsonObject, sort_keys=True, indent=4))
    createDirIfNotExists(jsonObject['_maintenanceToolsFolder'])
    createDirIfNotExists(jsonObject['_firmwareFolder'])
    createDirIfNotExists(jsonObject['_deliveryFolder'])

    jsonObject['_projectFolder'] = _projectFolder
    return jsonObject


def getVersion():
    """
    Looking for version number in platformio.ini
    """
    version = ""
    f = open(os.path.join(os.path.dirname(
        __file__), '..', 'platformio.ini'), 'r')
    # looking for the following line : -D COPILOT_VERSION="\"1.8.8\""
    searchObj = re.search(r'-D COPILOT_VERSION="\\"([^"]*)\\"', f.read(), re.S)
    if searchObj:
        version = searchObj.group(1)
    return version


def getPort(portName):
    """
    Looking for the port where is connected the device (if not None, simply returns the given string).
    \nReturns the port where arduino is connected.
    \nAsk for a choice if several ports found
    """

    if portName is None:

        system = platform.system()
        searchObj = None
        if system == 'Windows':
            # --------------------
            # Working on Windows !
            # --------------------

            cmdRes = os.popen("mode").read()
            #
            # Result sample
            #
            # Statut du peripherique COM18:
            # -----------------------------
            #     Baud :            115200
            #     Parite :          None
            #     Bits de donnees : 8
            #     Bits d'arret :    1
            #     Temporisation :   OFF
            #     XON/XOFF :        OFF
            #     Protocole CTS :   OFF
            #     Protocole DSR :   OFF
            #     Sensibilite DSR : OFF
            #     Circuit DTR :     OFF
            #     Circuit RTS :     ON
            #
            # Statut du peripherique CON:
            # ---------------------------
            #     Lignes :          28
            #     Colonnes :        201
            #     Vitesse clavier : 31
            #     Delai clavier :   1
            #     Page de codes :   850
            #
            # -> We are looking for "COMxx:\n-----...--\n    Baud :            115200" ...

            searchObj = re.findall(
                r'.* (COM\d*):(?:(?!:$)(?!115200).|\n)*115200', cmdRes)

        elif system == 'Darwin':
            # --------------------
            # Working on MacOS !"
            # --------------------

            cmdRes = os.popen("ls /dev/cu.*").read()
            #
            # Result sample
            #
            # /dev/cu.Bluetooth-Incoming-Port
            # /dev/cu.URT1
            # /dev/cu.URT2
            # /dev/cu.usbmodem14601
            # /dev/cu.usbmodem14301
            #
            # -> We are looking for "cu.usbmodem"...
            #
            searchObj = re.findall(r'(/dev/cu.usbmodem[^ \n]*)', cmdRes)

        if not searchObj is None:
            if len(searchObj) == 0:
                portName = None
            elif len(searchObj) == 1:
                portName = searchObj[0]
            else:
                print("Several ports found :")
                i = 0
                for value in searchObj:
                    i = i + 1
                    print('\t', i, value)
                try:
                    choice = int(input("Your choice ? : "))
                except:
                    choice = 0
                if choice > i or choice < 1:
                    portName = None
                else:
                    portName = searchObj[choice-1]

    # --------------------
    # Exiting
    return portName


def createDirIfNotExists(dirPath):
    """
    Creates a folder if it dos not exists
    """
    if not os.path.isdir(dirPath):
        print("Creating directory ", dirPath)
        os.mkdir(dirPath)


def searchDirs(rootFolder, dirName1, dirName2):
    """
    Looking for a directory "dirName1/dirName2"
    """
    for dirpath, dirnames, filenames in os.walk(rootFolder):
        for dir in dirnames:
            if dir == dirName1:
                for dirpath, dirnames, filenames in os.walk(os.path.join(dirpath, dir)):
                    for dir in dirnames:
                        if dir == dirName2:
                            return os.path.join(dirpath, dir)
    return None


def getFolderTree(dirName1, dirName2, dirName3):
    """
    Looks for a directory "dirName1/dirName2" and returns a sub dir dirName3
    """
    retPath = searchDirs(
        Path.home(), dirName1, dirName2)
    if not retPath is None:
        retPath = os.path.join(retPath, dirName3)
        createDirIfNotExists(retPath)
    return retPath


def removeFilesByPattern(pattern):
    """
    Remove files by matching pattern
    """
    fileList = glob.glob(pattern)
    for filePath in fileList:
        os.remove(filePath)


def zipFolder(_folderPath, _zipFilePath):
    """
    Delete and create a ZIP file relative to the given folder, excluding regexp
    """
    if os.path.exists(_zipFilePath):
        os.remove(_zipFilePath)
    _curDir = os.getcwd()
    os.chdir(_folderPath)
    with ZipFile(_zipFilePath, 'w') as zip:
        for path, directories, files in os.walk('.'):
            for f in files:
                fileName = os.path.join(path, f)
                if not re.search(r'.*\.code-workspace|.*__pycache__.*|.*[/\\]firmware[/\\].*|.*\.pio[/\\]build[/\\].*|.*\.git[/\\].*|\.DS_Store|\.vscode[/\\].*|.*\.buildInfos_.*\.json', fileName):
                    zip.write(fileName)
    print('-> ' + _zipFilePath + ' has been created.')
    os.chdir(_curDir)


def resetProcessor(_port):
    """
    NB : cette séquence sera inversée sur la version B de la carte EXOMO/Hardtech
    """
    print("-> Sending reset sequence...")

    # Default for Arduino : SERIAL_8N1 (8 -> bits of data, N -> none, without parity, 1 -> bit of stop)
    s = Serial(port=_port,
               baudrate=115200,
               bytesize=8,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               timeout=None
               )
    s.write(str.encode(r'AT+PIO21'))
    time.sleep(1)
    s.write(str.encode(r'AT+PIO20'))
    time.sleep(0.1)
    s.write(str.encode(r'AT+PIO21'))
    s.close()
    """
    In verbose/debug mode, we should have : 
        linux_pty.py: Read: b'AT+PIO21'
        ble_interface.py: Sending b'AT+PIO21'
        ble_interface.py: Received notify from 17: bytearray(b'OK+PIO2:1')
        linux_pty.py: Write: bytearray(b'OK+PIO2:1')
        linux_pty.py: Read: b'AT+PIO20'
        ble_interface.py: Sending b'AT+PIO20'
        ble_interface.py: Received notify from 17: bytearray(b'OK+PIO2:0')
        linux_pty.py: Write: bytearray(b'OK+PIO2:0')
        linux_pty.py: Read: b'AT+PIO21'
        ble_interface.py: Sending b'AT+PIO21'
        ble_interface.py: Received notify from 17: bytearray(b'OK+PIO2:1')
        linux_pty.py: Write: bytearray(b'OK+PIO2:1')

    But with windows version, at least in a parallel virtual machine :
        windows_com0com.py: Read: b'AT+PIO21'
        ble_interface.py: Sending b'AT+PIO21'
        windows_com0com.py: Read: b'AT+PIO20'
        ble_interface.py: Sending b'AT+PIO20'
        windows_com0com.py: Read: b'AT+PIO21'
        ble_interface.py: Sending b'AT+PIO21'
    """
    """
    # Another approach, same result :
    if platform.system() == 'Windows':
        os.system(r'cmd /c "echo | set /p=AT+PIO21 > COM9"')
        time.sleep(1)
        os.system('cmd /c "echo | set /p=AT+PIO20> COM9"')
        time.sleep(0.1)
        os.system('cmd /c "echo | set /p=AT+PIO21> COM9"')
    else:
        os.popen(r'printf %s AT+PIO2>'+_port)
        time.sleep(1)
        os.popen(r'printf %s AT+PIO20>'+_port)
        time.sleep(0.1)
        os.popen(r'printf %s AT+PIO21>'+_port)
    """


def upload(_firmware, _port, _bBle, _bVerbose, _bSilent):
    """
    Upload and loop maximum 10 times if upload fails
    Each upload will have a timeout of 300 seconds
    """

    if not os.path.exists(_firmware):
        print(_firmware, 'not found')
        return 1

    print('-> ' + 'Will upload ' + _firmware + ' on port ' + _port)
    _count = 0
    _retVal = 0

    _conf = os.path.join(
        Path.home(), ".platformio", "packages", "tool-avrdude", "avrdude.conf"
    )

    _cmd = getAvrdudePath()
    _cmd = _cmd + " -P " + _port
    _cmd = _cmd + " -C " + _conf
    _cmd = _cmd + " -D -U flash:w:" + _firmware + ":i"
    _cmd = _cmd + " -p atmega2560"
    _cmd = _cmd + " -b 115200"
    _cmd = _cmd + " -c wiring"
    #_cmd = _cmd + " -c stk500"
    _cmd = _cmd + " -v"
    # _cmd = _cmd + " -vvv"

    while (not _retVal == 0 or _count == 0) and _count < 10:
        _count = _count + 1
        print("-> Try upload : ", _count)
        if _bVerbose:
            print(_cmd)

        # reset
        if _bBle:
            resetProcessor(_port)

        # upload
        p = subprocess.Popen(_cmd, shell=True)

        # Run with timeout
        @timeout(300)
        def runWithTimeout():
            p.wait()

        try:
            runWithTimeout()
            _retVal = p.returncode
        except:
            if platform.system() == 'Windows':
                os.popen('PowerShell -Command "Stop-Process -Name avrdude"')
            else:
                os.popen(
                    "cmd=\"kill `ps -a| grep avrdude | grep -v grep | sed -E 's/[ ]*([^ ]*) .*/\\1/g'`\";$cmd;")
            time.sleep(1)
            print("\n\n--- Timeout reached ! ---\n\n")
            _retVal = 1

    # The end
    msg = ''
    if _retVal == 0:
        if _count == 1:
            msg = "Upload successfull after " + str(_count) + " try."
        else:
            msg = "Upload successfull after " + str(_count) + " tries."
    else:
        msg = "Upload failed after " + str(_count) + " tries."

    say(msg, _bSilent)
    return _retVal


def transformLine(line):

    # 2021-11-09 17:21:57;10;10001; -> yyyy-mm-dd hh:mm:ss;s;ms;
    line = re.sub(
        r'[0-9][0-9][0-9][0-9]-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2};[^;]*;[^;]*;',
        'yyyy-mm-dd hh:mm:ss;s;ms;', line)

    # 2021-08-13 13:02:30 -> yyyy-mm-dd hh:mm:ss
    line = re.sub(
        r'[0-9][0-9][0-9][0-9]-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}',
        'yyyy-mm-dd hh:mm:ss', line)

    # 2021-08-13-13-02-30 ->  yyyy-mm-dd-hh-mm-ss
    line = re.sub(
        r'[0-9][0-9][0-9][0-9]-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}',
        'yyyy-mm-dd-hh-mm-ss', line)

    # :PASS -> 	[PASSED]
    line = re.sub(
        r':PASS',
        '\t[PASSED]', line)

    # :FAIL -> 	[FAILED]
    line = re.sub(
        r':FAIL',
        '\t[FAILED]', line)

    # test/unity_xmem/unity_xmem.cpp:109:test_xmem_selfTest	[PASSED]
    # unity_xmem:test_xmem_selfTest	[PASSED]

    # test\unity_cruiseSlope\unity_cruiseSlope.cpp:17::INFO: USE_ANALOGREAD_SIMULATION is equal to 1: OK
    # -> unity_cruiseSlope::INFO: USE_ANALOGREAD_SIMULATION is equal to 1: OK
    line = re.sub(
        r'.*[\/\\](unity_[^\/\\]*).cpp:[^:]*:',
        r'\g<1>:', line)

    return line


def runAndLog(_target, _port, _bBle, _env, _bLog, _bVerbose, _bSilent):
    """
    Run and log a platformio command
    """

    _logPath = os.path.join(
        os.getcwd(), "test",  _target, _target + ".log"
    )
    if _target == 'main':
        _logPath = os.path.join(
            os.getcwd(), datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + "_main" + ".log")

    # reset
    if _bBle:
        resetProcessor(_port)

    if _bBle or not _target.startswith("unity_"):
        _cmd = "platformio device monitor"
        _cmd = _cmd + " --port " + _port
        _cmd = _cmd + " --echo"
        _cmd = _cmd + " -f log2file"
        # will generate "platformio-device-monitor-%date%.log"

        if _bVerbose:
            print(_cmd)

        # Launch process
        p = subprocess.Popen(_cmd, stderr=subprocess.STDOUT, shell=True)

        # Get log file
        fileList = glob.glob(os.path.join(
            os.getcwd(), "platformio-device-monitor-*.log"))
        logFilePath = ''
        for filePath in fileList:
            logFilePath = filePath
            break

        # Timeout or simple wait
        if _bBle:
            # nb : "pio test" does not woprk thru BLE : "OSError: [Errno 25] Inappropriate ioctl for device"
            # that is why we use this workaround here ...

            # Run with timeout
            @timeout(30)
            def runWithTimeout(p):
                p.wait()

            try:
                runWithTimeout(p)
                _retVal = p.returncode
            except:
                p.terminate()
                time.sleep(1)
                print("\n\n--- Timeout reached ! ---\n\n")
                _retVal = 0
        else:
            p.wait()
            _retVal = p.returncode

        # rename and move .log if exists
        if _bLog:
            shutil.move(logFilePath, _logPath + 'tmp')
        else:
            os.remove(logFilePath)

    else:
        # nb : "pio test" does not woprk thru BLE : "OSError: [Errno 25] Inappropriate ioctl for device"

        print('-> ' + 'Will monitor on port ' + _port +
              ' and store the result in ' + _logPath)
        _cmd = "platformio test"
        _cmd = _cmd + " --filter " + _target
        _cmd = _cmd + " --environment " + _env
        _cmd = _cmd + " --test-port " + _port
        _cmd = _cmd + " --without-building"
        _cmd = _cmd + " --without-uploading"

        if _bVerbose:
            print(_cmd)

        # Runs the command, show sstdout and stores it to file
        runAndLogCmd = runAndLogCommand()
        runAndLogCmd.runAndLog(cmd=_cmd, logPath=_logPath + 'tmp')
        _retVal = runAndLogCmd.returnCode

    # Teansforms output file for furthur git comparaison
    if _bLog:
        with open(_logPath, 'w') as fWrite:
            with open(_logPath + 'tmp', 'r') as fRead:
                for line in fRead:
                    fWrite.write(transformLine(line))
    os.remove(_logPath + 'tmp')

    # The end
    msg = ''
    if _retVal == 0:
        msg = "Program ran successfully."
    else:
        msg = "Program ran with errors."

    say(msg, _bSilent)
    return _retVal


def say(tx, bSilent):
    """
    Make Python speak
    From https://stackoverflow.com/a/59118441
    """
    print(tx)
    if bSilent:
        return
    syst = platform.system()
    if syst == 'Windows':
        os.system('PowerShell -Command "Add-Type -AssemblyName System.speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.SelectVoice(\'Microsoft Zira Desktop\'); $speak.Speak(\'' + tx + '\');"')
    elif syst == 'Darwin':
        os.system('say -v Alex %s' % tx)
    else:
        # do nothing
        return


def getAvrdudePath():
    """
    returns the path for avrdude executable
    """
    avrdudePath = ''
    fileList = glob.glob(os.path.join(
        Path.home(), ".platformio", "packages", "tool-avrdude", "**", "avrdude*"
    ), recursive=True)

    for filePath in fileList:
        if not filePath.endswith(".conf"):
            avrdudePath = filePath
    return avrdudePath


def build(_target, _env, _savedFirmware, _maintenanceToolsFolder, _deliveryFolder, _version, _bVerbose, _bSilent):
    """
    Build a specific firmware
    """

    cleanTmpFiles(_bVerbose)

    # ---------------------------------------
    # Transform platformio.ini
    fRead = open("platformio.ini", "r")
    fWrite = open("platformio.ini_tmp", "w")

    for line in fRead:
        line = line.replace(';-save-temps', '-save-temps')
        if _target != 'main':
            line = line.replace(';-D DEBUG', '-D DEBUG')
            line = line.replace('-D LOG_FUNC=0', '-D LOG_FUNC=1')
        # TODO find a better way
        if _target in ['unity_cruiseSlope', 'unity_controllerTemp']:
            line = line.replace('-D USE_ANALOGREAD_SIMULATION=0',
                                '-D USE_ANALOGREAD_SIMULATION=1')
        if _target in ['unity_controllerTemp']:
            line = line.replace('-D CONTROLLER_TEMP_SIMULATION=0',
                                '-D CONTROLLER_TEMP_SIMULATION=1')

        fWrite.write(line)

    fRead.close()
    fWrite.close()

    # ---------------------------------------
    # Build _cmd
    if _target == 'main':
        _cmd = "platformio run --environment " + \
            _env + " --project-conf platformio.ini_tmp"
    else:
        _cmd = "platformio test --environment " + _env + \
            " -f " + _target + \
            " --without-uploading --without-testing --project-conf platformio.ini_tmp"
    print("-> Building...")
    if _bVerbose:
        print(_cmd)
    os.popen(_cmd).read()
    os.remove('platformio.ini_tmp')

    # ---------------------------------------
    # Exit if a compilation problem occured
    _firmware = os.path.join('.pio', 'build', _env, 'firmware')
    if not os.path.exists(_firmware + '.hex'):
        cleanTmpFiles(_bVerbose)
        say("Error during build process. Please fix.", _bSilent)
        return 1

    # ---------------------------------------
    # Rename and move hex file in firmware folder
    shutil.move(_firmware + '.hex', _savedFirmware + '.hex')
    print('-> ' + _savedFirmware + '.hex' + ' has been created.')

    # ---------------------------------------
    # Generate .txt hexa file to look for crash addresses
    _cmd = os.path.join(getFolderTree('.platformio', 'packages',
                                      'toolchain-atmelavr'), 'bin', 'avr-objdump') + ' -d -S -j .text ' + _firmware + '.elf'
    if _bVerbose:
        print(_cmd)
    with open(_savedFirmware + '.txt', 'w') as fWrite:
        fWrite.write(os.popen(_cmd).read())
        fWrite.close()
    print('-> ' + _savedFirmware + '.txt' + ' has been created.')

    # ---------------------------------------
    # Generate script to analyse ExomoCrashDump results

    # Use files kept by "-save-temps" compilator option to look for Exomo stack Ids
    stackIdsFilePath = _savedFirmware + '_stackIds.py'
    if os.path.exists(stackIdsFilePath):
        os.remove(stackIdsFilePath)

    fWrite = open(stackIdsFilePath, "w")
    fWrite.write("#!/usr/local/bin/python3\n")
    fWrite.write("# -------------------------------------------\n")
    fWrite.write("import sys\n")
    fWrite.write("class id(object):\n")
    fWrite.write("    pass\n")
    fWrite.write("\n")
    previousLine = ''
    fileList = glob.glob('*.ii')
    for f in fileList:
        with open(f, 'r') as fRead:
            for line in fRead.readlines():
                line = line.strip()
                if not line.startswith('# ') and not line == '' and not line == '{':
                    if re.search(r'ExomoWatchdog::ExomoCrashMonitor::addIdToStack\(', line):
                        # previousLine : void fct_CatFile(const char *p)
                        # line         : ExomoWatchdog::ExomoCrashMonitor::addIdToStack(1178211);
                        # ->           : setattr(id, "1178211", "void fct_CatFile(const char *p)")
                        line = line.replace(
                            'ExomoWatchdog::ExomoCrashMonitor::addIdToStack(', '').replace(');', '')
                        fWrite.write('setattr(id, "' + line +
                                     '", "' + previousLine + '")' + '\n')
                    previousLine = line
            fRead.close()
    fWrite.write("\n")
    fWrite.write("i = 1\n")
    fWrite.write("while i < len(sys.argv):\n")
    fWrite.write("    if hasattr(id, sys.argv[i]):\n")
    fWrite.write("        print(getattr(id, sys.argv[i]))\n")
    fWrite.write("    else:\n")
    fWrite.write("        print(sys.argv[i] + ' -> id not found !')\n")
    fWrite.write("    i += 1\n")
    fWrite.write("\n")
    fWrite.close()
    cleanTmpFiles(_bVerbose)
    print('-> ' + stackIdsFilePath + ' has been created.')

    # Check unicity of stack ids
    print('-> looking for duplicate IDs in ' + stackIdsFilePath + '...')
    previousLine = ''
    bDuplicateIdFound = False
    with open(stackIdsFilePath, 'r') as fRead:
        for line in sorted(fRead):
            line = line.strip()
            if not line == '' and re.sub(r'(setattr\(id, ".*", ").*', r'\g<1>', previousLine) == re.sub(r'(setattr\(id, ".*", ").*', r'\g<1>', line):
                bDuplicateIdFound = True
                print("Duplicate id found : " +
                      previousLine + '\n               and : ' + line)
            previousLine = line
        fRead.close()
    if bDuplicateIdFound:
        say("Duplicate IDs was found. Please fix.", _bSilent)
        return 1

    # ---------------------------------------
    # Generate delivery and source ZIP files
    if _target == 'main':
        _zipFile = "Exomo_" + _version + ".zip"
        _zipSourceFile = "Exomo_Sources_" + _version + ".zip"

        macOsPath = os.path.join(
            _maintenanceToolsFolder, 'Exomo', 'ExomoCopilotMacOs.app', 'Contents', 'MacOS')
        shutil.copy(stackIdsFilePath, os.path.join(
            macOsPath, os.path.basename(stackIdsFilePath)))
        shutil.copy(_savedFirmware + '.hex', os.path.join(macOsPath,
                    os.path.basename(_savedFirmware + '.hex')))

        zipFolder(_maintenanceToolsFolder, os.path.join(
            _deliveryFolder, _zipFile))

        zipFolder(os.getcwd(), os.path.join(
            _deliveryFolder, _zipSourceFile))

    # Successfull return
    return 0


def cleanTmpFiles(_bVerbose):
    """
    clean function
    """
    print("-> Cleanning previous builds")
    _cmd = "platformio run -t clean --silent"
    if _bVerbose:
        print(_cmd)
    os.popen(_cmd).read()

    # remove files kept by "-save-temps" compilator option
    removeFilesByPattern('*.i')
    removeFilesByPattern('*.ii')
    removeFilesByPattern('*.s')


def scanAndChooseBleUuid():
    """
    Scan BLE devices looking for those having a characteristic "['read', 'write-without-response', 'notify']"
    Asks to chose if several devices are found

    Cf. https://www.programcreek.com/python/index/168/serial

    Prerequisis : with admin rights (on windows or MacOS):
        python -m pip install --upgrade pip
        pip install ble-serial
        pip install pyserial

    Cf. https://github.com/Jakeler/ble-serial
    For Windows :
        desactivate signature's check for drivers in bios
        https://docs.microsoft.com/fr-fr/windows-hardware/manufacture/desktop/disabling-secure-boot?view=windows-11
        install first
            Setup_com0com_v3.0.0.0_W7_x64_signed.exe
        then
            ble-com-setup.exe --install-path "C:/Program Files (x86)/com0com/"
            mode
    """
    print("----------------------------")
    print("Scanning BLE devices...")
    print("----------------------------")
    tmpFile = "tmp.log"
    with open(tmpFile, 'w') as f:
        for line in os.popen("ble-scan -t 10"):
            searchObj = re.search(r'(.*) \(RSSI=.*: (.*)', line.rstrip(), re.S)
            if searchObj:
                deviceUUID = searchObj.group(1)
                deviceName = searchObj.group(2)
                print(deviceUUID + " " + deviceName)
                if not deviceName == "Unknown":
                    f.write(deviceUUID + " " + deviceName + '\n')

    # -------------------------------------------------------------------------------
    print("----------------------------")
    print("Deep scanning BLE devices...")
    print("----------------------------")
    UUIDs = {}
    with open(tmpFile, 'r') as f:
        for line in f:
            searchObj = re.search(r'([^ ]*) (.*)\n', line, re.S)
            deviceUUID = searchObj.group(1)
            deviceName = searchObj.group(2)
            cmdRes = ''
            try:
                cmdRes = os.popen("ble-scan -t 20 -d " + deviceUUID)
            except:
                print("Something was wrong with", deviceUUID)
            if not cmdRes == '':
                for line in cmdRes:
                    print(line.rstrip())
                    searchObj = re.search(
                        r".*CHARACTERISTIC (.*) \['read', 'write-without-response', 'notify'\]", line.rstrip(), re.S)
                    if searchObj:
                        UUIDs[deviceUUID] = {
                            "deviceName": deviceName, "characteristicId": searchObj.group(1)}

    os.remove(tmpFile)

    # -------------------------------------------------------------------------------
    # Show found devices and ask to choose

    print()
    i = 0
    for UUID in UUIDs:
        i = i+1
        print(i,
              "- DeviceName:", UUIDs[UUID]["deviceName"],
              "- UUID:", UUID,
              "- characteristicId:", UUIDs[UUID]["characteristicId"])

    if i == 0:
        print("-------------------------")
        print("No device found. Exiting.")
        print("-------------------------")
        exit(1)

    userChoice = 1
    if i > 1:
        userChoice = input("Please choose the device: ")

    targetUUID = None
    i = 0
    for UUID in UUIDs:
        i = i + 1
        if str(userChoice) == str(i):
            targetUUID = UUID
            break

    return targetUUID
