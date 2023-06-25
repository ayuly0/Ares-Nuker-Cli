__import__('sys').path.append('../')
from .requests_maker import GetQ
import global_vars, requests, json
from AresNuker import Console

console = Console()
q = GetQ()

headers = global_vars.headers
config = global_vars.config
channel_name = config['nuke']['channel_name']
amount_channel = int(config['nuke']['amount_channel'])
guild_id = config['discord']['guild_id']

def CreateChannels() -> None:
	payload = {
		'type': 0,
		'name': channel_name,
		'permission_overwrites': []
	}

	for i in range(amount_channel):
		try:
			q.put((requests.post, f'https://discord.com/api/v8/guilds/{guild_id}/channels', headers, payload))
			console.log(f'Created channel {channel_name}')
		except:
			console.error(f'Unble to create channel {channel_name}')

def GetChannels(server_id):
	r = requests.get(f"https://discord.com/api/v8/guilds/{server_id}/channels", headers = headers)
	json_channels = json.loads(r.text)
	channels = []
	for i in range(0, len(json_channels)):
		id = json_channels[i]['id']
		name = json_channels[i]['name']
		channels.append({'id': id, 'name': name})
	return channels


def DeleteChannels() -> None:
	channels = GetChannels(guild_id)
	for channel in channels:
		try:
			q.put((requests.delete, f'https://discord.com/api/v8/channels/{channel["id"]}', headers, None))
			# r = requests.delete(f'https://discord.com/api/v8/channels/{channel["id"]}', headers = headers)
			# print(r)
			console.log(f'Deleted channel {channel["name"]}')
		except:
			console.error(f'Unble to delete channel {channel["name"]}')
