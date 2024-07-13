"""
Polymorphism:

    1. Operator overloading
    2. Method overloading/ overriding
    3. Constructor overloading/ overriding

 1. Operator overloading

 <operand> <opertor> <operand>
 1+2= -1

"""

class opearatorOverloading:

    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        total_pages = self.pages - other.pages
        return total_pages



a = opearatorOverloading(10)
b = opearatorOverloading(5)

print(a+b)



"""

Method and constructor overloading

"""

class A:
    def add(self):
        print("Addition of X and Y")


class B(A):
    def add(self):
        print("Different defination")
#this is the concept of overriding Method are same but having different code


class MethodOverloading:
    def __init__(self):
        print("constructor")

    def __init__(self,name):
        self.name = name
        print("parameterised constructor")

    def add(self,a,b):
        return a+b

    # def add(self,a,b,c):
    #     return a+b+c


# obj = MethodOverloading()
# print(obj.add(10,20))
obj1 = MethodOverloading("Rahul")
print(obj1.add(10,20))

"""
3. Method overriding in derived class
"""
class methodOverriding:

    def __init__(self):
        print("base constructor")

    def sum(self):
        print("Inside base class")


class methodOverridingDerived(methodOverriding):

    def __init__(self):
        super().__init__()
        print("derived constructor")

    def sum(self):
        super().sum()
        print("Inside derived class")


ob=methodOverridingDerived()
ob.sum()

class Parent:
    name = 'Sharvil'


class Child(Parent):
    pass


Obj = Child()
print(Obj.name)


