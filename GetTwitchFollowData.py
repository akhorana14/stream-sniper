from twitch import TwitchClient

client = TwitchClient('f0ilugz4jjhaheg2ioky2oe0wif8oo')
users = client.users.translate_usernames_to_ids(['xsmart'])

for user in users:
     follows = client.users.get_follows(user_id=user.id, limit=100, offset=0)
     print(follows)
