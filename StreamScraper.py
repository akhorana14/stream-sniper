
from twitch import TwitchClient
import sys, requests,json
from twitch.constants import DIRECTIONS, DIRECTION_DESC, USERS_SORT_BY, USERS_SORT_BY_CREATED_AT
import Credentials as cr
import numpy as np
import pandas as pd
from random import random
from random import randrange

'''
A quick script written to get a similar Twitch streamer 
using a Twitch streamer's username.

Jacob Zietek, Bryan Yakimisky
'''





df = pd.read_csv('./Dec12Edges.csv')
client = TwitchClient(cr.client_id)

def getRecommendations(input_username):
    # Gathers all rows streamer is in from the dataframe
    streamer_rows = df['Target'].loc[lambda x: x==input_username].index
    streamer_rows.append(df['Source'].loc[lambda x: x==input_username].index)

    # Gets index of the highest rated streamer in the category
    highest_rated_in_category_index = df['Weight'][streamer_rows].nlargest()

    recommendations = []
    # Gets Top 5 Recommendations
    for i in range(5):
        highest_rated_in_category = df['Target'][highest_rated_in_category_index.index[i]]
        if(highest_rated_in_category==input_username):
            highest_rated_in_category = df['Source'][highest_rated_in_category_index.index[i]]
        recommendations.append(highest_rated_in_category)

    return recommendations





def getInfoFromAccount(username):
    
    streamer_dict = dict()
    streamer_dict

    user = client.users.translate_usernames_to_ids([username])[0]
    follows = client.users.get_follows(user_id=user.id, limit=100, offset=0)
    for streamers in follows:
        try:
            recs = getRecommendations(streamers.channel.name)
            for rec in recs:
                if not rec in streamer_dict:
                    streamer_dict[rec] = 1
                else:
                    streamer_dict[rec] +=1
        except IndexError:
            continue

    for streamers in follows:
        if streamers.channel.name in streamer_dict:
            del streamer_dict[streamers.channel.name]

    
    return getList(streamer_dict)

def getList(streamer_dict): 
    streamer_dict = sorted(streamer_dict.items(), key = 
        lambda kv:(kv[1], kv[0]),reverse = True)


    l = []
    for i in range(5):
        l.append(streamer_dict[i][0])

    streamers = []
    users = client.users.translate_usernames_to_ids(l)
    for streamer in users:
        channel = client.channels.get_by_id(streamer.id)
        streamers.append([channel.name,channel.logo,channel.url])


    return streamers
      
def randomStreamer():
    Headers = {'Client-ID': 'gp762nuuoqcoxypju8c569th9wz7q5', 'Authorization': "Bearer " + '8y3pmm4jme26d3ap1ace51wf3uxjsi'}
    r = requests.get('https://api.twitch.tv/helix/streams?first=' + str(100), headers=Headers)
    raw = r.text.encode('utf-8')
    j = json.loads(raw)
    sys.stdout.flush()
    dict = {}
    streamers = [element['user_name'] for element in j['data']]

    i = int(random() * 50)
    streamer_dict =  {streamers[i] : 1, streamers[i+10] : 1, streamers[i+20] : 1, streamers[i+30] : 1, streamers[i+40] : 1}

    return getList(streamer_dict)

    

if __name__ == '__main__':
    print(getInfoFromAccount('SpecialSnowflack'))