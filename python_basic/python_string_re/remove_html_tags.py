# Write a Pandas program to remove the html tags within the specified column of a given DataFrame.

import pandas as pd
import re

dataframe = pd.DataFrame({
    'Name_Code': ['RnD16', 'RnD17', 'RnD18', 'RnD19', 'RnD38', 'RnD39'],
    'Date_of_Birth': ['Feb/17/1992', 'Jan/01/1995','Dec/13/1994', 'Aug/23/1993', 'Sep/09/1994', 'Oct/16/1994'],
    'Address': ['<b>Vatiyari</b>', '<i>21-Lane<i> Road', '<p>Lake View 4455</p>', 'Foyslake', '2 No gate</br>', '<pre>Nowapara</pre>']
})
print("\nOriginal Dataframe:")
print(dataframe)

def remove_html_tag(text):
    tag_removed = re.sub('<.*?>','', text)
    return tag_removed

dataframe['Tag_Removed'] = dataframe['Address'].apply(lambda x: remove_html_tag(x))
print("\nRemoving HTML Tags:")
print(dataframe)