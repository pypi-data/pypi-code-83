# jbase

from ctypes import CDLL, byref, c_char_p, c_longlong, c_void_p, string_at
import numpy as np
import os
import subprocess

jt = 0


def init(basedir, uname):
 global libj, jt
 os.chdir(basedir)
 bindir = basedir + "/j"
 darwin = uname == "darwin"
 win32 = uname == "win32"
 jc = "/jconsole.exe" if win32 else "/jconsole"
 jl = "/j" if win32 else "/libj"
 ext = ".dll" if win32 else ".dylib" if darwin else ".so"
 avx = subprocess.check_output([bindir + jc,"-jprofile","avx.ijs"],
  cwd=bindir, encoding="utf8", text=True)
 if "avx2" in avx:
  jl += "avx2"
 elif "avx" in avx:
  jl += "avx"
 dll = bindir + jl + ext
 if jt != 0:
  raise AssertionError('init already run')
 libj = CDLL(dll)
 libj.JInit.restype = c_void_p
 libj.JGetR.restype = c_char_p
 jt = libj.JInit()
 if jt == 0:
  raise AssertionError('init library failed')


def call(cmd):
 req="res=: exec_server_ '" + cmd.replace("'","''") + "'"
 do(req)
 return get("res")


def close():
 global jt
 call('["maisvr",["close",""]]')
 jt = 0


def do(a):
 return libj.JDo(c_void_p(jt), tob(a))


def dor(a):
 libj.JDo(c_void_p(jt),tob(a))
 s= getr()[:-1]
 if 0!=len(s):
  print(s)


def get(n):
 dt = c_longlong(0)
 dr = c_longlong(0)
 ds = c_longlong(0)
 dd = c_longlong(0)
 libj.JGetM(c_void_p(jt), tob(n), byref(dt), byref(dr), byref(ds), byref(dd))
 t = dt.value
 if t == 0:
  raise AssertionError('get arg not a name')
 shape = np.fromstring(string_at(ds.value, dr.value*8), dtype=np.int64)
 count = np.prod(shape)
 if t == 2:
  r = (string_at(dd.value, count))
 elif t == 4:
  r = np.fromstring(string_at(dd.value, count*8), dtype=np.int64)
  r.shape = shape
 elif t == 8:
  r = np.fromstring(string_at(dd.value, count*8), dtype=np.float64)
  r.shape = shape
 else:
  raise AssertionError('get type not supported')
 return r


def getr():
 return string_at(libj.JGetR(c_void_p(jt))).decode('utf-8')


def tob(s):
 if type(s) is str:
  s = s.encode('utf-8')
 return s


def j():
 while 1:
  s = input('   ')
  if s == '....':
   break
  dor(s)
