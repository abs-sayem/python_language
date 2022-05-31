''' In traditional madlib, there have been a bunch of blanks in a paragraph and these blanks needs to be fill.
Here, we are going to create this project in Python using string concatenation.'''
# String concatenation(put string together) - by removing white spaces, new line etc.
''''
nlp = "Natural Language Processing"

# few ways to concatenate string
print(nlp + " is the ability of a computer program to understand human language.")
print("{} is the ability of a computer program to understand human language.".format(nlp))
print(f"{nlp} is the ability of a computer program to understand human language.")  # f-string
'''
adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
adv = input("Adverb: ")
madlib = f"Computer programming is so {adj}! It make me so excited all the time because\
I love to {verb1}. Stay safe and {verb2} your hands after a while {adv}."
print(madlib)