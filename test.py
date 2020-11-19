def evenOdd( x ): 
    if (x % 2 == 0): 
        print ("even")
    else: 
        print ("odd")
  
# Driver code 
evenOdd(2) 
evenOdd(3) 

def add(x,y):
    print(x+y)

add(10,5)    

#pass by reference and pass by reference
def mylist(x):
    x[2]=100
list=[10,15,20,30,40]

mylist(list)
print(list)


class dog:
    attrib1="Animal"
    attrib2="Four legs"

    def fun(self):
        print("I am an ", self.attrib1)
        print("I ve ", self.attrib2)

roger = dog()
roger.fun() 
print(roger.attrib1)       