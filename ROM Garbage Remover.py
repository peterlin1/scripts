from sys import *
from os import *
if len(argv)<3:
	argv=[1,2,3]
	argv[1]=raw_input('Enter source dir:')
	argv[2]=raw_input('Enter destination dir:')
if argv[1][-1] not in ['\\', '/']: argv[1]+='\\'
if argv[2][-1] not in ['\\', '/']: argv[2]+='\\'
fi=listdir(argv[1])
for qi in fi:
	if qi.strip(".gba")!=qi:
		f=file(argv[1]+qi,"rb")
		q=file(argv[2]+qi,"ab")
		x=16777214
		i=0
		while True:
			f.seek(x)
			a=f.read(1)
			if a not in ['\xff', '\x00']:
				x+=1
				break
			x-=1
		p=range(0, 100, 5)
		while i<x:
			f.seek(i)
			q.write(f.read(300))
			warble=int(100*i/x)
			if warble in p:
				print p.pop(0),"%..."
			i+=300
