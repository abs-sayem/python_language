# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
## Python has two programs of taking input from user.
#   raw_input(): takes string data and simply return the string ended with a new line.
#   input(): reads a line from sys.stdin and returns it with the trailing newline stripped.

first_name = input("Input your first name:")
last_name = input("Input your last name:")
def reverse(fpart, lpart):
    print("Your reversed name:", lpart + " " + fpart)
def conjunc(fpart, lpart):
    print("Your reversed name:", fpart + "_" + lpart)

reverse(first_name, last_name)
conjunc(first_name, last_name)