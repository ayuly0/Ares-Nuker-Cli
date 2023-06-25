import config

config = config.LoadsConfig()

# ≫ ≪

## GLOBAL VARIBLE
headers = {'authorization': "Bot " + config['bot_token'], 'content-type': 'application/json'} if config['bot_token'] != 'None' else None
