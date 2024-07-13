"""
Dictionary
Key and value pair
    1. key-Numbers, String, tuple
    2. Value-Python object


"""

D1 ={

    "Name":"Rahul",
    "Age":23
}

print(type(D1))
print(D1)

D2 ={

    "Name":"Rahul",
    "Age":23,
    "Salary":60000.00,
    "org":"Eligarf",
    "Is-Married":True

}


print("Name {}".format(D2["Name"]))
print("Age {}".format(D2["Age"]))
print("Sal {}".format(D2["Salary"]))
print("Org {}".format(D2["org"]))
print("Married {}".format(D2["Is-Married"]))

"""
Update key value in dictionary

"""
# D2["Name"]=input("Enter Name --")
# D2["Age"]=int(input("Enter Age --"))
# D2["Salary"]=float(input("Enter Salary--"))
# D2["org"]=input("Enter Org--")
# D2["Is-Married"]=bool(input("Is-Married --"))
# print(D2)

del(D2["Is-Married"])
print(D2)

"""
Iteration a Dictionary
"""
# Printing all key values

for a in D2:
    print(a)

#     printing all values
for b in D2:
    print((D2[b]))

print(".............................................")
for c in D2.values():
    print(c)

for d in D2.items():
    print(d)

print(".............................................")

item={
    "fruits":["apple","mango","Banana"],
    "price":100,
    "size":10.5

}
print(item["fruits"][0])

item1={
    "location":"india",
    "Fruits":{"Name":"Kivi","price":102},
    "Name":"Delhi"
}
print(item1["Fruits"]["Name"])
print(item1.get("Fruits").get("price"))
print(len(item1))
print(len(item1["Fruits"]))
