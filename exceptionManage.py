'''
https://www.programiz.com/python-programming/exception-handling
'''

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break

    # except (TypeError, ZeroDivisionError):
    #     print(TypeError)
    #     print("TypeError: ZeroDivisionError !")

    # except ZeroDivisionError:
    #     print("Exception: ZeroDivisionError !")

    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()

print("The reciprocal of", entry, "is", r)


# The entry is a
# Oops! < class 'ValueError' > occurred.
# Next entry.

# The entry is 0
# Oops! < class 'ZeroDivisionError' > occurred.
# Next entry.
# The entry is 2
# The reciprocal of 2 is 0.5

# My exception Added
#
# The entry is a
# Oops! < class 'ValueError' > occurred.
# Next entry.

# The entry is 0
# Exception: ZeroDivisionError !
# The entry is 2
# The reciprocal of 2 is 0.5
