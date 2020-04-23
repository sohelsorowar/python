from numpy import *

#six ways to create array
#1
arr=linspace(0,15,16)
print("this is linspace")
print(arr)


#2
arr=logspace(0,40,5)
print("this is logspace")
print(arr)

#3
arr=arange(1,15,2)
print("this is arange")
print(arr)

#4
arr=zeros(5)
print("this is zeros")
print(arr)

#5
arr=ones(5)
print("this is ones")
print(arr)

#6
arr=array([2,3,4])
print("this is oarray")
print(arr)



#add two array
a=array([1,2,3,4,5])
a1=array([1,2,3,4,5])
a2=a+a1
print(a2)

#copy array
ar=array([1,3,4,5])
ar1=ar.view()    # .view() also called shallow copy
ar[0]=5         #if we want to change a value
print("copy of ar:",ar1)

ar2=ar.copy()    #.copy also called Deep copy
ar[2]=5
print("ar:",ar)
print("copy of ar:",ar2)
# shalllow and deep copy differs on changing valuse
