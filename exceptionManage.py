#
# import module sys to get the type of exception
#
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        # do something
        print("The entry is", entry)
        r = 1/int(entry)
        break

    # except ZeroDivisionError:
    #     # handle an exception
    #     print("Exception: ZeroDivisionError !")
    #     pass

    # except (TypeError, ZeroDivisionError):
    #     # handle multiple exceptions
    #     print(TypeError)
    #     print("TypeError: ZeroDivisionError !")
    #     pass

    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
        pass

    except:
        # handle all other exceptions
        pass

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
