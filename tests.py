# from dankware import fade

# banner = f"""
#  ▄▄▄       ██▀███  ▓█████   ██████     ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
# ▒████▄    ▓██ ▒ ██▒▓█   ▀ ▒██    ▒     ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
# ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ░ ▓██▄      ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
# ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
#  ▓█   ▓██▒░██▓ ▒██▒░▒████▒▒██████▒▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
#  ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
#   ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
#   ░   ▒     ░░   ░    ░   ░  ░  ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
#       ░  ░   ░        ░  ░      ░              ░    ░     ░  ░      ░  ░   ░     
#                                                        A r e s  N u k e r  V1
# """

# menu = """
# ┌─────────────────────────┬────────────────────────┐
# │   [1] Nuke              │   [5] Get Admin        │
# │   [2] Delete Channels   │   [6] Get All Guild    │
# │   [3] Create Channels   │   [7] Invite Guild     │
# │   [4] Spam Message      │   [8] Bot Invite       │
# └─────────────────────────┴────────────────────────┘
# 		"""



# print(fade('[>>] this is the long text i dont know wtf to say', 'purple'))

# from rich import print
# from rich.panel import Panel
# print(Panel("Hello, [red]World!", title="[red]> Welcome <"))

from rich.panel import Panel
from rich import box
from rich.table import Table
from rich.panel import Panel
from rich import print
from rich.align import Align

table = Table(show_header=True, expand=False, box=box.HEAVY, collapse_padding = True, padding = (0, 0))
table.add_column('> Account Nuker')
table.add_column('> Guilds Nuker')
table.add_column('> MutiToken Raider')

account_nuker = Table(show_header=False, expand=True, show_edge=False, box=box.HEAVY)
account_nuker.add_column('index')
account_nuker.add_column('func')

account_nuker.add_row('1', 'Nuke')
account_nuker.add_row('2', 'Leave/Delete Guilds')
account_nuker.add_row('3', 'Block Frineds')
account_nuker.add_row('4', 'Mass DM')

server_nuker = Table(show_header=False, expand=True, show_edge=False, box=box.HEAVY)
server_nuker.add_column('index')
server_nuker.add_column('index')

p1 = Table(show_header=False, expand=True, show_edge=False, box=box.HEAVY)
p2 = Table(show_header=False, expand=True, show_edge=False, box=box.HEAVY)

p1.add_column('index')
p1.add_column('func')
p2.add_column('index')
p2.add_column('func')

p1.add_row('6', 'Killl')
p2.add_row('8', 'Die')

server_nuker.add_row(p1, p2)

table.add_row(account_nuker, server_nuker)


print(table)

# table = Table(title = '', box = None, expand = True, show_header = False, padding = (0, 3, 0, 3))
# table.add_column('')
# table.add_column('')
# table.add_column('')

# table.add_row('[[deep_sky_blue3]1[white]] [deep_pink2]Delete Channels', '[[deep_sky_blue3]2[white]] [deep_pink2]Delete Channels', '[[deep_sky_blue3]3[white]] [deep_pink2]Delete Channels')
# table.add_row('[[deep_sky_blue3]4[white]] [deep_pink2]Delete Channels', '[[deep_sky_blue3]5[white]] [deep_pink2]Delete Channels', '[[deep_sky_blue3]6[white]] [deep_pink2]Delete Channels')
# table.add_row('[[deep_sky_blue3]7[white]] [deep_pink2]Delete Channels', '[[deep_sky_blue3]8[white]] [deep_pink2]Delete Channels')

# panel = Panel(
# 		table,
# 		box=box.SQUARE,
# 		title = '>[purple] A R E S  N U K E R [white]<',
# 		border_style= "white",
# 		expand = True
# 		)
# print(Align.center(panel))
# input()