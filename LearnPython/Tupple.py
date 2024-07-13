"""
Tuples
    1.It is used to store the sequence of Immutable objects
    2. mostly all the other operations are similar to a list

"""

T1=("Rahul",12.3,123)
print(type(T1))

a = []
b = [1, 2.3, "rahul", True, 3 + 2j, "rahul"]
print(type(b))
print(b)
print(b[4])
print(b[5])
b.append("cory")
print(b)

emp = ["rahul", 102, "india"]
dep1 = ["it", 10]
dep2 = ["elec", 12]
print(f"Name is {emp[0]}, Deprt is {emp[1]},and country is {emp[2]}")

"""""
List slicing
"""
c = [0, 1, 2, 3, 4, 5, 6]
print(c[0:])  # 0 to 6
print(c[:])  # 0 to 6
print(c[2:4])  # 2,3
print(c[:4])  # 0,1,2,3

"""
Updating list
"""

d = [1, 2, 3, 4, 5, 6]
print(d)
d[3] = 7
print(d)
d[1:4] = ["Rahul", "cory", "", 8, 5, 6]
print(d)

"""
Delete the value
"""
del d[4]
print(d)

"""
Sort the list
"""
e = ["a", "e", "v", "d", "s", "h"]

e.sort()
print(e)
e.sort(reverse=True)
print(e)
"""
List Operation

    1.  Repetation operation
    2.  Concatenation
    3.  Membership
    4.  Iteration
    5.  Length function

"""

print(".........Repetation operation..............")
l1 = (1, 2, 3, "Rahul", True)
print(l1 * 2)
l2 = (5, 6, 3, "cory", False)
print(l1 + l2)

print(".........concatenation operation..............")

l3 = (1, 2, 3, "Rahul", True)
l3 = l3 * 2
l4 = (5, 6, 3, "Rahul", False)
print(l3 + l4)
print(".........Membership operation..............")
print("Rahul" in l1)
print("cory" not in l2)

print(".........Iteration operation..............")
for i in l1:
    print(i)

print(".........length operation..............")

print(len(l4))
l5 = (5, 6, 3, 1, 2, 3)
print(max(l5))
print(min(l5))
string = "Priti"
print(list(string))
