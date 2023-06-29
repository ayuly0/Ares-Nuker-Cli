import requests, sys
sys.path.append('../')
from AresNuker import Console
import global_vars

console = Console()

def CheckToken(token, type) -> bool:
	if global_vars.headers == None:
		console.log('Please set the token bot.')
		return
	headers = {'authorization':"Bot " + token if type == 'bot' else '' + token, 'content-type': 'application/json'}
	req = requests.get('https://discord.com/api/v9/users/@me', headers = headers)
	if req.status_code == 200:
		return True
	elif req.status_code == 401:
		return False

def IsGuild(id) -> bool:
	req = requests.get(f"https://discord.com/api/v9/guilds/{id}", headers = global_vars.headers)
	if req.status_code == 200:
		return True
	elif req.status_code == 404:
		return False

