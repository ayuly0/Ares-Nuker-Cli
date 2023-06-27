from AresCore import BlockFriend, LeaveGuilds, CreateGuilds


def Nuke() -> None:
	LeaveGuilds()
	CreateGuilds()
	BlockFriend()