import time
import ctypes  # An included library with Python install.
from configparser import ConfigParser
import winsound #winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

config = ConfigParser()
languages = ConfigParser()
config.read("config.ini")
languages.read("languages.ini")

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    ##  Styles:
    ##  0 : OK
    ##  1 : OK | Cancel
    ##  2 : Abort | Retry | Ignore
    ##  3 : Yes | No | Cancel
    ##  4 : Yes | No
    ##  5 : Retry | No
    ##  6 : Cancel | Try Again | Continue

def updateLanguage():
    config.read("config.ini")
    languages.read("languages.ini")
    language = config.get("main","language")
    mboxtitle = languages.get("language","title")
    mboxtext = language.get("language","text")

def run():
	global timer
	winsound.PlaySound(f'sounds/{language}.wav', winsound.SND_FILENAME)
	Mbox(mboxtitle,mboxtext,0)
	winsound.PlaySound(f'sounds/{language}.wav', winsound.SND_FILENAME)
updateLanguage()
print(language,mboxtext,mboxtitle)
timer = 1_800#s
while True == False:
	run()
	time.sleep(timer)
