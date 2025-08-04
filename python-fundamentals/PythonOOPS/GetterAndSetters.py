class Person:
    _country = "India"

    def __init__(self,age):
        self.__age = age

    def get_age(self):
        return self.__age
    

    def set_age(self,x):
        self.__age = x

    def is_eligible_for_vote(self):
        result = "Eligble for vote" if self.__age > 18 else "Not Eligble for Vote"
        return result
    

person = Person(25)
print(person.get_age())
print(person.is_eligible_for_vote())

person.set_age(10)
print(person.get_age())
print(person.is_eligible_for_vote())

