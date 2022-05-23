# Fibonacci series
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946

items = int(input("Enter item number:"))

# Inintialize
first_number = 0
second_number = 1

if(items<=0): print("Please! Enter a positive integer")
elif(items==1): print(f"{first_number}")
elif(items==2): print(f"{first_number}\n{second_number}")
elif(items>2):
    number=3
    print(f"{first_number}\n{second_number}")
    while(number <= items):
        number += 1
        next_number = first_number + second_number
        print(f"{next_number}")
        first_number = second_number
        second_number = next_number