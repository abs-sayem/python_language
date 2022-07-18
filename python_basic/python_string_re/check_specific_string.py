# Write a Pandas program to check if a specified column starts with a specified string in a DataFrame.

import pandas as pd
dataframe = pd.DataFrame({
    'Company_Name': ['Google', 'ALCHEMY', 'Microsoft Corporation', 'tesla', 'Hewlett-Packard', 'GrameenPhone'],
    'Date_of_Foundation': ['Sep 04 1998', 'Jan 01 2010','Apr 04 1975', 'Jul 01 2003', 'Jan 01 1939', 'Jan 01 1997'],
    'Number_of_Employees': [139995, 50, 182268, 70757, 53000, 2086]
})
print("Original Dataframe:")
print(dataframe)

# If a specified column starts with a specified string
dataframe['Company_Name_Starts_With'] = list(map(lambda x: x.startswith('G'), dataframe['Company_Name']))
print("\nIf a specified column starts with a specified string:")
print(dataframe)