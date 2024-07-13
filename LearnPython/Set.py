"""
Set
    1.It is similar to list
    2. It can store different type of values (Objects) String, int, Float, Bool etc,
    3. set cannot have duplicate values
    4. set are defined{}
    5. It's a collection which is unordered and unindexed


"""
s1={"Selenium", "Appium","Cypress",100,True,100.1, "selenium"}

print(s1)
print(type(s1))
print(len(s1))

for i in s1:
    print(i)

s1.add("Protractor")
print(s1)


s1.discard("Protractor")
print(s1)

s2={"Hello"}

s3=s1.copy()
# s2=s1.add("Java")
# s4 =s2 + s1
# print("s3+s2",s4)
print("s1",s1)
print("s3",s3)
print("s2",s2)