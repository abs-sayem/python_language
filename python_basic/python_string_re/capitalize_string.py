# Write a Pandas program to capitalize all the string values of specified columns of a given DataFrame.

import pandas as pd

dataframe = pd.DataFrame({
    'Name': ['hasan', 'Saifa', 'sayeM', 'InaN', 'FAISAL', 'nOWSHAD'],
    'Date_of_Birth': ['17/02/1992', '01/01/1995','12/11/1994', '23/08/1993', '09/09/1994', '16/10/1994'],
    'Age': [28.10, 25.11, 26.01, 26.11, 26.03, 26.02]
})
print("Original Dataframe:")
print(dataframe)

# Capitalize all the string
dataframe['Name'] = list(map(lambda x: x.capitalize(), dataframe['Name']))
print("\nCapitalizing Name Column:")
print(dataframe)