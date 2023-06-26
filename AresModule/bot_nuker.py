from AresCore.channels import CreateChannels, DeleteChannels
from AresCore.users import BanAll
from AresCore.roles import CreateRoles
from AresCore.requests_maker import StartRequestMaker
from threading import Thread

StartRequestMaker()


def Nuke() -> None:
	DeleteChannels()
	CreateChannels()
	CreateRoles()

