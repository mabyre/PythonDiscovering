#
# Objects concepts in Python
#
# Héritage, legacy
#

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print('Hi, I am ', self.name)

    def getAge(self):
        print(f'I am {self.age} years old' )

class Customer(User):
    is_customer = True

    def isCustomer(self):
        return self.is_customer


mathilde = User('Mathilde', 29)
pierre = Customer('Pierre', 27)

print(pierre.getName())
print(pierre.getAge())

if pierre.isCustomer():
    print(' and I am a customer')
else:
    print(' and I am NOT a customer')
