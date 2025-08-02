# Dictionary In Python

student = {
    "name":"Sachin Mishra",
    "age" : 18,
    "Sex" : "M",
    "Course":"Engineering",
    "Specilization":"Computer Science"
}

student.update({"dob":"31-July-2006"})
# print(student)


# only values not keys can be updated.

# Traversing Over Dictorniries

# for key in student:
    # print(f"Student {key} : {student[key]} ")

# for key,value in student.items():
    # print(f"Student {key}: {value}")


# dict methods

# student.clear()
student1 = student.copy() # .copy returns a shallow copy
# print(student1)

# item = student1.pop("dob")
# print(item)
# print(student1)
# item1 = student1.popitem()
# print(item1)