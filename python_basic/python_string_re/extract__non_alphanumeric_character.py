# Write a Pandas program to extract only non alphanumeric characters from the specified column 
# of a given DataFrame.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
dataframe = pd.DataFrame({
    'Employee_Code': ['Hasan16', 'Saifa#17', '^Sayem@18', 'Inan*?19', '$Faisal38@', '!39Nowshad'],
    'Joined_Year': ['Hasan 1918', 'Saifa 2020', 'Sayem 2022', 'Tanvir 2221', 
                    'Faisal 2922', 'Nowshad 3011']
})
print("\nOriginal Dataframe:")
print(dataframe)

def find_nonalphanumeric(text):
    nonalphanumeric = re.findall("[^A-Za-z0-9]", text)
    return nonalphanumeric

# Extract Non-Alphanumeric Characters
dataframe['NonAlphanumeric'] = dataframe['Employee_Code'].apply(lambda x: find_nonalphanumeric(x))
print("\nExtract Non AlphaNumeric Characters:")
print(dataframe)