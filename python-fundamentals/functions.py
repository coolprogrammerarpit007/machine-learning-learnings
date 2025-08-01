# functions in Programming

def greet(user_name):
    return f"Hello, Nice to meet you! {user_name}"


# name = input("Enter Name: ")
# result = greet(name)
# print(result)


# keyword arguments

def student_details(name,age):
    return f"Student {name} is {age} year's old!"

# data = student_details(age = 26,name="Arpit")
# print(data)


# default arguments

def addition(num1 = 23,num2 = 78):
    return num1 + num2


result = addition()
# print(result)