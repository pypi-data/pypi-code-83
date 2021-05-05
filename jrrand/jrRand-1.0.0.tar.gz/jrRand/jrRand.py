import random,time,sys
def randint(a:int,b:int):
    return random.randint(a,b)
def randfloat(a:int,b:int):
    x=10**(b-1)
    y=10**b-1
    z=random.randint(x,y)
    z=z/(10**b)
    return z+a
def randword():
    word=[chr(i) for i in range(19968,40918)]
    return random.choice(word)
def printf(text,times,color,background):
    try:
        print("\033[3{};4{}m{}".format(color,background,text))
        time.sleep(times)
    except:
        print("\033[3;4;31;47m代码有误\033[0m")
        sys.exit(0)
def clean():
    print("\033[2J\033[00H",end="")