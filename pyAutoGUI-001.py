#
# https://pyautogui.readthedocs.io/en/latest/
#
# https://pyautogui.readthedocs.io/en/latest/install.html
# Installation :
# py -m pip install pyautogui
#
#
#

import pyautogui

default = 'aaa'
#text = 'mon texte'

pyautogui.prompt(text='', title='My Box Prompt', default='')

print(text)
