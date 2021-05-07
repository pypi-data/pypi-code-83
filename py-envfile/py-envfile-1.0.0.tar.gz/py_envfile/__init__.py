def getenv(key):
    f = open('.env')
    for line in f:
        if line.startswith(key):
            return line.strip('\n').split('=')[1]

def getenvfile(envfile,key):
    f = open(envfile)
    for line in f:
        if line.startswith(key):
            return line.strip('\n').split('=')[1]

def dict2envs(objectr):
    out = ''
    for key in objectr:
        out += key + '=' + objectr[key] + '\n'
    return out

def envs2dict(envs):
    out = {}
    
    dictr = envs.split('\n')
    del dictr[-1]
    for line in dictr:
        out[line.split('=')[0]] = line.split('=')[1]
    return out

def envs2file(envname, envs):
    open(envname,'w').write(envs)

def setenvfile(envname, key, value):
    envs = open(envname).read()
    dicto = envs2dict(envs)
    if key in dicto:
        dicto[key] = value.replace('\n','\\n')
        f = open(envname, 'w')
        f.write(dict2envs(dicto))
    else:
        open(envname, 'a').write(key + '=' + value.replace('\n','\\n') + '\n')

def setenv(key, value):
    envname = '.env'
    
    envs = open(envname).read()
    dicto = envs2dict(envs)
    if key in dicto:
        dicto[key] = value.replace('\n','\\n')
        f = open(envname, 'w')
        f.write(dict2envs(dicto))
    else:
        open(envname, 'a').write(key + '=' + value.replace('\n','\\n') + '\n')
    
        
        


        
    
