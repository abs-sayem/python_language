# How to pick a random english word from a list.  
# First, we have to take some random english words.

import random
import string
from noun_words import words
#print(words)

def get_valid_word(words):
    word = random.choice(words)     # Randomly choose something from list
    while('-' in word or ' ' in word):
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)    # Keep the Letters in the word as a set
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()     # What the user has guessed

    # Geeting user input
    while(len(word_letters)>0):
        # Tell user words they have already used
        print("You have used these letters: ", " ".join(guessed_letters))   #Each of the characters in string seoerated by space
        
        # Tell user what the current position of the word is (W - R D)
        word_list = [letter if letter in guessed_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        # Taking input from user
        user_letter = input("Guess a letter: ").upper()
        if(user_letter in (alphabet-guessed_letters)):
            guessed_letters.add(user_letter)
            if(user_letter in word_letters):
                word_letters.remove(user_letter)
        elif(user_letter in guessed_letters):
            print("You have already used that character. Please try again.")
        else:
            print("Invalid character. Please try again.")
hangman()