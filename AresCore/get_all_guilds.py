__import__('sys').path.append('../')
import global_vars, requests, json
from AresNuker import Console
import time

console = Console()
headers = global_vars.headers
headers_account = global_vars.headers_account

def _GetAllGuilds() -> list:
	r = requests.get('https://discord.com/api/v8/users/@me/guilds', headers = headers)
	guilds = json.loads(r.text)
	guilds_ = []
	for guild in guilds:
		guilds_.append({'name':guild['name'], 'id':guild['id']})
	return guilds_

def _GetAllGuildsUser():
	r = requests.get('https://discord.com/api/v8/users/@me/guilds', headers = headers_account)
	if r.status_code == 200:
		guilds = json.loads(r.text)
		guilds_ = []
		for guild in guilds:
			guilds_.append({'name':guild['name'], 'id':guild['id'], 'owner': True if guild['owner'] == 'true' else False})
		return guilds_
	elif r.status_code == 429:
		time.sleep(3)
		guilds = json.loads(r.text)
		guilds_ = []
		for guild in guilds:
			guilds_.append({'name':guild['name'], 'id':guild['id'], 'owner': True if guild['owner'] == 'true' else False})
		return guilds_
	else:
		return None

def GetAllGuilds() -> None:
	guilds = _GetAllGuilds()
	if guilds == None:
		console.error('Cant get Guilds')
		input()
		return

	for guild in guilds:
		console.info(f"{guild['name']} → {guild['id']}")
	input()