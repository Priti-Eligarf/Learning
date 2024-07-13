"""

OOPS Concepts / Procedural language (Step by Step implementation of the code)

    1. Classes
    2. Objects
    3. Encapsulation
    4. Absraction
    5. Inheritance
    6. Polymorphism


    kgkjsfd
    lkhsdfkjs
    jhsdgfsjkdfs
    jsdhgfsfjks

        kgkjsfd
    lkhsdfkjs
    jhsdgfsjkdfs
    jsdhgfsfjks


What is a Class?


1. A Class can be defined as a Blueprint / Template which describes the state / behavior
of it's object


class <classname>:
    statements


    School Class:
    Name
    Age
    Roll number
    Address

    1 - Rahul, 16, 1, asfsdf
    2. Raman, 18, 2, asfsdfser

"""





class Human:
  eyes="Blue"
  Nose="large"

  def eyes_function(self):
      print("Function to see")
  def Nose_function(self):
    print("Function to smell")

  def ear_function(self):
        print("Function to listen")


a = Human()

a.eyes_function()
a.ear_function()
a.Nose_function()


class Human1:
    eyes = "Blue"
    Nose = "large"

    def eyes_function(self,color):
        print("Function to see{}".format(color))

    def Nose_function(self,size):
        print("Function to {} smell".format(size))

    def ear_function(self,color):
        print("Function to listen{}".format(color))


b = Human1()

b.eyes_function("pink")
b.ear_function("small")
b.Nose_function("brown")




