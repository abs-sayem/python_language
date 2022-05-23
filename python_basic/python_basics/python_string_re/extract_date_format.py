# Write a Pandas program to extract date (format: mm-dd-yyyy) from a given column of a given DataFrame.

import pandas as pd
import re

dataframe = pd.DataFrame({
    'Name_Code': ['RnD16', 'RnD17', 'RnD18', 'RnD19', 'RnD38', 'RnD39'],
    'Date_of_Birth': ['02/17/1992', '01/01/1995','12/13/1994', '23/08/1993', '09/09/1994', '16/10/1994'],
    'Age': [28.10, 25.11, 26.01, 26.11, 26.03, 26.02]
})
print("Original Dataframe:")
print(dataframe)

def find_date_format(date):
    date_format = re.findall(r'\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\b', date)
    return date_format

dataframe['Valid_Date'] = dataframe['Date_of_Birth'].apply(lambda date: find_date_format(date))
print("\nExtracting Valid Dates:")
print(dataframe)