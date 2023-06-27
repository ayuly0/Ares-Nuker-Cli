from .get_all_guilds import _GetAllGuilds
from .channels import GetChannels
from AresNuker import Console
from rich.console import Console as Con
import global_vars, requests, json

con = Con()
console = Console()
headers = global_vars.headers

def GetBotId() -> int:
	r = requests.get('https://discord.com/api/v8/users/@me', headers = headers)
	id = int(json.loads(r.text)['id'])
	return id

def GetBotUsername() -> str:
	r = requests.get('https://discord.com/api/v8/users/@me', headers = headers)
	username = json.loads(r.text)['username']
	discriminator = json.loads(r.text)['discriminator']
	return f'{username}#{discriminator}'

def BotInvite() -> None:
	id = GetBotId()
	link = f"https://discord.com/api/oauth2/authorize?client_id={id}&permissions=8&scope=bot"
	console.info(f'[Bot Invite] {link}')
	input()

def CreateInvite() -> None:
	guilds = _GetAllGuilds()
	for guild in guilds:
		console.log(f'{guild["name"]} → {guild["id"]}')
	payload = {
		'max_age': 2592000,
		'max_uses': 100,
		'temporary': False,
		'unique': True
	}
	guild_id = con.input(' [white][[purple]~/bot-nuker/guild-id[white]] [purple]>[grey78] ')
	channels = GetChannels(guild_id)
	for channel in channels:
		console.log(f"{channel['name']} → {channel['id']}")
	channel_id = con.input(' [white][[purple]~/bot-nuker/guild-id/channel-id[white]] [purple]>[grey78] ')
	r = requests.post(f"https://discord.com/api/v8/channels/{channel_id}/invites", headers = headers, json = payload)
	code = json.loads(r.text)['code']
	console.info(f'[Invite Link] → https://discord.gg/{code}')
	input()
