


#abstract base classes-abc
from abc import ABC , abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("it is rumming")

class Programmer:
    def work(self,com):
        print("printing bugs")
        com.process()
com1 = Laptop()
prog1 = Programmer()
prog1.work(com1)
