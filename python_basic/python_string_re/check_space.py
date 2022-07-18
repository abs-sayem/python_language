# Write a Pandas program to check whether only space is present in a given column of a DataFrame.

import pandas as pd
dataframe = pd.DataFrame({
    'Company_Name': ['Google', ' ', 'Microsoft Corporation', 'tesla', 'Hewlett-Packard', 'GrameenPhone'],
    'Date_of_Foundation': ['Sep 04 1998', 'Jan 01 2010','Apr 04 1975', 'Jul 01 2003', 'Jan 01 1939', 'Jan 01 1997'],
    'Number_of_Employees': [139995, 50, 182268, 70757, 53000, 2086]
})
print("Original Dataframe:")
print(dataframe)

# Check whether there is anly space in Company Name
dataframe['Is_only_Space'] = list(map(lambda x: x.isspace(), dataframe['Company_Name']))
print("\nIs there is only Space in Company Name:")
print(dataframe)