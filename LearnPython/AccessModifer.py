"""
Public modifier
Protected variable -  _variable and def _Method
Private variable -   __variable and def __Method

"""

class car:
    publicVar = 9
    _protectedVar = 10
    __privateVar = 11

    def __init__(self):
        print("Inside the car constructor")

    def publicMethod(self):
        print("Inside the public method")

    def _protectedMethod(self):
        print("Inside the protected method")

    def __privateMethod(self):
        print("inside the private method")

    @property
    def protectedVar(self):
        return self._protectedVar

