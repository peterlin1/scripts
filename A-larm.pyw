from time import localtime,sleep
from winsound import Beep

wakey=(20,05) #(hour, minute)

def tune():
	Beep(700,500)
	Beep(600,500)
	Beep(800,500)
	Beep(30000,100)
	Beep(800,500)
	Beep(600,500)
	Beep(700,500)
	
while localtime()[3:5]!=wakey:
	pass
for i in range(10):
	tune()
	sleep(20)
