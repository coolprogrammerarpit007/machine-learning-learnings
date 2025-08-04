# Advanced Stuff in Python

# decorators in Python

# def decorate(fn):
#     def wrapper():
#         print("Hello buddy, Who are you?")
#         fn()
#         print("Hello, Arpit Nice to meet you!")
#     return wrapper
#
# @decorate
# def hello():
#     print("Hello, my name is Arpit Mishra!")
#
# hello()


# decorators capture the function which is given a decorator.
# wrapper captures the args given to that function.


# *args and **kwargs in python

def addition(*args):
    total = 0
    for num in args:
        total += num

    return total

total = addition(1,2,3,4,5,6,7,8,9,10)
# print(f"Total: {total}")


# *args stands for Arguments.
# **kwargs, kwargs stands for Keyword Arguments.

def user(**kwargs):
    return kwargs


student = user(name = "Arpit",age = 26,sex = "Male",job = "Software-developer")
# print(student)


# List,Set and Dictionary Comprehensions

# List Comprehension

# labels = ["Even" if x % 2 == 0 else "ODD" for x in range(25)]

# print(labels)
even_numbers = [num for num in (range(21)) if num % 2 ==0]
# print(even_numbers)


# dict Comprehensions

squares = {x : x * x for x in range(50) if x % 2 == 0}
# print(squares)



# Set comprehensions

uniqye_set_elems = {x*x for x in range(16)}
# print(uniqye_set_elems)


# Lambda Functions

addition_two_numbers = lambda x,y : x+y
# print(f"Addition of two numbers: {addition_two_numbers(25,27)}")


# MAP,ZIP AND FILTER

# numbers = [1,2,3,4,5]
# doubled_numbers = map(lambda num : num * 2,numbers)
# print(list(doubled_numbers))

# filter
numbers = list(range(21))
even_numbers_list = list(filter(lambda num:num % 2 ==0,numbers))
# print(even_numbers_list)


