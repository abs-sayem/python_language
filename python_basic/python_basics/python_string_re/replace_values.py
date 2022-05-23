# Write a Pandas program to replace arbitrary values with other values in a given DataFrame.

import pandas as pd
dataframe = pd.DataFrame({
    'Company_Name': ['G', 'A', 'M', 'T', 'A', 'B'],
    'Date_of_Foundation': ['Sep 04 1998', 'Jan 01 2010','Apr 04 1975', 'Jul 01 2003', 'Jan 01 1939', 'Jan 01 1997'],
    'Number_of_Employees': [139995, 50, 182268, 70757, 53000, 2086]
})
print("Original Dataframe:")
print(dataframe)

# Replace arbitrary values with other values
# replace() function only replace one character word
dataframe = dataframe.replace("A", "x")
print("\nReplace Arbitrary Values by Another Values")
print(dataframe)
#-----------------------------------------------------------------------------------------------
# Write a Pandas program to replace more than one value with other values in a given DataFrame

# Replace more than one value with other values
dataframe = dataframe.replace(["A", "T"], ["x", "y"])
print("\nReplace more than one Values by Another Values")
print(dataframe)