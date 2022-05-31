# First, we will take inputs from user and let computer choice randomly.
# Then, we will set some rules according to: rock>scissor, scissor>paper and paper>rock

import random

def is_win(player, opponent):
    # This function will return true if the conditions satisfy.
    # Conditions: rock>scissor, scissor>paper and paper>rock
    if player == 'r' and opponent == 's':
        return True
    elif player == 's' and opponent == 'p':
        return True
    elif player == 'p' and opponent == 'r':
        return True

def play():
    #print("\nr for Rock\np for Paper\ns for Scissor\nEnter any one: ")
    user = input("Whats your choice?\n'r' for Rock\n'p' for Paper\n's' for Scissors\n     You: ")
    computer = random.choice(['r', 'p', 's'])
    print("Computer:", computer)

    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost."

print(play())