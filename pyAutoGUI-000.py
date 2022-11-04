#
# https: // pyautogui.readthedocs.io/en/latest/
#
# https://pyautogui.readthedocs.io/en/latest/install.html
# Installation :
# py -m pip install pyautogui
#
#
#

import pyautogui

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()

# Get the XY position of the mouse.
currentMouseX, currentMouseY = pyautogui.position()

pyautogui.moveTo(100, 150)  # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.
pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.

# Find where button.png appears on the screen and click it.
pyautogui.click('button.png')

# Move mouse 10 pixels down from its current position.
pyautogui.move(0, 10)
pyautogui.doubleClick()    # Double click the mouse.
# Use tweening/easing function to move mouse over 2 seconds.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)

# type with quarter-second pause in between each key
pyautogui.write('Hello world!', interval=0.25)
# Press the Esc key. All key names are in pyautogui.KEY_NAMES
pyautogui.press('esc')

pyautogui.keyDown('shift')  # Press the Shift key down and hold it.
# Press the left arrow key 4 times.
pyautogui.press(['left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')   # Let go of the Shift key.

pyautogui.hotkey('ctrl', 'c')  # Press the Ctrl-C hotkey combination.

# Make an alert box appear and pause the program until OK is clicked.
pyautogui.alert('This is the message to display.')
