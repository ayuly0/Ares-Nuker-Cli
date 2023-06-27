import config

config = config.LoadsConfig()

# ≫ ≪

## GLOBAL VARIBLE
headers = {'authorization': "Bot " + config['bot']['token'], 'content-type': 'application/json'} if config['bot']['token'] != 'None' else None
guild_id = config['discord']['guild_id']