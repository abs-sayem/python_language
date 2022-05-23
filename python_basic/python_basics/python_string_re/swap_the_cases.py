# Write a Pandas program to swap the cases of a specified character column in a given DataFrame.

import pandas as pd
dataframe = pd.DataFrame({
    'Company_Name': ['Google', 'ALCHEMY', 'Microsoft Corporation', 'tesla', 'Hewlett-Packard', 'GrameenPhone'],
    'Date_of_Foundation': ['Sep 04 1998', 'Jan 01 2010','Apr 04 1975', 'Jul 01 2003', 'Jan 01 1939', 'Jan 01 1997'],
    'Number_of_Employees': [139995, 50, 182268, 70757, 53000, 2086]
})
print("Original Dataframe:")
print(dataframe)

# Swap the cases of string of Company_Name column
dataframe['Swapped_Company_Name'] = list(map(lambda x: x.swapcase(), dataframe['Company_Name']))
print("\nSwapped Company_Name Column:")
print(dataframe) 