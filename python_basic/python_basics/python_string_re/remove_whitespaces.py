# Write a Pandas program to remove whitespaces, left sided whitespaces and right sided whitespaces 
# of the string values of a given pandas series.

import pandas as pd

color = pd.Index(['Red   ', ' Green', '  Blue  ', 'Maroon', 'Off  White'])
print("\nOriginal Series:")
print(color, "\n")
print("Remove Whitespaces:")
print(color.str.strip(), "\n")
print("Removed Left Sided Whitespaces:")
print(color.str.lstrip(), "\n")
print("Removed Right Sided Whitespaces:")
print(color.str.rstrip(), "\n")