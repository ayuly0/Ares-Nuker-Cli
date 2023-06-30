__import__('sys').path.append('../')
import os
from Utils import clear
from .is_vaild import CheckToken
from AresNuker import Console
from rich.console import Console as rConsole

rconsole = rConsole()
console = Console()


def TokenChecker():
	rconsole.print('[purple] > Type - [ [1] 1 Token - [2] File Token ]')
	type = rconsole.input(' [white][[purple]~/check-type[white]] [purple]>[grey78] ')
	if type == '1':
		token = rconsole.input(' [white][[purple]~/check-type/token[white]] [purple]>[grey78] ')
		if CheckToken(token, 'account'):
			console.log(f'Token is vaild: {token}')
		else:
			console.log(f'Token is invaild: {token}')

	elif type == '2':
		file = rconsole.input(' [white][[purple]~/check-type/file[white]] [purple]>[grey78] ')
		tokens = []
		vaild_tokens = []
		invaild_tokens = []
		with open(file, 'r') as f:
			tokens = f.readlines()
		for index, token in enumerate(tokens):
			os.system(f'title Ares Nuker ^| by _0xfc (Ayuly#3851) ^| Token Check: Vaild {len(vaild_tokens)} - Invaild {len(invaild_tokens)}')
			token = token.strip()
			if CheckToken(token, 'account'):
				vaild_tokens.append(token)
				with open('../live_token.txt', 'a+') as f:
					f.write(f'{token}\n')
				clear()
				rconsole.print(f'[green] > [{index+1}/{len(tokens)}] Token is vaild >> {token}')
			else:
				clear()
				rconsole.print(f'[red1] > [{index+1}/{len(tokens)}] Token is invaild >> {token}')
				invaild_tokens.append(token)
