# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====
#  Listes Tuple Files Piles
# ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====-
from collections import namedtuple
numbers = [1, 2, 3, 4, 5]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

print(numbers)
print(type(numbers))

# [1, 2, 3, 4, 5]
# <class 'list' >

# indice négatif !
i = -1
while i >= -len(numbers):
    print(numbers[i])
    i -= 1

sous_numbers = numbers[1:3]
print(sous_numbers)

print(numbers[:3])
print(numbers[3:])

numbers[2:2] = [0]
print(numbers)

a = [1, 2] * 4
print(a)

# --------------------------------------


def contains(data, element):
    i = 0
    while i < len(data):
        if data[i] == element:
            return True
        i += 1
    return False


print(contains(a, 4))
print(4 in a)

print(not contains(a, 2))
print(2 not in a)

# copie
a = [1, 2, 3]
b = a[0:len(a)]
c = b[:]

a[0] = -1
b[0] = -2
print(a)
print(b)
print(c)

# -----------------------------------------------------------------------------
#  Tuple
# ------------------------------------------------------------------------------

t = 1, 2, 3
r = sum(t)
print(r)

r = sum((1, 2, 3))
print(r)


def find(data, element):
    i = 0
    while i < len(data):
        if data[i] == element:
            return True, i
        i += 1
    return False, None


values = [1, 2, 3, 4]

print(find(values, 2))
print(find(values, 6))

tuple1 = find(values, 2)

tu1, tu2 = tuple1  # déballage
print('tu1:', tu1)
print('tu2:', tu2)

t = 1, 2, 3       # emballage
a, b, c = t       # déballage

print(t)
print(a)
print(b)
print(c)

# Operateur de deballage : *

t = 1, 2, 3
result = max(*t)

print(result)

# Tuple nomé

Item = namedtuple('Item', ['barcode', 'description', 'price'])
coca = Item(5449000000996, "Coca-Cola 33cl", 0.70)

print(coca)
print(len(coca))
print(coca[1])
print(coca[1:3])
print(coca.description)

# ------------------------------------------------------------------------------
#  Chaines de caractères
# ------------------------------------------------------------------------------

s1 = "coucou loulou"
# s2 = s1[11] ERROR

print(s1)
print(s1[11])

print("lou" in s1)

# ------------------------------------------------------------------------------
#  Intervalles
# ------------------------------------------------------------------------------

i = range(1, 5)

print(i)
print(len(i))
print(i[2])
print(i[2:5])

evens = range(2, 12, 2)
print(evens)

j = 0
for i in evens:
    print(f"evens[{j}]={evens[j]}")
    j += 1

# ------------------------------------------------------------------------------
#  Files
# ------------------------------------------------------------------------------

queue = []                 # la file est vide

queue.append(1)            # la file contient [1]
queue.append(2)            # la file contient [1, 2]
queue.append(3)            # la file contient [1, 2, 3]

result = queue.pop(0)      # la file contient [2, 3]

print(result)
print(queue)

# ------------------------------------------------------------------------------
#   Piles
# ------------------------------------------------------------------------------

stack = []                 # la pile est vide

stack.append(1)            # la pile contient [1]
stack.append(2)            # la pile contient [1, 2]
stack.append(3)            # la pile contient [1, 2, 3]

result = stack.pop()       # la pile contient [1, 2]

print(result)
print(stack)

# ------------------------------------------------------------------------------

maQueue = []                 # la file est vide

maQueue.append(1)            # la file contient [1]
maQueue.append(2)            # la file contient [1, 2]
maQueue.append(3)            # la file contient [1, 2, 3]

result = maQueue.pop(0)      # la file contient [2, 3]

print(result)
print(maQueue)

# ------------------------------------------------------------------------------

myStack = []                 # la pile est vide

myStack.append(1)            # la pile contient [1]
myStack.append(2)            # la pile contient [1, 2]
myStack.append(3)            # la pile contient [1, 2, 3]

result = myStack.pop()       # la pile contient [1, 2]

print(result)
print(myStack)

# Chaîne vers liste
chaine = '1:2:3:4'
liste = chaine.split(':')
print(liste)
print(type(liste))

# Liste vers chaîne
chaine2 = ":".join(liste)
print(f"chaine2={chaine2}")
print(type(chaine2))
