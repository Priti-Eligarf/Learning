
import re

# Function which uses re.findall method to convert string to list character wise
def Convert(string):
    return re.findall('[a-zA-Z]', string)

# Driver code
str1 ="Priti"
print("List of character is : " ,Convert(str1))


def Convert1(string):
    li = list(string.split(" "))
    return li


# Driver code
str1 = "Geeks for Geeks"
print(Convert1(str1))



str2 = "Geeks for Geeks demo"
li = list(str2.split(" "))
print(li)