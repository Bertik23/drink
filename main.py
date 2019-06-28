import time
import ctypes  # An included library with Python install.
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
import winsound
#winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
languagesFile = open("language.txt","r")
l = languagesFile.readlines()
for line in l:
	#print(line)
	l[l.index(line)] = line[:-1]
	#print(line)
#print(l)
for i in range(len(l)-1):
	#print(l[i].split("|"))
	if l[i+1].split("|")[0] == l[0]:
		language = l[i+1].split("|")[0]
		mboxtitle = l[i+1].split("|")[1]
		mboxtext = l[i+1].split("|")[2]

def run():
	global timer
	winsound.PlaySound(f'sounds/{language}.wav', winsound.SND_FILENAME)
	Mbox(mboxtitle,mboxtext,0)
	winsound.PlaySound(f'sounds/{language}.wav', winsound.SND_FILENAME)


timer = 1_800#s	
while True:
	run()
	time.sleep(timer)