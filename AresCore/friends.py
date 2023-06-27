import global_vars, requests, json
from AresNuker import Console

console = Console()
headers = global_vars.headers


def GetFriends() -> list:
	r = requests.get('https://discord.com/api/v8/users/@me/relationships', headers = headers)
	friends = json.loads(r.text)
	friend_list = []
	for friend in friends:
		user = friend['user']
		id = user['id']
		username = user['username']
		discriminator = user['discriminator']
		friend_list.append({'id':id, 'username':f'{username}#{discriminator}'})
	return friend_list

def BlockFriends() -> None:
	pass