#5!=5*4*3*2*1=120



def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=5
result=fact(x)
print(result)
