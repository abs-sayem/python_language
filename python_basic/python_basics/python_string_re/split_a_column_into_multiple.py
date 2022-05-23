# Write a Pandas program to split a string of a column of a given DataFrame into multiple columns.

import pandas as pd
dataframe = pd.DataFrame({
    'Name': ['Hasan Mazumder', 'Saifa Shahid', 'Abs Sayem', 'Tanvir Ishraq Khan', 'GM Faisal', 'Nowshad Amin'],
    'Date_of_Birth': ['17/02/1992', '01/01/1995','12/11/1994', '23/08/1993', '09/09/1994', '16/10/1994'],
    'Age': [28.10, 25.11, 26.01, 26.11, 26.03, 26.02]
})
print("Original Dataframe:")
print(dataframe)

# Split Name column into multiple
dataframe[["First", "Middle", "Last"]] = dataframe["Name"].str.split(" ", expand=True)
print("\nSplit Name Column in Multiple Columns:")
print(dataframe)