# Write a Pandas program to extract only phone number from the specified column of a given DataFrame.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
dataframe = pd.DataFrame({
    'Employee_Name': ['Hasan', 'Saifa', 'Sayem', 'Inan', 'Faisal', 'Nowshad'],
    'Phone_Number': ['Hasan 01313406616', 'Saifa 01313406617', 'Sayem 01313406618', 'Tanvir 01313406619', 
                    'Faisal 01313406638', 'Nowshad 01313406639']
})
print("\nOriginal Dataframe:")
print(dataframe)

def find_phone_number(text):
    phone_number = re.findall(r"\b\d{11}\b", text)
    return " ".join(phone_number)

dataframe['Phone_Number'] = dataframe['Phone_Number'].apply(lambda x:find_phone_number(x))
print("\nExtracting Phone Number:")
print(dataframe)