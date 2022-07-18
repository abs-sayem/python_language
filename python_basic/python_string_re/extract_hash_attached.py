# Write a Pandas program to extract hash attached word from twitter text from the specified column of 
# a given DataFrame.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
dataframe = pd.DataFrame({
    'Tweets': ['#saveOurChildren', '#Me_Too', '1 = BD should #remove_ict_act', '#SaveForests', '#FaceTheClimateEmergency', 'Just a simple #Break_Off']
})
print("Original Dataframe:")
print(dataframe)

def find_hashtag(text):
    hash_words = re.findall(r'(?<=#)\w+', text)
    return " ".join(hash_words)
dataframe['Hash_Words'] = dataframe['Tweets'].apply(lambda x: find_hashtag(x))
print("\nExtracting Hashtaged words:")
print(dataframe)