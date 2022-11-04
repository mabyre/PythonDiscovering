test = []
print(test, 'is', bool(test))

test = [0]
print(test, 'is', bool(test))

test = 0.0
print(test, 'is', bool(test))

test = None
print(test, 'is', bool(test))

test = True
print(test, 'is', bool(test))

test = 'Easy string'
print(test, 'is', bool(test))

a = 3
b = 3

print('a == b : ', a == b)
print('not(a == b) : ', not(a == b))

# [] is False
# [0] is True
# 0.0 is False
# None is False
# True is True
# Easy string is True
# a == b:  True
# not(a == b):  False
