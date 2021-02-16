from twitch import TwitchClient
#client = TwitchClient('f0ilugz4jjhaheg2ioky2oe0wif8oo', '8y3pmm4jme26d3ap1ace51wf3uxjsi')

client = TwitchClient("f0ilugz4jjhaheg2ioky2oe0wif8oo")
ingests = client.ingests.get_server_list()

games = client.games.get_top()
print(games)