""" Debug functions

    "sys.gettrace() is not None" means we are in DEBUG MODE
"""
import sys
import builtins

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