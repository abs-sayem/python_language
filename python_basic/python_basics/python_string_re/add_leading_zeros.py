# Write a Pandas program to add leading zeros to the integer column in a pandas series and makes 
# the length of the field to 8 digit.

import pandas as pd

numbers = {'Amount': [8, 17, 350, 7100, 14200, 285000, 5710000, 11430000]}
dataframe = pd.DataFrame(numbers)
print("Original Dataframe:")
print(dataframe)

# Adding the leading zeros upto 8 digit
dataframe['Amount'] = dataframe['Amount'].apply(lambda x:'{0:0>8}'.format(x))
print("\nAdding Leading Zeros:")
print(dataframe)

# Write a Pandas program to add leading zeros to the character column in a pandas series 
# and makes the length of the field to 8 digit.

# Adding the leading zeros, make the length upto 10 digit
dataframe['Amount'] = list(map(lambda x: x.zfill(10), dataframe['Amount']))
print("\nAdding Leading Zeros:")
print(dataframe)
