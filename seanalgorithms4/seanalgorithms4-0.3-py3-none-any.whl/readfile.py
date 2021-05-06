import os
alist=[]
for (path, dir, files) in os.walk("D:\SEANLAB6\git_algorithms\py_algorithms4\seanalgorithms4"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        dirname=list(map(str,path.split('\\')))
        if dirname[-1] !="__pycache__" and dirname[-1] !="seanalgorithms3" and dirname[-1] !=".idea" :
            #print(dirname[-1])
            #print(dirname)
            if dirname[-1] not in alist :
                alist.append(dirname[-1])
                #print("  - [{}]({})".format(dirname[-1]))
        if ext == '.py' and filename[:-3]!="__init__" :
            print("     - [{}]({}/{})".format(filename[:-3],dirname[-1],filename))
            #print("%s/%s" % (path, filename))