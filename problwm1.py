from array import *

arr = array('i',[])

n=int(input("enter the length of array: "))

for i in range(n):
    x=int(input("Enter value"))
    arr.append(x)

print(arr)

#search array

val=int(input("enter value for search: "))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+1