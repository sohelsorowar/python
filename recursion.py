
import sys


def g():
    print('hello')
    g() # function is called by itself is called recursion
#g()



#factorial using recursion

def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)
x=5
result=fact(x)
print(result)
