
class Computer:
    def __init__(self):
        self.name = "sohel"
        self.age = 23

#    def update(self):   #self points particular values
#        self.age = 40
    def compare(self,other):
        if self.age == other.age:
            print(self.age)
            return True
        else:
            print(other.age)
            return False


c1 = Computer()      #constructor
c2 = Computer()      #  ||
c1.name = "Sorowar"
c1.age= 23

#c1.update()


if c1.compare(c2):
    print("they aare same")
else:
    print("they are not same")


print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)
