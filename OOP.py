class car:
    pass
#object
obj1 = car()
print(obj1)
#constructor
class car:
    def __init__(self, name, color):
     self.name = name
     self.color = color
#modifiers
speed=40
speed+=10
print("speed =", speed)
#encapsulation protected variable
class car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage
    def description(self):
        return f"the {self.name} car gives the mileage of {self. mileage}km/1"
obj= car("bmw 7-series",70.53)
print(obj.description())
print(obj.mileage)
print(obj.name)
#encapsulation private variable
class car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage
    def description(self):
        return f"the {self._name} car gives the mileage of {self.mileage}km/1"
obj = car("honda accord",20.53)
print(obj.description())
print(obj.name)
print(obj.mileage)