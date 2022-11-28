#
# It is useful to measure time
#
# https: // www.geeksforgeeks.org/how-to-measure-elapsed-time-in-python/
#
# it's quite easy to mesure time in python
#
import time
import timeit

#-----------------------------------------------------------#

start = time.time()

print(23*2.3)
time.sleep(0.01)

end = time.time()
print(end - start)

#-----------------------------------------------------------#

# define the code statement to test and
# calculate the execution time
exec_time = timeit.timeit("print('Hello World!')", number=3)

# printing the execution time in seconds
print(exec_time, 'secs.')

#-----------------------------------------------------------#

# code segment to measure
code_segment = '''\
import random
def execute(n):
    return n**n
execute(random.randint(20, 50))
'''

# execute code segment and find the execution time
exec_time = timeit.timeit(code_segment, number=10**6)

# printing the execution time in secs.
# nearest to 3-decimal places
print(f"{exec_time:.03f} secs.")

#-----------------------------------------------------------#

# 52.9
# 0.010207653045654297
# Hello World!
# Hello World!
# Hello World!
# 0.000990700000000011 secs.
# 1.580 secs.
