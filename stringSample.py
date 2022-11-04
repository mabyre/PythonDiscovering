"""
    Play with strings never so easy as it seams
"""


def substractLast(str, car):
    i = str.rfind(car)
    # car not founded in str
    if i == -1:
        return str
    end = len(str)
    s = str[0:i] + str[i+1:end]
    return s

# -----------------------------------------------------------------------------


s = 'python is fun'
c = 'n'
print(s.find(c))
print(s.rfind(c))

# 5
# 12

# -----------------------------------------------------------------------------

str = "coucou\naaa\n"
print(str[0])
print(str[1])
print(str[2])
print(len(str))
print(str)

str1 = substractLast(str, '\n')
print(str1)

# c
# o
# u
# 11
# coucou
# aaa
#
# coucou
# aaa

str = "coucouaaa"
str1 = substractLast(str, '\n')
print(str1)
