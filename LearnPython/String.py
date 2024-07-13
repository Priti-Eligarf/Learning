print(type("this is a string"))

a="Welcome to w2a"
print(a)

b='Wlcome to W2A'
print(b)

'''
Hey, my name is "priti"
'''
print('Hey, my name is "priti"')

e= "Hay" \
    "My name is " \
    "Priti"
print(e)

g= """
Hay
    My name is 
    "Priti"

"""

print(g)

print("This is Priti's \"New\"House")

name="Priti"
print(name[1:4:2])  #[ony index] [Sart index:end index][start index: endindex : jump]
print(name[::2])    #jump on th char
print(name[::1])    #normal string
print(name[::-1]) # revers the string

print(len(name))

abc="Hello, Priti"

b=abc.split(",")
print(b[0])
print(b)
print(b[1].strip())

ab="hi"
cd="priti"

print(ab+cd)

#print(10+"10")

a="10"*4
print(a)
print("ba"+"na"*2)

city="New delhi"
age=35
id=10
print("Hey i live in ",city)
print(f"Hey i live in {city} my age is {age}, and id is {id}")
print("Hey, i live in {}, My age is{}, and id is{}".format(city,age,id))
print("hey, I live in  %s, My age is %d, and id is %f"%(city,age,id))
























