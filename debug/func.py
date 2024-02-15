""" Debug functions

    "sys.gettrace() is not None" means we are in DEBUG MODE
"""
import os
import sys
import builtins
from datetime import datetime
from tkinter import NO

# A function that prints in DEBUG MODE
# does nothing otherwise
# yes she is making a test 
# but in python you know 
# there's no conditionnal compilation 
# cause there's no compilation
#
def print( *args, **kwargs ):
    if sys.gettrace() is not None:
        builtins.print( *args, **kwargs )

_log_path = None
       
def log( *args, **kwargs ):
    global _log_path
    if _logPath is None:
        _logPath = "./log/gmonitor-stock-" + os.path.join(
            os.getcwd(), datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".log"
        )

    line = ' '.join(map(str, args)) + ' ' + ' '.join(f'{key}={value}' for key, value in kwargs.items())    
    with open(_logPath, 'w') as file:
        file.write( line + '\n' )