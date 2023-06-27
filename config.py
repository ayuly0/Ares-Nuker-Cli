from configparser import ConfigParser
from AresNuker import Console
import os, json

console = Console()
config = ConfigParser()

config_file_exists = os.path.exists('config.ini')

config.read('config.ini')

def CreateConfig():
	console.error('config.ini not found')
	config.add_section('bot')
	config.set('bot', 'token', 'None')
	config.set('bot', 'version', '1')

	config.add_section('nuke')
	config.set('nuke', 'guild_name', 'Ares Nuker On Top')
	config.set('nuke', 'channel_name', 'Ares Nuker On Top')
	config.set('nuke', 'role_name', 'Ares Nuker')
	config.set('nuke', 'webhook_name', 'Ares Nuker')
	config.set('nuke', 'ban_reason', 'Ares Nuker On Top')
	config.set('nuke', 'get_admin', 'true')
	config.set('nuke', 'ban_all', 'true')
	config.set('nuke', 'amount_channel', '100')
	config.set('nuke', 'amount_role', '50')
	config.set('nuke', 'amount_message_per_channel', '50')

	config.add_section('message')
	config.set('message', 'content', 'Ares Nuker on top')
	config.add_section('message.embed')
	config.set('message.embed', 'title', 'Ezz Nuke')
	config.set('message.embed', 'description', 'AresNuker On Top')
	config.set('message.embed', 'icon_url', 'https://i.ibb.co/zrLHDJC/icon.png')
	config.set('message.embed', 'image_url', 'https://i.ibb.co/PG4zP2c/banner-ares.gif')
	config.set('message.embed', 'color', '1491362')

	config.add_section('discord')
	config.set('discord', 'user_id', '0')
	config.set('discord', 'guild_id', '0')
	config.set('discord', 'white_users_id', '[]')
	config.set('discord', 'white_guilds_id', '[]')

	config.add_section('account')
	config.set('account', 'token', 'None')
	config.set('account', 'last_message', 'Nuked')

	with open('config.ini', 'w') as configfile:
		config.write(configfile)
	console.info('Created config.ini, please config in config.ini file.')
	input()
	os._exit(0)

def LoadsConfig():
	CreateConfig() if not config_file_exists else None

	return config