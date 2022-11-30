#
# Objects concepts in Python
#
# Surcharge, overload
#
# Customer have an email so getName is overloaded in case of a Customer
#

class User:
    seniority = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print('Hi, I am ', self.name)


class Customer(User):
    is_customer = True

    def setEmail(self, email):
        self.email = email

    def getName(self):
        print('Hi, I am ', self.name, ' and my email is ', self.email)


mathilde = User('Mathilde', 29)
jean = Customer('Jean', 27)

jean.setEmail('jean@customer.com')
jean.getName()

if jean.is_customer:
    print(' and I am a customer')
else:
    print(' and I am NOT a customer')

print(isinstance(jean, User))
print(isinstance(jean, Customer))
print(issubclass(User, Customer))
print(issubclass(Customer, User))
