import global_vars, requests, json,
from AresNuker import Console

console = Console()
headers_account = global_vars.headers_account

def LeaveHypesquad() -> None:
	r = requests.delete('https://discord.com/api/v9/hypesquad/online', headers = headers_account)
	console.log('Left Hypesquad')

