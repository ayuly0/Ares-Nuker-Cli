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
	config.set('bot', 'prefix', '!')
	config.set('bot', 'status', 'invisible')
	config.set('bot', 'version', '1')

	config.add_section('nuke')
	config.set('nuke', 'guild_name', 'Nuked')
	config.set('nuke', 'channel_name', 'Nuked')
	config.set('nuke', 'role_name', 'Nuked')
	config.set('nuke', 'webhook_name', 'Nuked')
	config.set('nuke', 'ban_reason', 'Nuked')
	config.set('nuke', 'get_admin', 'true')
	config.set('nuke', 'ban_all', 'true')
	config.set('nuke', 'amount_channel', '100')
	config.set('nuke', 'amount_role', '50')

	config.add_section('message')
	config.set('message', 'content', 'AresNuker on top\nEz Nuke')
	config.add_section('message.embed')
	config.set('message.embed', 'title', 'Ezz Nuke')
	config.set('message.embed', 'description', 'AresNuker On Top')
	config.set('message.embed', 'icon_url', '')
	config.set('message.embed', 'image_url', '')
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
	return

def LoadsConfig():
	CreateConfig() if not config_file_exists else None

	return config