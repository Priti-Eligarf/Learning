"""
    1. Arithmatic
    2. Compparision
    3. Equality
    4. Logical
    5. Bitwise
    6. Shift
    7. Assignment
    8. Ternary
    9. Membership
    10. Identity

"""
"""
    Arithmatic Operators
    
    a Addition(+)
    b substraction(-)
    c Multiplication(*)
    d Division(/)
    e Modulus(%)
    f Exponential Operator(**)
    g Floor division(//)
    
"""
a=20
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b); '''exponatial operator'''
print(a//b); 'floor division'

""" 2. Comparision Operator
a. (>)
b.(<)
c.(>=)
d. (=<)
"""
S1='CAT'
S2="DOG"
print("-------Comparision operator--------------")
print(S1>S2)
print(S1>=S2)
print(S1<S2)
print(S1<=S2)

print(ord("c"))   #Ascii value
print(ord("D"))


'''
Relatioal Value chanining
'''
print(10<20<30<40)
print(10<20>10<40)
"""Equatlity operators
a. equal to (==)
b. Not equal to (!=)
"""
print("-------Equality operator--------------")
print(a==b)
print(a!=b)
print(1== True)
print(0==True)
print(0==False)
print(10==10.0)
print("priti"=="priti")

"""
4. Logical Operators
    a And ---> return tru whatever both the arguments are true in nature
    b Or
    c Not
"""
print(True and True)
print(1 and 0)


"""a. if the value x, evaluates to false then the result is the value of x
b.  if the value x, evaluates to true then the result is the value of y """


print(10 and 20)  #20

print(0 and 20)     #0
#
# username = input("enter the username:")
# password = input("enter the password:")
#
# if username == "priti" or password =="test":
#     print("valid user")
# else:
#     print("invalid user")


    # print(not True)
    # print(not False)
    # a=10
    # print(not a==10)

'''
Bitwise operator
a. bitwise And(&)
b.bitwise or (|)
c. bitwise xor (^)
d. bitwise complement (~)
'''
""" Bitwise & """
print(bin(16))
print(bin(18))
print(16 & 18)
print(16 | 18)
print(16 ^ 18 )
print(~(-18))
"""
6.  Shift Operator
left shift (<<)
right shift (>>)
"""
print(bin(11))
print(10<<2)
print(10>>2)
"""
Assignment operator
=
+=
-=
*=
 etc
 
"""
x=20
print(x)
x+=10
print(x)
x-=10
print(x)
x*=10
print(x)

"""
Ternary Operators

it is a conditional operator
there is no specific keyword for ternary operator
var = first value if condition else second value
"""
a=50
b=90
c=30 if a>b else 40
print(c)
a=int(input("enter a="))
b=int(input("enter b="))
min= a if a<b else b
print(min)





"""
9. Identity Operators
    1. is
    2. is not
"""
a=2
b=2
print("-----------------")
print(a is b)  # True
print(a is not b)  # False

"""
Membership operator
in
not in

"""
a=[10,20,30,55,"abc"]

print(10 in a)
print(20 not in a)
print(31 not in a)
print(22 in a)