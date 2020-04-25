


class Student:                          #this is outher class

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()         # this is for inner laptop class

    def show(self):
        print(self.name, self.roll)
        self.lap.show()                 #this is for inner class show()


    class Laptop():                     # this is inner class

        def __init__(self):
            self.brand = 'MacBook'
            self.cpu = 'i5'
            self.ram = '8 '

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Sohel', 28)
s2 = Student('Sorowar', 64)
s1.show()
