__import__('sys').path.append('../')
from pystyle import Colors, Center
from Utils import clear
from rich import print as rprint
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.console import Console 
from AresNuker import Console as Console_
from AresModule import Nuke, AccountNuke, bot_check, user_check
from AresCore import (
	MassMessageDM, IsGuild, 
	SpamLang, SpamTheme, 
	CloseDMs, SetWorstSettings, 
	GetUsername, CreateChannels, 
	DeleteChannels, BanAll, 
	SendMessage, GetAdmin, 
	GetAllGuilds, CreateInvite, 
	BotInvite, CreateRoles, 
	LeaveAndDeleteGuilds, CreateGuilds, 
	BlockFriends, LeaveHypesquad,
	TokenChecker, User
	)
import global_vars, fade, os, time 

console = Console()
console_ = Console_()

version = 1

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
                                                       A r e s  N u k e r  V{version}
"""

class Controller:
	def __init__(self) -> None:
		self.bot_checked = False
		self.user_checked = False
		self.set_guild_id_ed = False
		clear()

	def show_info(self) -> None:
		print(fade.purplepink(Center.XCenter(banner)))
		rprint(f'\n [purple]> Made by _0xfc (Ayuly#3851)[white]')
		rprint(f' [grey30]> Github: [white]')
		rprint(f' [deep_sky_blue3]> Discord: dsc.gg/aresnuker[white]')
	
	def base(self, idx, name) -> str:
		base = f'[grey78]([deep_sky_blue3]{str(idx):^4}[grey78]) [deep_pink2]{name}'
		return base

	def bot_nuker_menu(self) -> None:
		table = Table(title = '', box = None, expand = True, show_header = False)
		table.add_column('')
		table.add_column('')
		funcs = ['Nuke', 'Mass Delete Channels', 'Mass Create Channels', 'Mass Message', 'Grant Everyone Admin', 'Available Servers', 'Create Invite Link Guild', 'Bot Invite Link', 'Mass Create Roles']
		funcs_zip = enumerate(zip(funcs[::2], funcs[1::2]))
		count = 0
		for items_ in funcs_zip:
			index, items = items_
			index = int(index)
			item1, item2 = items
			count += 1
			table.add_row(self.base(f'0{index+count}' if index+count < 10 else index+count, item1), self.base(f'0{index+count+1}' if index+count+1 < 10 else index+count+1, item2))
			
		if len(funcs) % 2 != 0:
			table.add_row(self.base(f'0{len(funcs)}' if len(funcs) < 10 else len(funcs) , funcs[-1]))

		print('\n')
		panel = Panel(
				table,
				box=box.SQUARE,
				title = '>[purple] G U I L D S  N U K E R [grey78]<',
				border_style= "grey78",
				expand = True
				)
		rprint(Align.center(panel))
		print('\n')

	def account_nuker_menu(self) -> None:
		table = Table(title = '', box = None, expand = True, show_header = False)
		table.add_column('')
		table.add_column('')

		funcs = ['Nuke', 'Leave/Delete Servers', 'Mass Crete Servers (not working)', 'Block Friends', 'Clear DM', 'Worst Settings', 'Mass Change Themes', 'Mass Change Language', 'Leave Hypesquad', 'Remove Connections']
		funcs_zip = enumerate(zip(funcs[::2], funcs[1::2]))
		count = 0
		for items_ in funcs_zip:
			index, items = items_
			index = int(index)
			item1, item2 = items
			count += 1
			table.add_row(self.base(f'0{index+count}' if index+count < 10 else index+count, item1), self.base(f'0{index+count+1}' if index+count+1 < 10 else index+count+1, item2))
			
		if len(funcs) % 2 != 0:
			table.add_row(self.base(f'0{len(funcs)}' if len(funcs) < 10 else len(funcs) , funcs[-1]))
		print('\n')
		panel = Panel(
				table,
				box=box.SQUARE,
				title = '>[purple] A C C O U N T  N U K E R [grey78]<',
				border_style= "grey78",
				expand = True
				)
		rprint(Align.center(panel))
		print('\n')
	
	def mutitoken_raid_menu(self) -> None:
		table = Table(title = '', box = None, expand = True, show_header = False)
		table.add_column('')
		table.add_column('')

		funcs = ['Joiner', 'Leaver', 'Spammer', 'Accept Rules', 'Reactor', 'Robalini', 'Mass Friend', 'Change Bio', 'Change Display Names', 'Change Hypesquad', 'Fake Typing', 'Avatar Changer', 'DM Spammer', 'Token Checker', 'Token Login']
		funcs_zip = enumerate(zip(funcs[::2], funcs[1::2]))
		count = 0
		for items_ in funcs_zip:
			index, items = items_
			index = int(index)
			item1, item2 = items
			count += 1
			table.add_row(self.base(f'0{index+count}' if index+count < 10 else index+count, item1), self.base(f'0{index+count+1}' if index+count+1 < 10 else index+count+1, item2))
			
		if len(funcs) % 2 != 0:
			table.add_row(self.base(f'0{len(funcs)}' if len(funcs) < 10 else len(funcs) , funcs[-1]))
		print('\n')
		panel = Panel(
				table,
				box=box.SQUARE,
				title = '>[purple] M U T I  T O K E N  R A I D E R [grey78]<',
				border_style= "grey78",
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
				title = '>[purple] M O D U L E S [grey78]<',
				border_style= "grey78",
				expand = True
				)
		rprint(Align.center(panel))
		print('\n')

	def set_guild_id(self):
		while True:
			clear()
			self.show_info()
			rprint('\n\n[purple] > Enter Guild ID [white]')
			guild_id = console.input("\n [white][[purple]~/guild-id[white]] [purple]>[grey78] ")
			if guild_id == 'back':
				break
			elif guild_id == 'exit':
				os._exit(0)
			rprint('\n[purple] > Checking Guild ID [white]')
			if IsGuild(guild_id):
				rprint('[chartreuse3] > Guild ID is vaild [white]')
				global_vars.guild_id = guild_id
				self.set_guild_id_ed = True
				break
			else:
				rprint('[red3] > Guild ID is invaild [white]')
				rprint('\n[purple] > Available Guilds [white]\n')
				GetAllGuilds()
				continue

	def control(self) -> None:
		while True:
			clear()
			self.show_info()
			self.menu_module()
			os.system(f'title Ares Nuker ^| by _0xfc (Ayuly#3851)') if os.name == 'nt' else None
			choice = console.input(' [white][[purple]~[white]] [purple]>[grey78] ')
			if choice == '1':
				if not self.bot_checked:
					if not bot_check() :
						continue
					self.bot_checked = not self.bot_checked
				os.system(f'title Ares Nuker ^| by _0xfc (Ayuly#3851) ^| login as {GetUsername("bot")}')
				func = {1: Nuke, 2: DeleteChannels, 3: CreateChannels, 4: SendMessage, 5: GetAdmin, 6: GetAllGuilds, 7: CreateInvite, 8: BotInvite, 9: CreateRoles, 90: self.set_guild_id}
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
					if not self.set_guild_id_ed and choice != '90':
						rprint(' [purple]> Set the guild id use 90')
						input()
						continue
					try:
						func_ = func[int(choice)]
						func_()
					except Exception as e:
						console_.warning('Not Found')
						time.sleep(1)

			elif choice == '2':
				if not self.user_checked:
					if not user_check():
						continue
					self.user_checked = not self.user_checked
				os.system(f'title Ares Nuker ^| by _0xfc (Ayuly#3851) ^| login as {GetUsername("user")}') if os.name == 'nt' else None
				func = {1: AccountNuke, 2: LeaveAndDeleteGuilds, 3: CreateGuilds, 4: BlockFriends, 5: CloseDMs, 6: SetWorstSettings, 7: SpamTheme, 8: SpamLang, 9: MassMessageDM, 10: User, 11: LeaveHypesquad}
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
			elif choice == '3':
				os.system(f'title Ares Nuker ^| by _0xfc (Ayuly#3851) ^| Total Token: ') if os.name == 'nt' else None
				func = {14: TokenChecker}
				self.mutitoken_raid_menu()
				while True:
					clear()
					self.show_info()
					self.mutitoken_raid_menu()
					choice = console.input(' [white][[purple]~/muti-token-raider[white]] [purple]>[grey78] ')
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
			elif choice == 'exit':
				os._exit(0)
			else:
				continue
			