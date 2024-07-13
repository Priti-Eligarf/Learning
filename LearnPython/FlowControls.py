# Python Flow Control

"""
    1. If Statement
    2. If-Else Statement
    3. If Elif else statement
    4. For Loops
    5. While Loops
    6. Nested Loops
    7. Break Statement
    8. Continue Statement
    9. Loops with Else block
    10. Pass Statement

"""

""" If Statements
 if a>b
 if 
"""
a=4
b=5
print("------- If Statement Demo---------")
if a>b:
   print("b is greater")
print("a is greater")
print("---------If -Else Demo---------")
if a>b:
   print("b is greater")
else:
    print("a is greater")

print("=====If elif else Demo=======")

# mark=int(input("Enter the Mark:"))
# section =input("Enter the section-")
# if mark==100:
#     if section == "A":
#         print("Brilliant Class")
#     grade ="A+"
#     print("Gread")
# elif 80 < mark < 100:
#     print("B Grade")
# elif 60 < mark < 100:
#     print("C Grade")
# else:
#     print("a is greater")

"""
    Iterative Statements
    1. For Loop
        for every x, in the sequence to perform some activity, which means
        every element which is      in the sequence, renge, list, tuple or a 
        dictionary 
    2. While loop
    Syntax: for x in sequence:
                 Statements
    """

Sequence= "Priti"
i = 0
for l in Sequence :
    print("The Char present at {},index-{}".format(i,l))
    i=i+1

for a in range (5):
     print("Hello",a)

for x in range(2, 5):
         print(x)

for x in range(2,40,15):
    print(x)

n=int(input("Enter the number:"))
for x in range(1,11):
    print(n,"*",x ,"=",n*x)


list = eval(input("enter the no for addition:"))
sum=0
for x in list:
    sum = sum+x
    print("the sum is :",sum)

string ="my name is priti"
s = string.split(" ")
for x in s:
    print(x)
f = string.capitalize()
print(f)



