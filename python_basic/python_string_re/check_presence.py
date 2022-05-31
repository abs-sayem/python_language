# Write a Pandas program to check whether two given words present in a specified column of a given DataFrame.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
dataframe = pd.DataFrame({
    'Name': ['Hasan', 'Saifa', 'Sayem', 'Inan', 'Faisal', 'Nowshad'],
    'Address': ['4455 Vatiyary View', '12-View Quarter 4455', 'Lake View 4455', 'Foyslake_1055', '2 No Gate View', '4455 East_Nowapara']
})
print("\nOriginal Dataframe:")
print(dataframe)

def test_presence(text):
    word_present = re.findall(r'(?=.*View.)(?=.*4455).*', text)
    return " ".join(word_present)

dataframe['Checked_Words'] = dataframe['Address'].apply(lambda x: test_presence(x))
print("\nChecking the Words Presence:")
print(dataframe)