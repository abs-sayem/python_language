# Write a Pandas program to extract email from a specified column of string type of a given DataFrame.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
dataframe = pd.DataFrame({
    'Name_Email': ['Alchemy Software Limited alchemy-bd@bd.org', 
            'Hasan Mozumder hasanweight420@hotmail.com', 
            'Saifa Shahid saifashahid08@gmail.com', 
            'Abs Sayem abs.alchemy20@outlook.com', 
            'Tanvir Ishraq Khan tanvirishraqkhan@gmail.com', 
            'GM Faisal gm_faisal@yahoo.com', 
            'Nowshad Amin amin.nowshad@gmail.com']
})
print("Original Dataframe:")
print(dataframe)
# Define find_email function
def find_email(text):
    email = re.findall(r'[\w\._-]+@[\w\._-]+', str(text))
    return " ".join(email)
# Extract email
dataframe['Extracted_Email'] = dataframe['Name_Email'].apply(lambda x: find_email(x))
print("\nExtracted Email from the DataFrame:")
print(dataframe)