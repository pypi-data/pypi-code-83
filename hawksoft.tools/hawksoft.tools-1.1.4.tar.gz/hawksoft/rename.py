
import os
import sys
import shutil

curPath = '.'

def walkFile(exts,fromDir,toDir):
    tmpPath = os.path.join(curPath,fromDir)
    index = 0
    for curDir,dirs,files in os.walk(tmpPath):
        for name in files:
            curFile = os.path.join(curDir,name)
            filePath, fileFullName = os.path.split(curFile)
            extension = fileFullName.split('.')[-1]
            if extension == exts:
                print('moving: {} '.format(fileFullName))
                temp = toDir + str(index)+'.' + extension
                shutil.move(curFile,temp)
                index = index + 1
    print('Finished!')

def main(args = None):
    if len(sys.argv) <4 :
        print('usage: rename ext fromDir newName.')
    else:
        fromPath = os.path.abspath(sys.argv[2])
        toPath = os.path.abspath(sys.argv[3])
        if not os.path.exists(fromPath):

            print('the directory [{}] dose not exist!'.format(fromPath))
            exit()
        #if not os.path.exists(toPath):
        #    sel1 = input('the directory[{}] dose not exist!\n are you sure to create it?(y/n)'.format(toPath))
        #    if sel1 == 'y' or sel1 == 'Y':
        #        os.mkdir(toPath)
        #        print("the directory [{}] was created!".format(toPath))
        #    else:
        #        exit()

        print('will rename all files with {} exts in [{}] to new name '.format(sys.argv[1],fromPath))
        sel = input('are you sure to rename?(y/n)')
        if sel == 'y' or sel == 'Y':
            walkFile(sys.argv[1],fromPath,toPath)    

if __name__ == '__main__':
    main()
    
