import os, shutil

os.system('@echo off')
os.system('title Building Ares Nuker ^| by _0xfc')

os.system(r'pyinstaller --noconfirm --paths=../venv/Lib/site-packages --onedir --console --icon "../icon/icon.ico" --name "Ares Nuker" --upx-dir "./upx-4.0.2-win64"  "../main.py"')

archived = shutil.make_archive('./dist/Ares Nuker', 'zip', './dist/Ares Nuker')

if os.path.exists('./dist/Ares Nuker.zip'):
	print(archived)
	print(' > Done')
	input()
else: 
	print("ZIP file not created")