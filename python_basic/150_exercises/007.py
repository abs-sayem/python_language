# Write a Python program to accept a filename from the user and print the extension of that.
#   Sample Input: main.py
#   Sample Output: py

file_name = input("Enter the filename:")

def find_extension(file_name):
    file_extension = file_name.split(".")
    print("The extension of the file is:" + repr(file_extension[-1]))

find_extension(file_name)