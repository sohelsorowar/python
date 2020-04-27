class A:                    #grand parent
    def feature1(self):
        print("feature1")

    def feature2(self):
        print("feature2")

class B:                    #parent class
    def feature3(self):
        print("feature3")

    def feature4(self):
        print("feature4")

class C(A,B):               #child class
    def feature5(self):
        print("feature5")
a1=A()
b1=B()

c1=C()
c1.feature1()






#constructor in Inheritance

class AB:
    def __init__(self):
        print("in AB __init__")


class CB(AB):
    def __init__(self):
        super().__init__()  #it will print class parent class
        print("in CB __init__")
aA=CB()
