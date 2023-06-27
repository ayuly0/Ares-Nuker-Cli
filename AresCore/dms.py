__import__('sys').path.append('../')
import global_vars, requests, json
from AresNuker import Console
from .requests_maker import GetQ

console = Console()
q = GetQ()
headers_account = global_vars.headers_account

def GetAllDMs():
	r = requests.get(f'https://discord.com/api/v8/users/@me/channels', headers = headers_account)
	if r.status_code == 200:
		dms = json.loads(r.text)
		dms_list = []
		for dm in dms:
			dms_list.append({'name': dm['recipients'][0]['global_name'], 'id': dm['id']})
		return dms_list
	else:
		return None

def CloseDMs() -> None:
	dms = GetAllDMs()
	if dms == None:
		console.error('Cant get DMs channel')
		input()
		return
	for dm in dms:
		id = dm['id']
		name = dm['name']
		try:
			q.put((requests.delete, f"https://discord.com/api/v8/channels/{id}", headers_account, None))
			console.log(f'Closed DM → {name}')
		except:
			console.error(f'Unble to close DM → {name}')
