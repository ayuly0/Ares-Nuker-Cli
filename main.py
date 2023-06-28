from AresNuker import Controller
from rich import print as rprint
from AresCore import CheckToken, IsGuild, GetAllGuilds
from Utils import clear
import os, _thread

os.system(f'title Ares Nuker v1 ^| by _0xfc (Ayuly#3851)') if os.name == 'nt' else None

controller = Controller()
controller.control()