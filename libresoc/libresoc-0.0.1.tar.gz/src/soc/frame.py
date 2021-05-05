import inspect

def callfrom():
    print ('caller name:', inspect.stack()[1][3])

def callfrom2():
    callfrom()

if __name__ == '__main__':
    callfrom2()
