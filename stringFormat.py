#
#
#

# curious sample don't know why it's works
print('%(language)s has %(number)03d quote types.'
      % {'language': "Python", "number": 2})

#
#  Example 1: Basic formatting for default, positional and keyword arguments
#

# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

#
# Example 2: Simple number formatting
#

# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.4567898))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: 0x{0:x}".format(12))

#
# Example 3: Number formatting with padding for int and floats
#

# integer numbers with minimum width
print("{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

# padding for float numbers
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))

#
# Example 4: Number formatting for signed numbers
#

# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))

#
# Example 5: Number formatting with left, right and center alignment
#

# integer numbers with right alignment
print("{:5d}".format(12))

# float numbers with center alignment
print("{:^10.3f}".format(12.2346))

# integer left alignment filled with zeros
print("{:<05d}".format(12))

# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))


#
# Example 6: String formatting with padding and alignment
#

# string padding with left alignment
print("{:5}".format("cat"))

# string padding with right alignment
print("{:>5}".format("cat"))

# string padding with center alignment
print("{:^5}".format("cat"))

# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))

#
# Example 7: Truncating strings with format()
#

# truncating strings to 3 letters
print("{:.3}".format("caterpillar"))

# truncating strings to 3 letters
# and padding
print("{:5.3}".format("caterpillar"))

# truncating strings to 3 letters,
# padding and center alignment
print("{:^5.3}".format("caterpillar"))

#
# Example 8: Formatting class members using format()
#


class Person:
    # define Person class
    age = 23
    name = "Adam"


# format age
print("{p.name}'s age is: {p.age}".format(p=Person()))

#
# ...
# https://www.programiz.com/python-programming/methods/string/format
#

# My Samples
fileName = "{:03d}".format(1)
print(fileName)

# Python has 002 quote types.
# Hello Adam, your balance is 230.2346.
# Hello Adam, your balance is 230.2346.
# Hello Adam, your balance is 230.2346.
# Hello Adam, your balance is 230.2346.
# The number is : 123
# The float number is : 123.456790
# bin: 1100, oct: 14, hex: 0xc
#    12
# 1234
#   12.235
# 00012
# 0012.235
# +12.230000 - 12.230000
# 12.230000 - 12.230000
#  12.230000 - 12.230000
#    12
#   12.235
# 12000
# - 12.235
# cat
#   cat
#  cat
# *cat*
# cat
# cat
#  cat
# Adam's age is: 23
# 001
