from AresNuker import Controller
from rich import print as rprint
from AresCore import CheckToken, IsGuild
from Utils import clear
import global_vars, os

os.system('title Ares Nuker v1 ^| by _0xfc (Ayuly#3851)')

config = global_vars.config

clear()

rprint('[purple] > Checking Token Bot [white]')
if CheckToken():
	rprint('[chartreuse3] > Token bot is vaild [white]')
else:
	rprint('[red3] > Token bot is invaild [white]')
	os._exit(0)

rprint('[purple] > Checking ID Guild [white]')
if IsGuild():
	rprint('[chartreuse3] > ID Guild is vaild [white]')
else:
	rprint('[red3] > ID Guild is invaild [white]')
	os._exit(0)

controller = Controller()
controller.control()