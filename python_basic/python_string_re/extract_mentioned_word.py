# Write a Pandas program to extract word mention someone in tweets using @ from the specified column 
# of a given DataFrame.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
dataframe = pd.DataFrame({
    'Tweets': ['@saveOurChildren', '@Me_Too', '1 = BD should ?remove_ict_act', '@SaveForests', '<FaceTheClimateEmergency', 'Just a simple =Break_Off']
})
print("Original Dataframe:")
print(dataframe)

def find_mentions(text):
    mentioned_word = re.findall(r'(?<=@)\w+', text)
    return " ".join(mentioned_word)

dataframe['Mentioned_Words'] = dataframe['Tweets'].apply(lambda x: find_mentions(x))
print("\nExtracting Mentioned Words:")
print(dataframe)