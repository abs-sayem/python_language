# Write a Pandas program to find the index of a given substring of a DataFrame column.

import pandas as pd

dataframe = pd.DataFrame({
    'Name': ['Hasan', 'Saifa', 'Sayem', 'Tanvir', 'Faisal', 'Nowshad'],
    'Date_of_Birth': ['17/02/1992', '01/01/1995','12/11/1994', '23/08/1993', '09/09/1994', '16/10/1994'],
    'Age': [28.10, 25.11, 26.01, 26.11, 26.03, 26.02]
})
print("Original Dataframe:")
print(dataframe)

# Find the index of occurrence of 0 in Date_of_Birth column.
dataframe['Index_0_DoB'] = list(map(lambda x: x.find('0'), dataframe['Date_of_Birth']))
print("\nIndex of all occurance of 0 in Date_of_Birth column")
print(dataframe)

# Write a Pandas program to find the index of a substring of DataFrame with beginning and end position.

# Finding index of a sub-string in a specified column
dataframe['Index_Substring'] = list(map(lambda x: x.find('a', 0, 7), dataframe['Name']))
print("\nFinding index of a sub-string in a specified column")
print(dataframe)