"""
Exception handling Demo
try:

except

else:

finally:


"""

try:
    a = int(input("Enter value A:"))
    b = int(input("Enter value A:"))
    c = a / b

    print("Result of C is {}".format(c))
    print ("Ending")

except (ZeroDivisionError,ValueError,IndentationError):
    print("Inside the catch block")

else:
    print("Inside the else block")

finally:
    print("Finally always be executed")

print("outside the Try and Except Block")
