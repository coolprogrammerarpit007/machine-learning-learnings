# Data Structures in Python

# 1. Lists
# 2. Tuples
# 3. Dictorniories
# 4. Sets


# lists in python
numbers = [1,2,3,4,5,6]

# for number in numbers:
#     print(f"Number: {number}")

# Problems on Lists

# num_list = [45,-78,25,-98,65,789,-987,25,-98,-964]
# # print positive and negative numbers inside a list.
#
# for number in num_list:
#     if number > 0:
#         print(f"Positive Number: {number}")
#
#     else:
#         print(f"Negative Number: {number}")


# Find the Mean of the elements inside lists.

# num_list = [25,34,78,95,25,14,65]
# count = 0
# total = 0
#
# for number in num_list:
#     count += 1
#     total += number
#
#
# print(f"Average: {total/count}")

# problem to find the largest and second largest number inside a list.

def find_largest_number(numbers = []):
    largest_number = None
    second_largest_number = None

    for index in range(len(numbers)):
        if largest_number is None or largest_number < numbers[index]:
            largest_number = numbers[index]

        else:
            pass

    if largest_number is not  None:
        numbers.remove(largest_number)
        for number in numbers:
            if second_largest_number is None or second_largest_number < number:
                second_largest_number = number

            else:
                pass

    return [largest_number,second_largest_number]

numbers = [1,78,25,96,35,78,123,-98,456,254,953]
# largest,second_largest = find_largest_number(numbers)
# print(f"Largest Number: {largest}")
# print(f"Second Largest Number: {second_largest}")

# check is a list is sorted or not.

def check_is_sorted(numbers):
    is_sorted = True

    for index in range(len(numbers)):
        if index < len(numbers)-1 and numbers[index] > numbers[index + 1]:
            is_sorted = False
            break

        else:
            continue

    return is_sorted

numbers1 = [1,2,3,4,5,6]
# result = check_is_sorted(numbers)
result = check_is_sorted(numbers1)
print(f"List is Sorted: {result}")