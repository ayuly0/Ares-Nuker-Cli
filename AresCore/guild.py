__import__('sys').path.append('../')
import global_vars, requests, json
from AresNuker import Console

headers = global_vars.headers
config = global_vars.config
guild_id = global_vars.guild_id


def ChangeNameGuild():
	payload = {
		'name': config['nuke']['guild_name']
	}
	r = requests.patch(f"https://discord.com/api/v8/guilds/{guild_id}", headers = headers, data = json.dumps(payload))