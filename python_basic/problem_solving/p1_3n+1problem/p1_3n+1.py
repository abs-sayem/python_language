# Taking the number of numbers to be printed
number = int(input("Enter any number between 0 and 1000000:"))
print(number)
if(number <= 0): print("Please enter a number greater than 0")
if(number > 1000000): print("Enter a number less than 1000000")
else:
    if(number%2 == 0): number = number/2
    elif(number%2 != 0): number = (3*number+1)
    print(number)