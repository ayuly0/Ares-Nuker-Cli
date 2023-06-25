import requests, sys
sys.path.append('../')

import global_vars

def CheckToken() -> bool:
	if global_vars.headers == None:
		print('[≫] Please set the token bot.')
		return
	req = requests.get('https://discord.com/api/v9/users/@me', headers = global_vars.headers)
	if req.status_code == 200:
		return True
	elif req.status_code == 401:
		return False

def IsGuild() -> bool:
	req = requests.get(f"https://discord.com/api/v9/guilds/{global_vars.config['discord']['guild_id']}", headers = global_vars.headers)
	if req.status_code == 200:
		return True
	elif req.status_code == 404:
		return False

