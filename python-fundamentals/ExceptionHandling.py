# Exception Handling
from math import remainder

number = input("Enter Number: ")

try:
    digit = int(number)
    remainder = 100/digit

except Exception as err:
    print(f"Sorry, There is an {err} error occurs.")

else:
    print("Good, Their is no error!")

finally:
    print("I will run no matter what!")

print("Thanks, for using it!")