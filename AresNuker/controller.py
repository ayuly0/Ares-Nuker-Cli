__import__('sys').path.append('../')
from pystyle import Colors, Center
from Utils import clear
from rich import print as rprint
from rich.align import Align
from rich.panel import Panel
from rich import box
from rich.table import Table
from rich.panel import Panel
from rich.console import Console 
from AresNuker import Console as Console_
from AresModule import Nuke, AccountNuke, bot_check, user_check
from AresCore import (SpamLang, SpamTheme, CloseDMs, SetWorstSettings, GetUsername, CreateChannels, DeleteChannels, BanAll, SendMessage, GetAdmin, GetAllGuilds, CreateInvite, BotInvite, CreateRoles, LeaveAndDeleteGuilds, CreateGuilds, BlockFriends)
import global_vars, fade, os, time, gratient 

console = Console()
console_ = Console_()

banner = f"""
 ▄▄▄       ██▀███  ▓█████   ██████     ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▒████▄    ▓██ ▒ ██▒▓█   ▀ ▒██    ▒     ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ░ ▓██▄      ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
 ▓█   ▓██▒░██▓ ▒██▒░▒████▒▒██████▒▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░   ▒     ░░   ░    ░   ░  ░  ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
      ░  ░   ░        ░  ░      ░              ░    ░     ░  ░      ░  ░   ░     
                                                       A r e s  N u k e r  V{global_vars.config['bot']['version']}
"""

class Controller:
	def __init__(self) -> None:
		self.bot_checked = False
		self.user_checked = False
		clear()

	def show_info(self) -> None:
		print(fade.purplepink(Center.XCenter(banner)))
		rprint(f'\n [purple]> Made by _0xfc (Ayuly#3851)[white]')
		rprint(f' [purple]> Github: [white]')
		rprint(f' [purple]> Discord: [white]')
	
	def base(self, idx, name) -> str:
		base = f'[[deep_sky_blue3]{str(idx):^4}[white]] [deep_pink2]{name}'
		return base

	def bot_nuker_menu(self) -> None:
		table = Table(title = '', box = None, expand = True, show_header = False, padding = (0, 3, 0, 3))
		table.add_column('')
		table.add_column('')
		# table.add_column('')

		table.add_row(self.base('01', 'Nuke'), self.base('02', 'Delete Channels'))
		table.add_row(self.base('03', 'Mass Create Channels'), self.base('04', 'Mass Message'))
		table.add_row(self.base('05', 'Grant Everyone Admin'), self.base('06', 'List All Guilds Have Bot'))
		table.add_row(self.base('07', 'Generator Invite Link Server'), self.base('08', 'Bot Invite Link'))
		table.add_row(self.base('09', 'Mass Create Roles'))

		# table.add_row(self.base('01', 'Nuke'), self.base('02', 'Delete Channels'), self.base('03', 'Mass Create Channels'))
		# table.add_row(self.base('04', 'Mass Message'), self.base('05', 'Grant Everyone Admin'), self.base('06', 'List All Guilds Have Bot'))
		# table.add_row(self.base('07', 'Generator Invite Link Server'), self.base('08', 'Bot Invite Link'), self.base('09', 'Mass Create Roles'))

		print('\n')
		panel = Panel(
				table,
				box=box.SQUARE,
				title = '>[purple] G U I L D S  N U K E R [white]<',
				border_style= "white",
				expand = True
				)
		rprint(Align.center(panel))
		print('\n')

	def account_nuker_menu(self) -> None:
		table = Table(title = '', box = None, expand = True, show_header = False, padding = (0, 3, 0, 3))
		table.add_column('')
		table.add_column('')
		table.add_column('')

		table.add_row(self.base('01', 'Nuke'), self.base('02', 'Leave/Delete Servers'), self.base('03', 'Mass Create Server (not working)'))
		table.add_row(self.base('04', 'Block Friends'), self.base('05', 'Clear DM'), self.base('06', 'Worst Settings'))
		table.add_row(self.base('07', 'Mass Change Theme'), self.base('08', 'Mass Change Language'), self.base('09', 'Mass Message DM'))
		table.add_row(self.base('10', 'User Info'), self.base('11', 'Leave HypeSquad'), self.base('12', 'Remove Connections'))
		print('\n')
		panel = Panel(
				table,
				box=box.SQUARE,
				title = '>[purple] A C C O U N T  N U K E R [white]<',
				border_style= "white",
				expand = True
				)
		rprint(Align.center(panel))
		print('\n')

	def menu_module(self) -> None:
		table = Table(title = '', box = None, expand = True, show_header = False, padding = (0, 3, 0, 3))
		table.add_column('')

		table.add_row(self.base('01', 'Guilds Nuker'))
		table.add_row(self.base('02', 'Account Nuker'))
		table.add_row(self.base('03', 'MutiToken Raider'))
		print('\n')
		panel = Panel(
				table,
				box=box.SQUARE,
				title = '>[purple] M O D U L E S [white]<',
				border_style= "white",
				expand = True
				)
		rprint(Align.center(panel))
		print('\n')

	def control(self) -> None:
		while True:
			clear()
			self.show_info()
			self.menu_module()
			os.system(f'title Ares Nuker v1 ^| by _0xfc (Ayuly#3851)') if os.name == 'nt' else None
			choice = console.input(' [white][[purple]~[white]] [purple]>[grey78] ')
			if choice == '1':
				if not self.bot_checked:
					bot_check()
					self.bot_checked = not self.bot_checked
				os.system(f'title Ares Nuker v1 ^| by _0xfc (Ayuly#3851) ^| login as {GetUsername("bot")}')
				func = {1: Nuke, 2: DeleteChannels, 3: CreateChannels, 4: SendMessage, 5: GetAdmin, 6: GetAllGuilds, 7: CreateInvite, 8: BotInvite, 9: CreateRoles}
				while True:
					clear()
					self.show_info()
					self.bot_nuker_menu()
					choice = console.input(' [white][[purple]~/guilds-nuker[white]] [purple]>[grey78] ')
					if choice == 'cls':
						clear()
						continue
					elif choice == 'back':
						break
					elif choice == 'exit':
						os._exit(0)
					try:
						func_ = func[int(choice)]
						func_()
					except Exception as e:
						console_.warning('Not Found')
						time.sleep(1)

			elif choice == '2':
				if not self.user_checked:
					user_check()
					self.user_checked = not self.user_checked
				os.system(f'title Ares Nuker v1 ^| by _0xfc (Ayuly#3851) ^| login as {GetUsername("user")}')
				func = {1: AccountNuke, 2: LeaveAndDeleteGuilds, 3: CreateGuilds, 4: BlockFriends, 5: CloseDMs, 6: SetWorstSettings, 7: SpamTheme, 8: SpamLang, 9: SpamLang}
				while True:
					clear()
					self.show_info()
					self.account_nuker_menu()
					choice = console.input(' [white][[purple]~/account-nuker[white]] [purple]>[grey78] ')
					if choice == 'cls':
						clear()
						continue
					elif choice == 'back':
						break
					elif choice == 'exit':
						os._exit(0)
					try:
						func_ = func[int(choice)]
						func_()
					except Exception as e:
						raise e
						# console_.warning('Not Found')
						# time.sleep(1)
			elif choice == 'exit':
				os._exit(0)
			else:
				continue
			