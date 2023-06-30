__import__('sys').path.append('../')
from AresNuker import Console
from rich.console import Console as rConsole
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich import box
import global_vars, requests, json


console = Console()
rconsole = rConsole()

def base(info_type, info) -> str:
	return f' [grey78][[deep_sky_blue3]{info_type}[grey78]] [deep_pink2]{info}[grey78]'

def User() -> str:
	r = requests.get('https://discord.com/api/v9/users/@me', headers = global_vars.headers_account)
	data = json.loads(r.text)
	user_id = data['id']
	username = data['username']
	discriminator = data['discriminator']
	displayname = data['global_name']
	bio = data['bio'].replace('\n', '  ')
	locale = data['locale']
	nsfw_allowed = data['nsfw_allowed']
	mfa_enabled = data['mfa_enabled']
	premium_type = data['premium_type']
	email = data['email']
	phone = data['phone']
	verified = data['verified']

	table = Table(title = '', box = None, expand = True, show_header = False)
	table.add_column('')
	table.add_column('')

	table.add_row(base('User ID', user_id), base('Nsfw', nsfw_allowed))
	table.add_row(base('Username', username), base('2FA', mfa_enabled))
	table.add_row(base('Hashtag', '#'+discriminator), base('Premium Type', premium_type))
	table.add_row(base('DisplayName', displayname), base('Email', email))
	table.add_row(base('Bio', bio), base('Phone', phone))
	table.add_row(base('Locale', locale), base('Verified', verified))

	print('\n')
	panel = Panel(
			table,
			box=box.SQUARE,
			title = '>[purple] U S E R  I N F O [grey78]<',
			border_style= "grey78",
			expand = True
			)
	rconsole.print(Align.center(panel))
	print('\n')
	input()
	




"""
User
hashtag
user id
email
date creation

dm
friends
server
server owner
2fa
badges

"""