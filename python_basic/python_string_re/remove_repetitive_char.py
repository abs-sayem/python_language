# Write a Pandas program to remove repetitive characters from the specified column of a given DataFrame.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
dataframe = pd.DataFrame({
    'Employee_Code': ['ASL016', 'ASL017', 'ASL018', 'ASL019', 'ASL038', 'ASL039'],
    'Message': ['Doon\'t tell anyone', 'Do anyyone in the washroom?', 'Noo noo, I won\'t doo it.', 'I\'ll try to come tomorrow.', 'What is the problem', 'Whhoo said thaat?']
})
print("Original Dataframe:")
print(dataframe)

def remove_repeted_char(string):
    total_char = string.group(0)
    if len(total_char) > 1:
        return total_char[0:1]  # can change the value on repetition
def unique_char(repeat, sent_text):
    convert = re.sub(r'(\w)\1+', repeat, sent_text)
    return convert
dataframe['Normal_Text'] = dataframe['Message'].apply(lambda x: unique_char(remove_repeted_char, x))
print("\nRemove Repetitive Characters:")
print(dataframe)