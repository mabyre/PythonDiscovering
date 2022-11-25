#
# Les Listes
#
# Surprenant résultat de
# a += "ddùmldl"
#
a = [1, 2]
b = [3, 4]
c = a + b
print(c)

a += a
print(a)

a = [1, 2]
a += '123'
print(a)

a = [1, 2]
a += ['123']
print(a)

a = ["1231"]
b = ["456"]
print(a + b)

a += "ddùmldl"
print(a)

a += ["ddùmldl"]
print(a)

# a = a + "rere"
# Une exception s'est produite: TypeError
# can only concatenate list(not "str") to list

# [1, 2, 3, 4]
# [1, 2, 1, 2]
# [1, 2, '1', '2', '3']
# [1, 2, '123']
# ['1231', '456']
# ['1231', 'd', 'd', 'ù', 'm', 'l', 'd', 'l']
# ['1231', 'd', 'd', 'ù', 'm', 'l', 'd', 'l', 'ddùmldl']
