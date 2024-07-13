class Dog:
    legs =4 #global variable (Static variable)

    def __init__(self):
        # istance of the variable
        self.name="milo"
        self.color="Brown"

    def getDogName(self):
        print(self.name)

    @classmethod
    def getLegsCount(cls):
        print(cls.legs)

    @staticmethod
    def getGenaralInformation():
        print("Beware of Dogs")


d1 = Dog()
d2 = Dog()

d2.name = " Bruno"
d2.color = "Black"

Dog.legs =3  # class level variable
d1.getDogName()
#d1.getLegsCount()
Dog.getLegsCount()
Dog.getGenaralInformation()
d1.getGenaralInformation()
print(d1.name,d1.color,Dog.legs)
print(d2.name,d2.color,d2.legs)



"""
3 types of methods/functions

    1. Instance method - use to access variable of the class
    2. Class method - static class level method
    3. Static method - standalone method
    
"""

# Instance method
