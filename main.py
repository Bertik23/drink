import time
from pymsgbox import alert
from configparser import ConfigParser
from boombox import BoomBox

config = ConfigParser()
languages = ConfigParser()
config.read("config.ini")
languages.read("languages.ini")

def updateValues():
    global language, mboxtitle, mboxtext, sound, timer
    config.read("config.ini")
    languages.read("languages.ini")
    language = config.get("main","language")
    mboxtitle = languages.get(language,"title")
    mboxtext = languages.get(language,"text")
    sound = BoomBox(f"sounds/{language}.wav")
    timer = int(config.get("main","remindingInterval"))

def run():
    updateValues()
    sound.play()
    alert(title = mboxtitle, text = mboxtext, button = "OK")
    sound.play

while True:
    run()
    time.sleep(timer)
