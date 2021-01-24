'''
A quick script written to get a similar Twitch streamer 
using a Twitch streamer's username.

Jacob Zietek, Bryan Yakimisky
'''

import numpy as np
import pandas as pd
from random import random
from random import randrange

df = pd.read_csv('./Dec12Edges.csv')
    
input_username = "Nivfnja"

# Gathers all rows streamer is in from the dataframe
streamer_rows = df['Target'].loc[lambda x: x==input_username].index
streamer_rows.append(df['Source'].loc[lambda x: x==input_username].index)

# Gets index of the highest rated streamer in the category
highest_rated_in_category_index = df['Weight'][streamer_rows].nlargest()


# Gets Top 5 Recommendations
for i in range(5):
    highest_rated_in_category = df['Target'][highest_rated_in_category_index.index[i]]
    if(highest_rated_in_category==input_username):
        highest_rated_in_category = df['Source'][highest_rated_in_category_index.index[i]]
    print(highest_rated_in_category)