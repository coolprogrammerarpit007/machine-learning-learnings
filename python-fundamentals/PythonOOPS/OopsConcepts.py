# Object Oriented Programming
# Student Class

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.course = "Computer Science"
#
#     def studentIntro(self):
#         return f"Hello, my name is {self.name}. I am {self.age} years old student who is going to study {self.course} "
#
# student1 = Student("Sachin Mishra",18)
# print(student1.studentIntro())


# Class Attributes and Instance Attributes

# class Animal:
#     species = "Mammals"  # class Attribute
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age   # Instance Attributes
#
#     # Instance Method
#     def getIntro(self):
#         return f"{self.name} is a {self.age} years old wild species."
#
#     # Class Method
#
#     @classmethod
#     def mammalsEvolution(cls):
#         return f"{cls.species} evolves around millenia, These species directly reproduce their offsprings."
#
#     # Static Methods
#     @staticmethod
#     def adultAnimals():
#         print("Most Animals above 2-3 years are generally considered adult.")
#
#
# animal1 = Animal("Lion",12)
# print(animal1.getIntro())
# print(animal1.species)
# print(animal1.mammalsEvolution())
# animal1.adultAnimals()


# 4 Pillars Of Object Oriented Programming
# 1. Abstraction
# 2. Inheritance
# 3. Polymorphism
# 4. Encapsulation

# Inheritance
# class FactoryMumbai:
#     a = "I am an attribute mentioned inside class factory of mumbai."
#
#     def hello(self):
#         print("Hello, I am a factory method inside factory of mumbai.")
#
# class FactoryPune(FactoryMumbai):
#     pass
#
# factory = FactoryPune()
# factory.hello()

# class Animal:
#     def __init__(self,name):
#         self.name = name
#
#     def show(self):
#         print(f"Hello my name is: {self.name}")
#
#
# class Horse(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#
#     def self_description(self):
#         print(f"{self.name} has {self.age} years old brain!")
#
# horse = Horse("Zubair",23)
# horse.show()
# horse.self_description()

# Multiple  Inheritance

# class Lion:
#     name1 = "Lion"
#
# class Human:
#     name2 = "Human"
#
# class Robots(Lion,Human):
#     name3 = "Chithi Babu"
#
# obj = Robots()
# print(obj.name1)
# print(obj.name2)
# print(obj.name3)


# Multi-Level Inheritance

class GrandFather:
    def heritage(self):
        print("Heritage from Grandfather")

class Father(GrandFather):
    def parent_heritage(self):
        print("Heritage from father")

class Chid(Father):
    pass

obj = Chid()
obj.heritage()
obj.parent_heritage()