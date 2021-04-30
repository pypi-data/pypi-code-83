import ctypes

drg = ctypes.cdll.LoadLibrary("./libdragon")

def eval(val):
	evall = drg.eval
	evall(str.encode(val))
	
def getInt(val):
	getI = drg.getInt
	return getI(str.encode(val))
	
def getFloat(val):
	getF = drg.getFloat
	getF.restype = ctypes.c_float
	return getF(str.encode(val))
	
def getDouble(val):
	getD = drg.getDouble
	getD.restype = ctype.c_double
	return getD(str.encode(val))

def getString(val):
	getS = drg.getString
	getS.restype = ctypes.c_char_p
	s = getS(val)
	return s.decode()

def setVariable(val,val2):
	getS = drg.setVariable
	getS(str.encode(val),str.encode(val2))
	
def select(val):
	sel = drg.eval
	sel(str.encode("select \""+val+"\""))
	
def show(val):
	sh = drg.eval
	sh(str.encode("show "+val))
	
def showln(val):
	shl = drg.eval
	shl(str.encode("showln "+val))
	
