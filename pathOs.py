# what can we do with path

import os
import sys
import glob
from pathlib import Path
from tools.exomoTools import getAvrdudePath


def getAvrdudeFiles():
    fileList = glob.glob(os.path.join(
        Path.home(), ".platformio", "packages", "tool-avrdude", "**", "avrdude*"
    ), recursive=True)
    return fileList


print('----------------------------')
print('- os.getcwd: get current dir')
print('-')
print(os.getcwd())

print('----------------------')
print('- Path.home():')
print('-')
print(Path.home())

print('----------------------')
print('- Python sys.path:')
print('-')
for path in sys.path:
    print(path)

print('----------------------')
print('- Avrdude files:')
print('-')
avrDudeFiles = getAvrdudeFiles()
for file in avrDudeFiles:
    print(file)

print('----------------------')
print('- Avrdude path:')
print('-')
avrDudePath = getAvrdudePath()
print(avrDudePath)

os.system("pause")

# ----------------------
# - Python sys.path:
# -
# d: \Mabyre\Ionbird\Python
# D: \Mabyre\Ionbird\Python
# D: \Users\Braby\AppData\Local\Programs\Python\Python38\Scripts
# D: \Users\Braby\AppData\Local\Programs\Python\Python38\python38.zip
# D: \Users\Braby\AppData\Local\Programs\Python\Python38\DLLs
# D: \Users\Braby\AppData\Local\Programs\Python\Python38\lib
# D: \Users\Braby\AppData\Local\Programs\Python\Python38
# D: \Users\Braby\AppData\Roaming\Python\Python38\site-packages
# D: \Users\Braby\AppData\Local\Programs\Python\Python38\lib\site-packages
# ----------------------
# - Avrdude files:
# -
# D: \Users\Braby\.platformio\packages\tool-avrdude\avrdude.conf
# D: \Users\Braby\.platformio\packages\tool-avrdude\avrdude.exe
# ----------------------
# - Avrdude path:
# -
# D: \Users\Braby\.platformio\packages\tool-avrdude\avrdude.exe
