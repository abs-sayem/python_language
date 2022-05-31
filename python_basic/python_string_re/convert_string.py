# Write a Pandas program to convert all the string values to upper, lower cases in a given pandas series.\
# Also find the length of the string values.
import pandas as pd
import numpy as np

s = pd.Series(['X', 'y', 'Z', 'Sayem', 'Abs', 'Abs Sayem', None, 'Bird', 'hASAn', 'saIfa', 'tanvir'])

print("Original Series:")
print(s)
print("Upper Case Series:")
print(s.str.upper())
print("Lower Case Series:")
print(s.str.lower())
print("Length of the Series:")
print(s.str.len())