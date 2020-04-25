#anonymous function

#def add(a,b):
#    c=a+b
#    return c
from functools import reduce

add=lambda a,b:a+b  #using lambda
result=add(4,5)
print(result)


#filter using lambda
nums=[2,3,4,5,6,7,8]
even=list(filter(lambda n:n%2==0,nums)) # no longer need to call a function while using lambda
print(even)


#map using lambda
nums=[2,3,4,5,6,7,8]
double=list(map(lambda n:n*2,nums)) # no longer need to call a function while using lambda
print(double)


#reduce using lambda

sum=reduce(lambda a,b:a+b,double) # no longer need to call a function while using lambda
print(sum)
