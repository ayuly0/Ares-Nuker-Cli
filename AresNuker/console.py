from pystyle import Colorate, Colors
from colorama import Fore, Back, Style
import datetime

class Console:

	def time(self):
		return f'{datetime.datetime.now():%H:%M:%S}'

	def log(self, content):
		print(f'[{Colorate.Horizontal(Colors.purple_to_red, self.time())}] [{Colors.purple}>>{Colors.white}] {content}{"":<90}')

	def info(self, content):
		print(f'[{Colorate.Horizontal(Colors.purple_to_red, self.time())}] [{Colors.purple}>>{Colors.white}] {content}{"":<90} [{Back.BLUE}INFO{Style.RESET_ALL}{Colors.white}]')

	def error(self, content):
		print(f'[{Colorate.Horizontal(Colors.purple_to_red, self.time())}] [{Colors.purple}>>{Colors.white}] {Fore.RED+content+Fore.WHITE:<90} [{Back.RED}ERROR{Style.RESET_ALL}{Colors.white}]')
