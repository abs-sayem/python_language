# Write a Pandas program to get the length of the string present of a given column in a DataFrame.

import pandas as pd
dataframe = pd.DataFrame({
    'Company_Name': ['Google', 'ALCHEMY', 'Microsoft Corporation', 'tesla', 'Hewlett-Packard', 'GrameenPhone'],
    'Date_of_Foundation': ['Sep 04 1998', 'Jan 01 2010','Apr 04 1975', 'Jul 01 2003', 'Jan 01 1939', 'Jan 01 1997'],
    'Number_of_Employees': [139995, 50, 182268, 70757, 53000, 2086]
})
print("Original Dataframe:")
print(dataframe)

# Determine length of the string of a column
dataframe['Company_Name_Length'] = dataframe['Company_Name'].apply(len)
print("\nLength of the string of Company_Name column:")
print(dataframe)
#-----------------------------------------------------------------------------------
# Write a Pandas program to get the length of the integer of a given column in a DataFrame.

# Determine length of the integer of a column
dataframe['Length_of_NoE'] = dataframe['Number_of_Employees'].map(str).apply(len)
print("\nLength of the integer of Number_of_Employees column:")
print(dataframe)