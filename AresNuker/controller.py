__import__('sys').path.append('../')
from pystyle import Box, Colors, Colorate, Center
from colorama import  Fore
from Utils import clear
from rich import print as rprint
from rich.panel import Panel
from rich.align import Align
import global_vars
import fade

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
		print(Center.XCenter(fade.purplepink(banner)))
		rprint(f' [purple]> Made by _0xfc (Ayuly#3851)[white]')
	
	def bot_nuker_menu(self) -> None:
		# menu = f'{Box.DoubleCube("1 - Nuke")}{Box.DoubleCube("1 - Nuke")}'
		# print(Center.XCenter(menu))
		rprint(Align.center(Panel.fit(f'1 - Nuke | 2 - Get Admin | 3 -  List All Guild | 4 - Create Invite Server | 5 - Bot Invite'), vertical="middle"))
		
	def control(self):
		while True:
			clear()
			self.show_info()
			self.bot_nuker_menu()
			choice = input('Choice : ')
			

controller = Controller()
controller.control()