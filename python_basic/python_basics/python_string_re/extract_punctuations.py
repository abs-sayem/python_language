# Write a Pandas program to extract only punctuations from the specified column of a given DataFrame.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
dataframe = pd.DataFrame({
    'Employee_Code': ['Hasan.16', 'Saifa#17', '^Sayem@18', 'Inan*?19', '$Faisal38@', '!39,Nowshad'],
    'Joined_Year': ['Hasan 1918', 'Saifa 2020', 'Sayem 2022', 'Tanvir 2221', 
                    'Faisal 2922', 'Nowshad 3011']
})
print("\nOriginal Dataframe:")
print(dataframe)

def find_punctuation(text):
    punctuation_only = re.findall(r'[!"\$%&\'()*+,\-.\/:;=#@?\[\\\]^_`{|}~]*', text)
    string = "".join(punctuation_only)
    return list(string)

# Extracting Only Punctuation from a column
dataframe['Punctuation_Only'] = dataframe['Employee_Code'].apply(lambda x: find_punctuation(x))
print("\nExtracting Only Punctution:")
print(dataframe)