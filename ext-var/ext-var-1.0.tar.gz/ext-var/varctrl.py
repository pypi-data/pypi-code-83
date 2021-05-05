#-----External Variables (extvar)
import os

def mkpth():
    os.system("mkdir ExtVars")
def getv(varname):
    var = open("ExtVars/" + varname + ".var")
    out = var.read()
    var.close()
    return out
def setv(varname, txt):
    var = open("ExtVars/" + varname + ".var", 'w')
    var.write(txt)
    var.close()
def addv(varname, txt):
    var = open("ExtVars/" + varname + ".var", 'a')
    var.write(txt)
    var.close()
