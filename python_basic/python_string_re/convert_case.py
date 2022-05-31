#  Write a Pandas program to convert a specified character column in upper/lower cases in a given DataFrame.

import pandas as pd
dataframe = pd.DataFrame({
    'Company_Name': ['Google', 'ALCHEMY', 'Microsoft Corporation', 'tesla', 'Hewlett-Packard', 'GrameenPhone'],
    'Date_of_Foundation': ['Sep 04 1998', 'Jan 01 2010','Apr 04 1975', 'Jul 01 2003', 'Jan 01 1939', 'Jan 01 1997'],
    'Number_of_Employees': [139995, 50, 182268, 70757, 53000, 2086]
})
print("Original Dataframe:")
print(dataframe)

# Convert Company_Name column to upper/lower case
print("\nConvert Company_Name Column to Upper/Lower Case:")
dataframe['Lowered_Company_Name'] = list(map(lambda x: x.lower(), dataframe['Company_Name']))
dataframe['Uppered_Company_Name'] = list(map(lambda x: x.upper(), dataframe['Company_Name']))
print(dataframe)
#----------------------------------------------------------------------------------------------
# Write a Pandas program to convert a specified character column in title case in a given DataFrame.

# Convert Company_Name column to title case
print("\nConvert Company_Name Column to Title Case:")
dataframe['Titled_Company_Name'] = list(map(lambda x: x.title(), dataframe['Company_Name']))
print(dataframe)