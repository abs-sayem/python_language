# Write a Pandas program to check whether only lower case or upper case is present in a given column 
# of a DataFrame.

import pandas as pd
dataframe = pd.DataFrame({
    'Company_Name': ['Google', 'ALCHEMY', 'Microsoft Corporation', 'tesla', 'Hewlett-Packard', 'GrameenPhone'],
    'Date_of_Foundation': ['Sep 04 1998', 'Jan 01 2010','Apr 04 1975', 'Jul 01 2003', 'Jan 01 1939', 'Jan 01 1997'],
    'Number_of_Employees': [139995, 50, 182268, 70757, 53000, 2086]
})
print("Original Dataframe:")
print(dataframe)

# Check Lowercase
dataframe['Is_Lowercase'] = list(map(lambda x: x.islower(), dataframe['Company_Name']))
print("\nIs Company Name is Lowercased:")
print(dataframe)

# Check Uppercase
dataframe['Is_Uppercase'] = list(map(lambda x: x.isupper(), dataframe['Company_Name']))
print("\nIs Company Name is Uppercased:")
print(dataframe)
#------------------------------------------------------------------------------------------
# Write a Pandas program to check whether only proper case or title case is present in a given column 
# of a DataFrame.

# Check Prper Case or Title Case
dataframe['Is_Titlecase'] = list(map(lambda x: x.istitle(), dataframe['Company_Name']))
print("\nIs Comapny Name is Title Case:")
print(dataframe)