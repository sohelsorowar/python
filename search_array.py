from array import *
arr=array('i',[])
n=int(input("enter the lenth of array:"))

for i in range(n):
    x=int(input("enter number:"))
    arr.append(x)

print(arr)


k=0 # k is counter variable
val=int(input("enter a value for search:"))
for  e in arr:
    if e==val:
        print(k)
        break
    k+=1
