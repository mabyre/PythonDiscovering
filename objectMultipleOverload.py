#
# Objects concepts in Python
#
# Surcharge multiple, multiple overload
#
# Don't use not working :
# https://deusyss.developpez.com/tutoriels/Python/heritage_metaclasse/
#

class Motor:
    def __init__(self, name):
        self.name = name

    def getName(self):
        print('Motor ', self.name)


class Wheel:
    def __init__(self, number):
        self.number = number

    def getNumber(self):
        print('I have ', self.number, ' wheels')


class Vehicul(Motor, Wheel):
    def __init__(self):
        Motor.__init__(self)
        Wheel.__init__(self)

    def getVehicul(self):
        print('My motor is ', self.getName(),
              ' and I have ', self.getNumber(), ' wheels')


motor1 = Motor("V6")
motor2 = Motor("None")

wheel1 = Wheel(4)
wheel2 = Wheel(2)

wroomwroom = Vehicul()
bycicle = Vehicul(motor2, wheel2)
