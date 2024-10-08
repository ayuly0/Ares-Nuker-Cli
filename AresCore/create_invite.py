__import__('sys').path.append('../')
from .get_all_guilds import _GetAllGuilds
from .channels import GetChannels
from AresNuker import Console
from rich.console import Console as Con
import global_vars, requests, json

con = Con()
console = Console()
headers = global_vars.headers
headers_account = global_vars.headers_account

def GetBotId() -> int:
	r = requests.get('https://discord.com/api/v8/users/@me', headers = headers)
	id = int(json.loads(r.text)['id'])
	return id

def GetUsername(type: str) -> str:
	if type == 'bot':
		r = requests.get('https://discord.com/api/v8/users/@me', headers = headers)
	elif type == 'user':
		r = requests.get('https://discord.com/api/v8/users/@me', headers = headers_account)
	username = json.loads(r.text)['username']
	discriminator = json.loads(r.text)['discriminator']
	return f'{username}#{discriminator}'

def BotInvite() -> None:
	id = GetBotId()
	link = f"https://discord.com/api/oauth2/authorize?client_id={id}&permissions=8&scope=bot"
	console.info(f'[Bot Invite] {link}')
	input()

def CreateInvite() -> None:
	payload = {
		'max_age': 2592000,
		'max_uses': 100,
		'temporary': False,
		'unique': True
	}
	channels = GetChannels(global_vars.guild_id)
	for channel in channels:
		console.log(f"{channel['name']} → {channel['id']}")
	channel_id = con.input(' [white][[purple]~/guilds-nuker/guild-id/channel-id[white]] [purple]>[grey78] ')
	r = requests.post(f"https://discord.com/api/v8/channels/{channel_id}/invites", headers = headers, json = payload)
	code = json.loads(r.text)['code']
	if code == '10003':
		console.error('Unknown Channel')
		input()
		return
	console.info(f'[Invite Link] → https://discord.gg/{code}')
	input()
