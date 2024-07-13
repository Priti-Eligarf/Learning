"""
Functions:
    1. Block of code used to perform a specific action
    2. Reusable block
    3. Can have parameters
    4. Collection of multiple function create a program
    5. Pre defined functions print() sort() etc

    deg function_name:
        statements/ code to be executed
"""


# default function
def print_func():
    print("My name is priti")


print_func()


# return function
def print_my_name_as(name):
    # print("my kid name is :"+name)
    return "my kid name is :" + name


name = print_my_name_as("sharvil")
print(name)


def get_user_details(name, age, salary):
    print("Name is:", name, "Salary is ", salary, "Age is ", age)


get_user_details("priti", 12, 600000)

""""
Types of Arguments:
    1. Required arguments
    2. Keyword arguments
    3. Default arguments
    4. Variable length arguments    

"""


def req_arg(a, b):
    print(a + b)


get_user_details(name="priti", age=12, salary=600000)
req_arg(1, 3)


def def_arg(name, school="oxford"):
    print("Name-{}".format(name))
    print("School {}".format(school))


def_arg("Sharvil")
def_arg("sharvil", "SPDPS")



def var_len_arg(*name):
    for i in name:
        print(i)


var_len_arg("priti","diya","sharvil","shantanu",12.2,4,56)

# demo for function with creating returns
def add(start, end):
    result = 0

    for i in range(start, end + 1):
        result = result + i
    return result

    s = add(1, 5)
    print(s)


# check the inbuilt fun conditions

def sum(start, end):
    if start > end:
        print("condition is true")
    else:
        print("false")
    return


sum(50, 30)


def test():
    i = 9
    return
    # print(i)


test()
print(test())


# ####################################\\


def func(k, j=100):
    print(k, j)


func(50)
