'''# To define a function that take two integers and return the sum of those two numbers
def add(a, b):
    print( "sum of two no",a + b)


# initializing the variables
n1 = 10
n2 = 5

# function calling and store the result into sum_of_twonumbers
sum = add(n1, n2)

# To print the result
print("Sum of {0} and {1} is {2};".format(n1, n2, sum))
#print("Sum of "num1+"and "num2 "is" +sum_of_twonumbers)

num1 = 15
num2 = 12

# Adding two numbers
sum_twoNum = lambda num1, num2: num1 + num2

# printing values
print("Sum of {0} and {1} is {2};".format(num1, num2, sum_twoNum(num1, num2)))'''


def add(a, b):
    # a=input("Enter the first number : ")
    # b=input("Enter the second number : ")
    return float(a+b)


num1 = input("Enter the first number : ")
num2 = input("Enter the second number : ")
sum = add(float(num1),float(num2))
print("sum of {} of {} is {}".format(num1, num2, sum))
