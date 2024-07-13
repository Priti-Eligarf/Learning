"""

Inheritance

class A -----> Base class/ parent class

class B------> Derived class / child class

so from Inheritance we can access members, properties and methods from another class

A <----- B <------ C - Multilevel inheritance

A     B
        <-------- Multiple inheritance
   C




"""

class AnimalParent:
    name ="Rahul"
    def ap(self):
        print("Inside Animal parent class")

    def Hello(self):
        print("Inside hello Animal parent class")


class animal:
    name ="Rahul"
    def a(self):
        print("Inside Animal class")

    def Hello(self):
        print("Inside hello Animal class")


#Multiple inhertance
class Mamals(AnimalParent,animal):
    def b(self):
        print("Inside Mamals class")

mam = Mamals()
mam.b()
mam.a()
mam.ap()
mam.a
print(mam.name)
mam.Hello()

