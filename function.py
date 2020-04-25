
# simple function caliing
def greet():
    print("hello")
greet()


#adding two numbers
def add(a,b):
    c=a+b
    print(c)
add(3,4)


#return two values

def add_sub(a,b):
    c=a+b
    d=a-b
    return c,d
r1,r2=add_sub(10,5)
print(r1,r2)


#function argument

def update(a):
    x=8
    print("X=",x)
b=10
update(b)
print("b=",b)



# variable lenth argument
def sum(a,*b):
    print(a)     # *b means multiple values
    print(b)     # **b means multiple data with key words
sum(5,6,7,10,8,)

def person(name,**data):
    print(name)
    print(data)
person('Sohel',age=25)




#pass a list to a function


def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
lst=[24,25,26,26,27,28,21,31,32]
even,odd=count(lst)

print("Even:{} and Odd:{}".format(even,odd))
