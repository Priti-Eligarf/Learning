for i in range(10):
    if i==5:
        print("executing break at ",i)
        break
    print("printing the value as ",i)

print("outside the for loop")

"""
break statement
It is used to current loop and resume the code

continue statement:
it is used to skip the current iteration and continue with the iteration
"""

print(" .............. od  no ........")

for i in range (10):
    if i%2==0:
        print("even:",i)
        continue
    print("odd :",i)


print("...................")

for i in range(10):
    if i==7:
        print("break: ",i)
        break
    elif i==5:
        continue
    print("contune:",i)


print("...................")
"""
Else block within the loops
"""
print("...................")

cart=[10,90,54,65,67,56]

for item in cart:
    if item >80:
        print("this item not allowed")
        continue
    print(item)
else:
    print("all items are succefully processed")


print("............//////.......")

for x in "Rahul":
    pass