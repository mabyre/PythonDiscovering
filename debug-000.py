""" The famous DEBUG functions

    I want to make traces but there is a 'trace' module to trace the execution of a program
    let see what's about
    
    ### Module Trace in DEBUG MODE
    PYDEV DEBUGGER WARNING:
    sys.settrace() should not be used when the debugger is being used.
    This may cause the debugger to stop working correctly.
    If this is needed, please check:
    http://pydev.blogspot.com/2007/06/why-cant-pydev-debugger-work-with.html
    to see how to restore the debug tracing back correctly.
"""
import sys
import trace
import debug.func as debug
import logger

# ----------------------------------------------------------------

# A function that prints in debug mode and does nothing otherwise
# def dbg_print(var):
#     if sys.gettrace() is not None:
#         print(f"{var}")
        
# sample function with a variable list of arguments
def debug_print(*args, **kwargs):
    if sys.gettrace() is not None:
        print(*args, **kwargs)        

def my_function_to_trace(a, b):
    result = a + b
    print(result)
            
# ----------------------------------------------------------------

x = 42
debug.print(x)
debug_print(x)
debug_print("x:", x)
debug.print("x:", x)

y = "hello"
debug_print("y:", y)
debug.print("y:", y)

# execute tracing in none debug mode
if sys.gettrace() is None:
    tracer = trace.Trace()
    tracer = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], trace=0, count=1)
    tracer.runfunc(my_function_to_trace, 10, 20)        

# Test Log function
x = 3
log = logger.Logger()
log.print("Error:", x, "different de 3")

log = logger.Logger()
log.print("Error:", x, "different de 3")

print( "END OF PYTHON SCRIPT" )