import os
import time
import downs
from copy import deepcopy as dcp
import tkinter as tk

_d_lrud={
	'left':[
		0,'0',False,'l','left','L','LEFT','Left',
	],
	'right':[
		1,'1',True,'r','right','R','RIGHT','Right',
	],
	'up':[
		2,'2','u','up','U','UP','Up',
	],
	'down':[
		3,'3','d','down','D','DOWN','Down',
	]
}

_js=None
_f=None

t=None
bts=None
ssa=None

bg=None
text=None
ss=None

DESTROY='/exit'
JUMP='/continue'

def f_press(i:int):
	a=_f(i)
	if a==DESTROY:
		t.destroy()
	elif a!=JUMP:
		f_up()

MXN=10000
for i in range(MXN):
	od='def ff_'+str(i)+'():f_press('+str(i)+')'
	exec(od)

def f_up():
	global ss

	if _js['s']!=ss:
		ss=_js['s']
		ssa.delete('0.0',tk.END)
		ssa.insert(tk.END,ss)

	for i in range(len(bts)):
		s='text'
		if text[i]!=_js[s][i]:
			bts[i][s]=_js[s][i]
			text[i]=_js[s][i]

		s='bg'
		if text[i]!=_js[s][i]:
			bts[i][s]=_js[s][i]
			text[i]=_js[s][i]


def _up(d:float):
	while True:
		f_up()
		time.sleep(d)

PTH=os.path.abspath(os.path.dirname(__file__))+'/1.ico'

def mtgui(
	js:dict,
	f,
	ico:str=PTH,
	hz:int=10,
)->None:

	global _js,_f,t,bts,bg,text,ss,ssa

	_js=js
	_f=f
	bg=dcp(js['bg'])
	text=[str(i) for i in js['text']]
	ss=js['s']

	nx,ny=_js['tk']['n']
	px,py=_js['tk']['buttom']
	dx,dy=_js['tk']['delta']
	exy,lrud=_js['tk']['w']
	mx,my=nx*(px+dx)+dx,ny*(py+dy)+dy

	if lrud in _d_lrud['left']:
		cx,cy=exy,0
		tx,ty=0,0
		mtx,mty=exy,my
		dpix,dpiy=mx+exy,my
	elif lrud in _d_lrud['right']:
		cx,cy=0,0
		tx,ty=mx,0
		mtx,mty=exy,my
		dpix,dpiy=mx+exy,my
	elif lrud in _d_lrud['up']:
		cx,cy=0,exy
		tx,ty=0,0
		mtx,mty=mx,exy
		dpix,dpiy=mx,my+exy
	elif lrud in _d_lrud['down']:
		cx,cy=0,0
		tx,ty=0,my
		dpix,dpiy=mx,my+exy
		mtx,mty=mx,exy
	else:
		raise TypeError

	del t
	t=tk.Tk()
	t.geometry(str(dpix)+'x'+str(dpiy)+'+0+0')
	t.title(_js['tk']['/nick'])
	try:
		t.iconbitmap(ico)
	except:
		None
	
	bts=list()
	fas=list()

	cm=tk.Frame(
		t,
		width=mx,
		height=my,
		bg='#ff0000',
	)
	cm.place(x=cx,y=cy)

	for j in range(ny):
		yy=dy+j*(py+dy)
		for i in range(nx):
			xx=dx+i*(px+dx)

			fa=tk.Frame(
				cm,
				width=px,
				height=py,
				bg='#ff00ff',
			)
			fas.append(fa)
			fa.propagate(False)
			fa.place(x=xx,y=yy)

			k=len(bts)
			a=tk.Button(
				fa,
				command=eval('ff_'+str(k)),
				bg=bg[k],
				text=text[k],
				font=('黑体',16,),
				bd=0,
			)
			bts.append(a)
			a.pack(expand=True,fill=tk.BOTH)

	fa=tk.Frame(
		t,
		width=mtx,
		height=mty,
		bg='#ffff00',
	)
	fa.propagate(False)
	fa.place(x=tx,y=ty)

	ssa=tk.Text(
		fa,
		bg='#ffffff',
		bd=1,
		font=('黑体',12,),
	)
	ssa.insert(tk.INSERT,ss)
	ssa.pack(expand=True,fill=tk.BOTH)
	
	if hz:
		downs.throws(_up,1/hz)
	t.mainloop()
