# Write a Pandas program to extract only number from the specified column of a given DataFrame.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
dataframe = pd.DataFrame({
    'Name': ['Hasan', 'Saifa', 'Sayem', 'Inan', 'Faisal', 'Nowshad'],
    'Address': ['5043 Vatiyary', '12-Quarter', 'Akbarshah 4455', 'Foyslake_1055', '2 No Gate', '6657_Nowapara']
})
print("\nOriginal Dataframe:")
print(dataframe)

def find_number(text):
    number = re.findall(r'[0-9]+', text)
    return " ".join(number)

dataframe['Number'] = dataframe['Address'].apply(lambda x: find_number(x))
print("\nExtracting Numbers:")
print(dataframe)

# Write a Pandas program to extract numbers greater than 940 from the specified column of a given DataFrame.

def extract_greater_number(text):
    greater_number = re.findall(r'95[5-9]|9[6-9]\d|[1-9]\d{3,}', text)
    return " ".join(greater_number)

dataframe['Greater_Number'] = dataframe['Address'].apply(lambda x: extract_greater_number(x))
print("\nExtracting Greater Number:")
print(dataframe)

# Write a Pandas program to extract numbers less than 100 from the specified column of a given DataFrame.

def extract_lesser_number(num):
    number = []
    for numbers in num.split():
        lesser_numbers = re.findall(r'\b(0*(?:[1-9][0-9]?|100))\b', numbers)
        number.append(lesser_numbers)
        all_numbers = [",".join(x) for x in number if x != []]
    return " ".join(all_numbers)

dataframe['Lesser_Number'] = dataframe['Address'].apply(lambda x: extract_lesser_number(x))
print("\nExtract Lesser Number:")
print(dataframe)