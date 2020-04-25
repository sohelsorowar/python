from numpy import *


arr1=array([[1,2,3],
            [4,5,6]
])
arr2=arr1.flatten() #.flatten will convert multi dimention to one dimention.
print(arr2)



#convert one dimention to multi dimention
arr3=arr2.reshape(2,3)
print("one dimention:",arr2 ,"to multi dimention",arr3 )


#complex matrix
ar4=array([1,2,3,4,5,6,7,8,9,10,11,12])
ar5=ar4.reshape(2,2,3)   # 2 matrix 2 row and 3 column
print(ar5)



#multiply matrix
m1= matrix('1 2 3; 4 5 6; 7 8 9')
m2= matrix('11 12 13; 14 15 16; 17 18 19')
m3=m1 * m2                 # this is the power of python
print("multiplication:\n",m3)
