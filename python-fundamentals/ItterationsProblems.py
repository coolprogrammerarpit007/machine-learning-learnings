# number = int(input("Enter Number: "))
# Print Hello World N number of times!
# for index in range(number):
#     print("Hello World!")

# Print Natural Numbers upto N
# for num in range(number+1):
#     print(num)


# Print Natural Numbers from N to 1 in the reverse order.
# for number in range(number,0,-1):
#     print(number)

# Take a number as input and print it's table.

# for number in range(number,(number*10)+1,number):
#     print(number)

# total_of_natural_numbers = 0

# for num in range(number+1):
#     total_of_natural_numbers += num


# print(f"Sum of N natural Numbers: {total_of_natural_numbers}")


#  find the factorial of a number
# fact = 1

# for num in range(1,number+1):
#     fact *= num
#     # print(f"Factorial: {fact}")


# print(f"Factorial Of Natural Numbers are: {fact}")

# sum_of_even_numbers = 0
# sum_of_odd_numbers = 0

# num = int(input("Enter Number: "))

# for number in range(num+1):
#     if number % 2 == 0:
#         # print("Even Number: ",number)
#         sum_of_even_numbers += number

#     else:
#         # print("ODD Number: ",number)
#         sum_of_odd_numbers += number

# print(f"Sum of Even numbers: {sum_of_even_numbers}")
# print(f"Sum of Odd Numbers: {sum_of_odd_numbers}")


# Print All Factors of a number

# number = int(input("Enter Number: "))
# for num in range(1,number+1):
#     if number % num == 0:
#         print(num)



# #  To check if a number is perfect number or not

# number = int(input("Enter Number: "))
# factors = []

# for index in range(1,number):
#     if number % index == 0:
#         factors.append(index)

#     else:
#         continue


# sum_of_factors = sum(factors)
# if  sum_of_factors == number:
#     print(f"Number {number} is a Perfect Number")

# else:
#     print(f"Number {number} is not a Perfect Number.")



# To check whether the given number is Prime Number or Not
# import math

# number = int(input("Enter Number: "))
# is_prime = True

# if number == 2:
#     is_prime

# if number <= 0:
#     print("Enter a valid Positive Number")

# if number > 2:
#     for digit in range(3,number):
#         if number % digit == 0:
#             is_prime = False
#             print("Prime Number Detected!")
#             break


#         else:
#             continue

        


# if is_prime:
#     print(f"Number: {number} is Prime Number")

# else:
#     print(f"Number: {number} is not a prime number!")
            


# Program to reverse a string

# input_string = input("Enter String: ")
# reverse_str = ''
# for index in range(len(input_string)-1,-1,-1):
#     reverse_str += input_string[index]



# print(f"Input String: {input_string}")
# print(f"Output String: {reverse_str}")


# check whether a string is palindrome or not

# input_string = input("Enter String: ")
# is_palindrome_str = False

# output_str = ''

# for char in range(len(input_string)-1,-1,-1):
#     output_str += input_string[char]


# if input_string.upper() == output_str.upper():
#     is_palindrome_str = True


# result = f"{input_string} is a palindrome string." if is_palindrome_str else f"{input_string} is not a palindrome string."

# print(result)

# Program to Count all letters, digits, and special symbols from a given
# string
# Given: str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4

# input_str = input("Enter String: ")
# count_digit = 0
# count_symbol = 0
# count_letters = 0

# for char in input_str:
#     if char.isdigit():
#         count_digit += 1

#     elif char.isalpha():
#         count_letters += 1

#     else:
#         count_symbol += 1

# print(f"Chars = {count_letters}")
# print(f"Digits = {count_digit}")
# print(f"Symbols = {count_symbol}")