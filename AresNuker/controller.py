__import__('sys').path.append('../')
from pystyle import Box, Colors, Colorate, Center
from colorama import  Fore
from Utils import clear
from rich import print as rprint
from rich.panel import Panel
from rich.align import Align
from rich.console import Console 
from AresModule import Nuke
import global_vars, fade, os

console = Console()

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
	
	def bot_nuker_menu(self) -> None:
		rprint(Align.center(Panel.fit(f'[1] Nuke | [2] Delete Channels | [3] Create Channels | [4] Spam Webhooks'), vertical="middle"))
		rprint(Align.center(Panel.fit(f'[5] Get Admin | [6] List All Guild | [7] Create Invite Server | [8] Bot Invite'), vertical="middle"))
		
	def account_nuker_menu(self) -> None:
		rprint(Align.center(Panel.fit(f'1 - Nuke'), vertical="middle"))


	def control(self) -> None:
		while True:
			clear()
			self.show_info()
			rprint(Align.center(Panel.fit(f'[1] BotNuker | [2] AccountNuker'), vertical="middle"))
			choice = console.input(' [[purple]~[white]] : ')
			if choice == '1':
				while True:
					clear()
					self.show_info()
					self.bot_nuker_menu()
					choice = console.input(' [[purple]~[white]] : ')
					if choice == '1':
						Nuke()
					elif choice == 'cls':
						clear()
					elif choice == 'exit':
						os._exit(0)
			elif choice == '2':
				while True:
					clear()
					self.show_info()
					self.account_nuker_menu()
					choice = console.input(' [[purple]~[white]] : ')
			elif choice == 'exit':
				os._exit(0)
			else:
				continue
			