# Write a Pandas program to count of occurrence of a specified substring in a DataFrame column.

import pandas as pd

dataframe = pd.DataFrame({
    'Name_Code': ['RnD16', 'RnD17', 'RnD18', 'RnD19', 'RnD38', 'RnD39'],
    'Date_of_Birth': ['17/02/1992', '01/01/1995','12/11/1994', '23/08/1993', '09/09/1994', '16/10/1994'],
    'Age': [28.10, 25.11, 26.01, 26.11, 26.03, 26.02]
})
print("Original Dataframe:")
print(dataframe)

# Count a specific substring
dataframe['count'] = list(map(lambda x: x.count("RnD"), dataframe['Name_Code']))
# count fn finds the specipic substring from the string column. We cannot count from age column,
# because float object has no attribute 'count'.
print("\nCount occurence of RnD in Name_Code column")
print(dataframe)

dataframe['Count'] = list(map(lambda x: x.count("9"), dataframe['Date_of_Birth']))
print("\nCount occurence of 9 in Date_of_Birth column")
print(dataframe)