# Write a Pandas program to extract the sentences where a specific word is present in a given column of 
# a given DataFrame.

import pandas as pd
import re

dataframe = pd.DataFrame({
    'Name_Code': ['RnD16', 'RnD17', 'RnD18', 'RnD19', 'RnD38', 'RnD39'],
    'Date_of_Birth': ['Feb/17/1992', 'Jan/01/1995','Dec/13/1994', 'Aug/23/1993', 'Sep/09/1994', 'Oct/16/1994'],
    'Address': ['Vatiyari', '21-View Lane', 'LakeView R/A 4455', 'Foyslake\nFoyslake', '2 No gate', 'GreenView R/A']
})
print("\nOriginal Dataframe:")
print(dataframe)

def sentence_of_specific_word(sentence, word):
    required_sentence = re.findall(r'([^.]*'+word+'[^.]*)', sentence)
    return required_sentence

dataframe['Sentence_Containing_Specific_Word'] = dataframe['Address'].apply(lambda x: sentence_of_specific_word(x, 'View'))
print("\nExtracting Sentence of Specific Word:")
print(dataframe)
#-------------------------------------------------------------------------------------------------------------

# Write a Pandas program to extract the unique sentences from a given column of a given DataFrame.
def find_unique_sentence(sentence):
    unique_sentence = re.findall(r'(?sm)(^[^\r\n]+$)(?!.*^\1$)', sentence)
    return unique_sentence

dataframe['Unique_Sentence'] = dataframe['Address'].apply(lambda x: find_unique_sentence(x))
print("\nExtracting Unique Sentence:")
print(dataframe)