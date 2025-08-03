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
# student1 = student.copy() # .copy returns a shallow copy
# print(student1)

# item = student1.pop("dob")
# print(item)
# print(student1)
# item1 = student1.popitem()
# print(item1)

# Problems on dict

# student_detail_1 = {"name":"Priyanshu Jangid","age":25}
# student_detail_2 = {"dob":"Aug-5-1997","Sex":"Male"}

# different ways to merge two dicts
# student_all_details = student_detail_1 | student_detail_2
# student_all_details = {**student_detail_1 , **student_detail_2}
# print(student_all_details)

# python program to merge all values in dict.

# dict1 = {"num1":100,"num2":200,"num3":300,"num4":400,"num5":500,"num6":600}

total = 0
# for value in dict1.values():
#     total += value

# print("Total Sum: ", total)


# Program to count the frequency in a list

# numbers = [1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,6,6,6,6]
#
# number_freq = {}
#
# for number in numbers:
#     number_freq[number] = number_freq.get(number,0) + 1
#
#
# print("********** List Number Frequency ***************")
# print(number_freq)

num_dict1 = {10:100,20:200,30:300,40:400}
num_dict2 = {40:300,50:500,60:600,70:700,80:800}



for key in num_dict2:
    if key in num_dict1.keys():
        num_dict1[key] = num_dict2[key] + num_dict1[key]

    else:
        num_dict1[key] = num_dict2[key]

# print(num_dict1)