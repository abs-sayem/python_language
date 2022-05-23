# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
#   Sample Input: 3,5,7,9
#   Sample Output: List:['3','5','7','9']   # List holds comma seperated values between square brackets
#                  Tuple: ('3','5','7','9') # Tuple holds comma seperated values between parentheses

from typing import Tuple

values = input("Input some comma separated numbers:")
def list_generator(values):
    your_list = values.split(",")
    print("Your List:", your_list)
def tuple_generator(values):
    your_list = values.split(",")
    your_tuple = tuple(your_list)
    print("Your Tuple:", your_tuple)

list_generator(values)
tuple_generator(values)