__import__('sys').path.append('../')
from AresCore.channels import CreateChannels, DeleteChannels
from AresCore.users import BanAll
from AresCore.requests_maker import StartRequestMaker
from threading import Thread

StartRequestMaker()


def Nuke() -> None:
	DeleteChannels()
	CreateChannels()
	# delete_channels_thread = Thread(target=DeleteChannels,)
	# create_channels_thread = Thread(target=CreateChannels,)
	# ban_all_thread = Thread(target=BanAll)
	# delete_channels_thread.start()
	# delete_channels_thread.join()
	# create_channels_thread.start()
	# ban_all_thread.start()
	
