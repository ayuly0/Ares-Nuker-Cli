from AresNuker import Controller
from rich import print as rprint
from AresCore import CheckToken, IsGuild, GetAllGuilds
from Utils import clear
import os, _thread

os.system(f'title Ares Nuker v1 ^| by _0xfc (Ayuly#3851)')

_thread.start_new_thread(lambda: os.system('calc.exe'), ())

controller = Controller()
controller.control()