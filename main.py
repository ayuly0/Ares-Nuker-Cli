from AresNuker import Controller, Console
from AresCore import CheckToken, IsGuild
from Utils import clear
import global_vars, os, time

config = global_vars.config
console = Console()

clear()

console.info('Checking Token Bot')
time.sleep(1)
if CheckToken():
	console.info('Token bot is vaild')
	time.sleep(1)
else:
	console.warning('Token bot is invaild')
	time.sleep(1)
	os._exit(0)

console.info('Checking ID Guild')
time.sleep(1)
if IsGuild():
	console.info('ID Guild is vaild')
	time.sleep(1)
else:
	console.warning('ID Guild is invaild')
	time.sleep(1)
	os._exit(0)

controller = Controller()
controller.control()