# Here, we will determine the highest number among 3 numbers.

def determineHighestNumber(x, y, z):
    if (x > y):
        if(x > z):
            print(f"{x} is the highest number.\n")
        else:
            print(f"{z} is the highest number.\n")
    else:
        if(y > z):
            print(f"{y} is the highest number.\n")
        else:
            print(f"{z} is the highest number.\n")

while(True):
    first_number = int(input("Enter the 1st number: "))
    second_number = int(input("Enter the 2nd number: "))
    third_number = int(input("Enter the 3rd number: "))
    determineHighestNumber(first_number, second_number, third_number)