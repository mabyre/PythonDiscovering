#
# https://www.delftstack.com/fr/howto/python/how-to-check-the-python-version-in-the-scripts/
#
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    cls()

print(f'program running on {os.name}')
print(sys.version)
print(sys.version_info)

if sys.version_info >= (2, 7):
    print('python version OK')

if sys.version_info != (3, 11):
    print('python version NOT the last version')
