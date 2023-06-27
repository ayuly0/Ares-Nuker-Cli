__import__('sys').path.append('../')
from pystyle import Colors, Center
from Utils import clear
from rich import print as rprint
from rich.align import Align
from rich.console import Console 
from AresNuker import Console as Console_
from AresModule import Nuke, AccountNuke
from AresCore import (CreateChannels, DeleteChannels, BanAll, SendMessage, GetAdmin, GetAllGuilds, CreateInvite, BotInvite, CreateRoles, LeaveGuilds, CreateGuilds, BlockFriends, DeleteGuilds)
import global_vars, fade, os, time

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
		self.module_type = ''
		clear()

	def show_info(self) -> None:
		print(fade.purplepink(Center.XCenter(banner)))
		rprint(f'\n [purple]> Made by _0xfc (Ayuly#3851)[white]')
		rprint(f' [deep_pink2]> Bot Nuker (done)[white]')
		rprint(f' [red1]> Account Nuker (soon)[white]')
	
	def bot_nuker_menu(self) -> None:
		menu = """
┌─────────────────────────┬────────────────────────┐
│   [grey78][[purple]1[grey78]] [deep_pink2]Nuke[grey78]              │   [grey78][[purple]5[grey78]] [deep_pink2]Get Admin[grey78]        │
│   [grey78][[purple]2[grey78]] [deep_pink2]Delete Channels[grey78]   │   [grey78][[purple]6[grey78]] [deep_pink2]Get All Guild[grey78]    │
│   [grey78][[purple]3[grey78]] [deep_pink2]Create Channels[grey78]   │   [grey78][[purple]7[grey78]] [deep_pink2]Invite Guild[grey78]     │
│   [grey78][[purple]4[grey78]] [deep_pink2]Spam Message[grey78]      │   [grey78][[purple]8[grey78]] [deep_pink2]Bot Invite[grey78]       │
└─────────────────────────┴────────────────────────┘
		"""
		rprint(Align.center(menu))

	def account_nuker_menu(self) -> None:
		menu = """
┌───────────────────┐
│ [grey78][[purple]1[grey78]] [deep_pink2]Nuke          [grey78]│
│ [grey78][[purple]2[grey78]] [deep_pink2]Leave Guild   [grey78]│
│ [grey78][[purple]3[grey78]] [deep_pink2]Spam Guild    [grey78]│
│ [grey78][[purple]4[grey78]] [deep_pink2]Block Friends [grey78]│
│ [grey78][[purple]5[grey78]] [deep_pink2]Remove DM     [grey78]│
│ [grey78][[purple]6[grey78]] [deep_pink2]Delete Server [grey78]│
└───────────────────┘
		"""
		rprint(Align.center(menu, vertical="middle"))

	def control(self) -> None:
		while True:
			clear()
			self.show_info()
			menu = """
┌────────────────────┐
│ [white][[purple]1[white]] [grey78]Bot Nuker      │
│ [[purple]2[white]][grey78] Account Nuker  │
└────────────────────┘
			"""
			rprint(Align.center(menu, vertical="middle"))
			choice = console.input(' [white][[purple]~[white]] [purple]>[grey78] ')
			if choice == '1':
				func = {1: Nuke, 2: DeleteChannels, 3: CreateChannels, 4: SendMessage, 5: GetAdmin, 6: GetAllGuilds, 7: CreateInvite, 8: BotInvite, 9: CreateRoles}
				while True:
					clear()
					self.show_info()
					self.bot_nuker_menu()
					choice = console.input(' [white][[purple]~/bot-nuker[white]] [purple]>[grey78] ')
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
				func = {1: AccountNuke, 2: LeaveGuilds, 3: CreateGuilds, 4: BlockFriends, 6: DeleteGuilds}
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
			