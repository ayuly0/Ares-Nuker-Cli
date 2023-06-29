__import__('sys').path.append('../')
import global_vars, requests, json, os
from AresNuker import Console
from rich.console import Console as rConsole
from rich import print as rprint
from .requests_maker import GetQ

rconsole = rConsole()
console = Console()
q = GetQ()
headers_account = global_vars.headers_account

def GetAllDMs():
	r = requests.get(f'https://discord.com/api/v8/users/@me/channels', headers = headers_account)
	if r.status_code == 200:
		dms = json.loads(r.text)
		dms_list = []
		for dm in dms:
			dms_list.append({'user_id':dm['recipients'][0]['id'], 'name': dm['recipients'][0]['global_name'], 'id': dm['id']})
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

def MassMessageDM() -> None:
	dms = GetAllDMs()
	if dms == None:
		console.error('Cant get DMs channel')
		input()
		return


	content = ""
	amount = 0

	while True:
		rprint('\n\n[purple] > Enter Message [white]')
		content = rconsole.input("\n [white][[purple]~/mass-message-dm/message[white]] [purple]>[grey78] ")
		if content == 'back':
			break
		elif content == 'exit':
			os._exit(0)
		rprint('\n\n[purple] > Enter Amount [white]')
		amount = int(rconsole.input("\n [white][[purple]~/mass-message-dm/amount[white]] [purple]>[grey78] "))
		break

	for i in range(amount):
		for dm in dms:
			id = dm['id']
			name = dm['name']
			user_id = dm['user_id']
			payload = {
				'content': f"<@{user_id}> " + content
			}
			try:
				q.put((requests.post, f'https://discord.com/api/v9/channels/{id}/messages', headers_account, payload))
				# r = requests.post(f'https://discord.com/api/v9/channels/{id}/messages', headers = headers_account, json = payload)
				console.log(f'[{i}/{amount}] Message to DM {name}')
				# console.debug(r.text)
				# input()
			except:
				console.error(f'[{i}/{amount}] Unble to message to DM {name}')
