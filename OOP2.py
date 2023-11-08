#inheritance #parent class
class car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage
    def description(self):
        return f"the {self. name} car gives the mileage of {self. mileage}km/1."
#child class
class toyota(car):
    pass
class audi(car):
    def audi_desc(self):
        return "this is the description method of class audi."
obj1 = toyota("corolla S", 35.40)
print(obj1.description())
obj2 = audi("audi A8 L", 15)
print(obj2.description())
print(obj2.audi_desc() )
#POLYMORPHISM
class audi:
    def description(self):
        print("this is the description function of class audi.")
class bmw:
    def description(self):
        print("this is the description function of class bmw.")
audi = audi()
bmw = bmw()
for car in (audi,bmw):
    car.description()
#abstraction
from abc import ABC, abstractmethod
class car(ABC):
    def __init__(self, name):
        self.name = name
    def description(self):
        print("this is the description function of class car.")
    @abstractmethod
    def price(self,x):
        pass
class new(car):
    def price(self,x):
        print(f"the {self.name}'s price is {x} naira.")
obj = new("Honda Crv")
obj.description()
obj.price(3000)
#interface
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def balance_check(self):
        pass
    @abstractmethod
    def interest(self):
        pass
class SBL(Bank):
    def balance_check(self):
        print("Balance is 1000 naira.")
    def interest(self):
        print("SBL interest is 500 naira.")
obj = SBL()
obj.balance_check()
obj.interest()