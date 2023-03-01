# Guessing Game: Where the computer has a secret number, and we are trying to guess the number.
# So, the first step is to make the computer generate a secret number for us to guess.
# And the second step is to guess a number and computer will tell us whwther it is too high or low or\
# guessed correctly. We need to keep looping untill we get the right number.

import random

# === User will guess the number ===
def userGuessNumber(x):
    random_number = random.randint(1, x)    # randint generates a random number range of given parameters.
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess < random_number:
            print(f"Sorry! Guess again. {guess} is too low.")
        elif guess > random_number:
            print(f"Sorry! Guess again. {guess} is too high.")
        
    print(f"Congrats! {guess} is the number.")

# === Computer guess the number ===
def systemGuessNumber(x):
    user_number = int(input(f"Enter any number between 1 and {x}: "))
    if user_number > x:
        raise ValueError(f"Enter the number less than {x}")
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} is too high(h), too low(l) or correct(c): ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Congrats! {guess} is the number.")

# === Automatic Computer guess the number ===
def automaticSystemGuessNumber(x):
    user_number = int(input(f"Enter any number from 1 to {x}: "))
    if user_number > x or user_number < 0:
        raise ValueError(f"Enter the number from 1 to {x}")
    low = 1
    high = x
    guess = -1
    count = 0
    while user_number != guess:
        guess = random.randint(low, high)
        count = count+1
        #if guess == user_number:
            #print(f"Congrats! {guess} is the number.")
            #break
        if guess > user_number:
            print(f"{guess} is too high")
            high = guess - 1
        elif guess < user_number:
            print(f"{guess} is too low")
            low = guess + 1
    print(f"Congrats! {guess} is the number.")
automaticSystemGuessNumber(100)