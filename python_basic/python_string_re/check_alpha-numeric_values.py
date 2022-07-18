# Write a Pandas program to check whether alpha numeric values present in a given column of a DataFrame.
# Note: isalnum() function returns True if all characters in the string are alphanumeric and
# there is at least one character, False otherwise.
# Alphanumeric: a character that is either a letter or a number.

import pandas as pd
dataframe = pd.DataFrame({
    'Name': ['Hasan', 'Saifa17', 'Sayem', '19Tanvir', '01313406638', 'Nowshad 39'],
    'Date_of_Birth': ['17/02/1992', '01/01/1995','12/11/1994', '23/08/1993', '09/09/1994', '16/10/1994'],
    'Age': [28.10, 25.11, 26.01, 26.11, 26.03, 26.02]
})
print("Original Dataframe:")
print(dataframe)

# Check whether alpha-numeric values are present
dataframe['Is_Name_Alpha-Numeric'] = list(map(lambda x: x.isalnum(), dataframe['Name']))
print("\nChecking whether Name Values are Alpha Numeric")
print(dataframe)
#--------------------------------------------------------------------------------------------------------
# Write a Pandas program to check whether alphabetic values present in a given column of a DataFrame.
# Note: isalpha() returns True if all characters in the string are alphabetic and 
# there is at least one character, False otherwise.

# Check whether alpha-numeric values are present
dataframe['Is_Name_Alphabetic'] = list(map(lambda x: x.isalpha(), dataframe['Name']))
print("\nChecking whether Name Values are Alphabetic")
print(dataframe)
#-------------------------------------------------------------------------------------------------------
# Write a Pandas program to check whether only numeric values present in a given column of a DataFrame.
# Note: isdigit() returns True if all characters in the string are digits, False otherwise.

# Check whether only numeric values are present
dataframe['Is_Name_Numeric'] = list(map(lambda x: x.isdigit(), dataframe['Name']))
print("\nChecking whether Name is only Number:")
print(dataframe)