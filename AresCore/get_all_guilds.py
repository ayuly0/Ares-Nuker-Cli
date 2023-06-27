import global_vars, requests, json
from AresNuker import Console

console = Console()
headers = global_vars.headers
headers_account = global_vars.headers_account
guild_id = global_vars.guild_id

def _GetAllGuilds() -> list:
	r = requests.get('https://discord.com/api/v8/users/@me/guilds', headers = headers)
	guilds = json.loads(r.text)
	guilds_ = []
	for guild in guilds:
		guilds_.append({'name':guild['name'], 'id':guild['id']})
	return guilds_

def _GetAllGuildsUser() -> list:
	r = requests.get('https://discord.com/api/v8/users/@me/guilds', headers = headers_account)
	guilds = json.loads(r.text)
	guilds_ = []
	for guild in guilds:
		guilds_.append({'name':guild['name'], 'id':guild['id']})
	return guilds_	

def GetAllGuilds() -> None:
	guilds = _GetAllGuilds()
	for guild in guilds:
		console.info(f"{guild['name']} → {guild['id']}")
	input()