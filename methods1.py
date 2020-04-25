#two types of methods 1.class method 2.static method
class Student:

    school = 'RDA'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m2)/3

    @classmethod         # class method
    def info(cls):
        return cls.school

    @staticmethod       # static method
    def info():
        print("this is static method")

s1 = Student(34, 67, 32)
s2 = Student(23, 23, 23)
print(s2.avg())
print(Student.info())
Student.info()
