from pystyle import Colorate, Colors
from colorama import Fore, Back, Style
import datetime, os

class Console:

	def time(self) -> str:
		return f'{datetime.datetime.now():%H:%M:%S}'

	def ter_size(self) -> int:
		size = os.get_terminal_size()
		cols, lines = size
		return cols

	def log(self, content) -> None:
		print(f'[{Colorate.Horizontal(Colors.purple_to_red, self.time())}] [{Colors.purple}>>{Colors.white}] {content}')

	def info(self, content) -> None:
		cols = self.ter_size()
		print(f'[{Colorate.Horizontal(Colors.purple_to_red, self.time())}] [{Colors.purple}>>{Colors.white}] {content}{"":<{cols-43}} [{Back.BLUE}INFO{Style.RESET_ALL}{Colors.white}]')

	def warning(self, content) -> None:
		cols = self.ter_size()
		print(f'[{Colorate.Horizontal(Colors.purple_to_red, self.time())}] [{Colors.purple}>>{Colors.white}] {Fore.YELLOW+content+Colors.white}{"":<{cols-49}} [{Back.YELLOW}WARRNING{Style.RESET_ALL}{Colors.white}]')		

	def error(self, content):
		cols = self.ter_size()
		print(f'[{Colorate.Horizontal(Colors.purple_to_red, self.time())}] [{Colors.purple}>>{Colors.white}] {Fore.RED+content+Fore.WHITE:<{cols-48}} [{Back.RED}ERROR{Style.RESET_ALL}{Colors.white}]')