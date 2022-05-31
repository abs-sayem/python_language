# Write a Pandas program to extract only words from a given column of a given DataFrame.

import pandas as pd
import re

dataframe = pd.DataFrame({
    'Name_Code': ['RnD16', 'RnD17', 'RnD18', 'RnD19', 'RnD38', 'RnD39'],
    'Date_of_Birth': ['Feb/17/1992', 'Jan/01/1995','Dec/13/1994', 'Aug/23/1993', 'Sep/09/1994', 'Oct/16/1994'],
    'Address': ['Vatiyari', '21-Lane Road', 'Lake View 4455', 'Foyslake', '2 No gate', 'Nowapara']
})
print("\nOriginal Dataframe:")
print(dataframe)

def extract_only_words(text):
    extracted_words = re.findall(r'\b[^\d\W]+\b', text)
    return " ".join(extracted_words)

#dataframe['Words_Only'] = dataframe['Name_Code'].apply(lambda x: extract_only_words(x))
#dataframe['Words_Only'] = dataframe['Date_of_Birth'].apply(lambda x: extract_only_words(x))
dataframe['Words_Only'] = dataframe['Address'].apply(lambda x: extract_only_words(x))
print("\nExtracting only Words:")
print(dataframe)
#------------------------------------------------------------------------------------------

# Write a Pandas program to extract words starting with capital words from a given column of a given DataFram.
def find_capital_word(sentence):
    capital_words = re.findall(r'\b[A-Z]\w+', sentence)
    return capital_words

dataframe['Capital_Words'] = dataframe['Address'].apply(lambda x: find_capital_word(x))
print("\nFinding Capital Words:")
print(dataframe)
