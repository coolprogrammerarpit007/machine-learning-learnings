# Abstraction in Python
from abc import ABC,abstractmethod

class MathUnit(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(MathUnit):
    def __init__(self,side):
        self.side = side

    def perimeter(self):
        return 2*(self.side + self.side)

    def area(self):
        return self.side * self.side



class Circle:
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius

# print("***************** Square ***********************************")
square = Square(4)
# print(square.area())
# print(square.perimeter())

# print("********************** Circle ******************************")
circle = Circle(4)
# print(circle.perimeter())
# print(circle.area())



# Dunder Methods

class Animal:
    def __init__(self,name,age=0):
        self.name = name
        self.age = age


    def __str__(self):
        return "This is an Animal Class."

    def __add__(self, other):
        return self.age + other.age

animal = Animal("Johnny",5)
print(animal)
animal1 = Animal("Nimo",10)
print(animal1)
print(animal + animal1)