from AresNuker import Controller
from AresNuker.auth_system import auth_system
from rich.console import Console
import os

os.system(f'title Ares Nuker ^| by _0xfc (Ayuly#3851)') if os.name == 'nt' else None

console = Console()

key = console.input(" > Auth Key: ")
if auth_system(key):
	console.print('[green] > Auth Key is vaild')
	input()
	controller = Controller()
	controller.control()
else:
	console.print('[red1] > Auth Key is invaild')
	os._exit(0)