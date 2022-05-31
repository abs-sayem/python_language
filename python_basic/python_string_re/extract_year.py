# Write a Pandas program to extract year between 1800 to 2200 from the specified column of a given DataFrame.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
dataframe = pd.DataFrame({
    'Employee_Name': ['Hasan', 'Saifa', 'Sayem', 'Inan', 'Faisal', 'Nowshad'],
    'Joined_Year': ['Hasan 1918', 'Saifa 2020', 'Sayem 2022', 'Tanvir 2221', 
                    'Faisal 2922', 'Nowshad 3011']
})
print("\nOriginal Dataframe:")
print(dataframe)

def find_year(text):
    year = re.findall(r"\b(19[0-9]{2}|20[0-8][0-9]|200[0-9]|2[01][0-9]{2}|2[0-9][0-9]{2}|3011)\b", text)
    return year

dataframe['Extracted_Year'] = dataframe['Joined_Year'].apply(lambda x: find_year(x))
print("\n Extracting Year:")
print(dataframe)