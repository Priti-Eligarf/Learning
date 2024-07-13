"""
While condition /true
execute the block
"""

i=0

while i<=10:
    print("hello")
    i+=1

# sum of 4 no
n=int(input("enter the no:"))
k=0
sum = 0
while k<n:
    sum = sum + k
    print(sum)
    print("the sum {} is {}".format(k,sum))
    k+=1
