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
ex_a=None

bg=None
text=None
ss=None
_button_or_text=None

DESTROY='/exit'
JUMP='/continue'
MXN=125
# KEYS='qwertyuiop asdfghjkl;zxcvbnm'
KEYS='`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./ '
# KEYS+='~!@#$%^&*()_+QWERTYUIOP\{\}|ASDFGHJKL:"ZXCVBNM<>?'

def f_up():
	global ss

	if _js['s']!=ss:
		ss=_js['s']
		if _button_or_text:
			ex_a['text']=ss
		else:
			ex_a.delete('0.0',tk.END)
			ex_a.insert(tk.END,ss)

	for i in range(len(bts)):
		s='text'
		if text[i]!=_js[s][i]:
			bts[i][s]=_js[s][i]
			text[i]=_js[s][i]

		s='bg'
		if text[i]!=_js[s][i]:
			bts[i][s]=_js[s][i]
			text[i]=_js[s][i]

def f_press(i:int):
	a=_f(i)
	if a==DESTROY:
		t.destroy()
	elif a!=JUMP:
		f_up()

for i in range(MXN):
	od='def ff_'+str(i)+'():f_press('+str(i)+')'
	exec(od)

def f_key(event):
	c=str(event.char)
	if c not in KEYS:
		return
	f_press(c)

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
	button_or_text:bool=True,
)->None:

	global _js,_f,t,bts,bg,text,ss,ex_a,_button_or_text

	_js=js
	_f=f
	bg=dcp(js['bg'])
	text=[str(i) for i in js['text']]
	_button_or_text=button_or_text
	# ss=js['s']

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
	
	listen_k=tk.Label(t)
	listen_k.focus_set()
	listen_k.pack()
	listen_k.bind("<Key>",f_key)

	bts=list()
	fas=list()

	cm=tk.Frame(
		t,
		width=mx,
		height=my,
		bg=_js['bg_delta'],
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

	ex_fa=tk.Frame(
		t,
		width=mtx,
		height=mty,
		bg=_js['bg_exd'],
	)
	ex_fa.propagate(False)
	ex_fa.place(x=tx,y=ty)

	if 'ex_d' in js['tk']:
		ex_ffa=ex_fa
		ex_fa=tk.Frame(
			ex_ffa,
			width=js['tk']['ex_p'][0],
			height=js['tk']['ex_p'][1],
		)
		ex_fa.propagate(False)
		ex_fa.place(x=js['tk']['ex_d'][0],y=js['tk']['ex_d'][1])

	if button_or_text:
		ex_a=tk.Button(
			ex_fa,
			bg=_js['bg_exp'],
			activebackground=_js['bg_exp'],
			bd=0,
			font=('黑体',12,),
			wraplength=js['tk']['ex_p'][0],
			relief=tk.FLAT
		)
		# ex_a['state']=tk.DISABLED
	else:
		ex_a=tk.Text(
			ex_fa,
			bg=_js['bg_exp'],
			bd=1,
			font=('黑体',12,),
		)
		ex_a.insert(tk.INSERT,ss)
	ex_a.pack(expand=True,fill=tk.BOTH)
	# wraplength=30
	if hz:
		downs.throws(_up,1/hz)
	t.mainloop()
