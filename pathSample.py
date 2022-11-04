#
# https://www.programiz.com/python-programming/methods/string/format
#
from pathlib import Path

# Linux sample
pathName = Path("/tmp/d/a.dat").name
print(pathName)

# Windows sampl
fileSource = r'C:\Users\Mabyre\Nextcloud\TEAM PRODUITS\CUSTOMER SERVICE\FlightDatas\0x3414B59254B6_2021-09-07_14-04-51_exomoOriginal.log'
fileName = Path(fileSource).name
print(fileName)

fileName1 = fileName.split('_')
print(fileName1[0])
print(fileName1[1])
print(fileName1[2])

fileName2 = fileName1[0] + fileName1[1] + fileName1[2]
print(fileName2)

# a.dat
# 0x3414B59254B6_2021-09-07_14-04-51_exomoOriginal.log
# 0x3414B59254B6
# 2021-09-07
# 14-04-51
# 0x3414B59254B62021-09-0714-04-51
# Python has 002 quote types.
