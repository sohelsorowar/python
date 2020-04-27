#types of polymorphism
#1.Duck typing 2.Operator overloading
#3.Method Overloading 4.method voerriding




#Duck typing

class Atom:
    def execute(self):
        print("compiling")
        print("running")

class MyEditor:
    def execute(self):
        print("spellCheck")
        print('line check')
class Laptop:
    def code(self,ide):
        ide.execute()

ide =MyEditor()           #ide is Duck here!!!
lap1 = Laptop()
lap1.code(ide)



# Operator Overloading

class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):      #__add__ operator overloading
        m1 = self.m1 + other.m1   #__gt__  ||
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3


    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = self.m1 + self.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return self.m1, self.m2

s1 = Student(58, 60)
s2 = Student(22, 30)
s3 = s1 + s2
print(s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1.__str__())



#Method overloading
#same method differnt argument
#Python dosent support method overloading,so we ve to create our own
class Student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):
        if a!= None and b!= None and c!= None:
            s = a+b+c
            return s
        elif a!=None and b!=None:
            s = a+b
            return s
        else:
             s = a
             return s
sa= Student(58, 22)
print(sa.sum(5,5,5))  # same methods but different agruments
print(sa.sum(5,5))    #         ||
print(sa.sum(5))      #         ||



#Method overriding
class A:
    def show(self):
        print("in A show")
class B(A):                     # A is overriding B
    def show(self):
        print("in B show")
a1=B()
a1.show()
