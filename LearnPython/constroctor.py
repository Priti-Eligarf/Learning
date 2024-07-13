"""
Constructors:

They are called as a first function of the class

Syntax: __init__()

All classes have this function which is always executed when the class being
initiated or an object of the class is created

"""

class Practice:
    # Default constructor
    def __init__(self):
        print("Inside constructor")

    def add(self):
        print("Adding somthing")


a = Practice()
a.add()


class emp:
    # parameterised constructor
    def __init__(self, eid, ename, sal):
        # global variable defining as self
        self.eid = eid
        self.ename = ename
        self.sal = sal

# constructor overloading is not possible in the python
    def __init__(self, eid, ename, sal, BDate):
            # global variable defining as self
            self.eid = eid
            self.ename = ename
            self.sal = sal
            self.Bdate = BDate

    def display(self):
        print("EMP ID:".format(self.eid), "EMP Name:".format(self.ename), "Sal:".format(self.sal))
        print("EMP ID: {} EMP NAME : {} SAL :{}".format(self.eid, self.ename, self.sal))
        print(self.eid, self.ename, self.sal)

e = emp(100,'Smith', 10000)
e.display()
class myclass:
    def __del__(self):
        print("Destroyed")


c1 = myclass()
c2 = myclass()

del c1






