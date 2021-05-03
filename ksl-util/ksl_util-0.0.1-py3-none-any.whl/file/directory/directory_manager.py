import os
import numpy as np
from os.path import expanduser
from ksl_util.time.time_check import current_date


def mkdir(dir_name, makeDir=True):
    if not os.path.exists(dir_name) and makeDir:
        os.makedirs('%s' % (dir_name))

    return os.path.abspath(dir_name)


def getFileList(directory, absolute=False, callback=None):

    tmp = os.listdir(directory)
    tmp.sort()
    if not absolute:
        return tmp

    lists = []
    for name in tmp:
        abName = '%s/%s' % (directory, name)
        if callback is not None:
            lists.append((abName, callback(abName)))
        else:
            lists.append(abName)

    return lists


def getFileLists(path1, path2, sort=True, absolute=False):
    
    tmp1 = os.listdir(path1)
    tmp2 = os.listdir(path2)
    
    if sort:
        tmp1.sort()
        tmp2.sort()
    
    if absolute:
        ab1 = ['%s/%s' % (path1, name) for name in tmp1]
        ab2 = ['%s/%s' % (path2, name) for name in tmp2]
        
        tmp1, tmp2 = ab1, ab2
    
    return tmp1, tmp2

def getFileLists3(paths, sort=True, absolute=False, number=None):

    tmp = list()
    
    for path in paths:
        tmp1 = os.listdir(path)
        tmp2 = []
        for t in tmp1:
            if t.find('.') == 0: continue
            tmp2.append(t)
        tmp1 = tmp2
        if sort:
            tmp1.sort()
    
        if absolute:
            ab1 = [os.path.abspath('%s/%s' % (path, name)) for name in tmp1]
            tmp1 = ab1

        if number is not None:
            tmp1 = tmp1[0:number]

        tmp.append(tmp1)

    return tuple(tmp)

from tqdm import tqdm
def checkNPZ(path, names):
    
    flag = True
    return_values = []
    return_values.append(False)
    for name in names:
        flag &= os.path.exists('%s/%s00.npz' % (path, name))
        print(flag, path, name)
        return_values.append(None)

    if not flag:
        return tuple(return_values)
    
    print('here')

    return_values.clear()
    return_values.append(True)
    for name in tqdm(names, desc='npz reading'):
        index = 0
        tmps = []
        error_count = 0
        while os.path.exists('%s/%s%02d.npz' % (path, name, index)):
            print('%s/%s%02d.npz' % (path, name, index))
            try:
                tmps.append(np.load('%s/%s%02d.npz' % (path, name, index))[name])
                index += 1
            except Exception as ex:
                error_count += 1
                print('error in %s_%d' % (name, index))
                
                if error_count >= 10:
                    return_values.clear()
                    return_values.append(False)
                    for name in names:
                        flag &= os.path.exists('%s/%s00.npz' % (path, name))
                        return_values.append(None)
                    return tuple(return_values)
        tmps = np.concatenate(tmps, axis=0)
        return_values.append(tmps)

    return_values = tuple(return_values)
    return tuple(return_values)


def search_files(root, ext: list = ['jpg', 'png'], useCache=True, refresh=False):
    r_values = []

    tmp_directory = mkdir('%s/.tmp_ksl' % expanduser('~'), makeDir=useCache)
    tmp_directory = mkdir('%s/search_files' % tmp_directory, makeDir=useCache)
    tmp_directory = mkdir('%s/%s__%s' % (tmp_directory, current_date(), os.getcwd().replace(':', '').replace(":\/\/", "__").replace(':\\\\', '__').replace('\/', '__').replace('\\', '__')), makeDir=useCache)
    file_name = os.path.basename(__file__).replace('py', 'txt')
    file_name = '%s/%s' % (tmp_directory, file_name)

    if refresh and os.path.exists(file_name):
        os.remove(file_name)

    if useCache and os.path.exists(file_name):
        line = []
        with open(file_name, 'r') as f:
            txt = f.readline()
            while txt:
                txt = txt.rstrip().lstrip()
                line.append(txt)
                txt = f.readline()
        return line

    for (root, dirs, files) in os.walk(root):
        r_values.extend(['%s/%s' % (root, file) for file in files if os.path.splitext(file)[1].replace('.', '') in ext])

    r_values = [value for value in r_values if os.path.splitext(value)[1] in ['.%s' % e for e in ext]]

    if useCache:
        with open(file_name, 'w') as f:
            for r_value in r_values:
                f.write('%s\n' % os.path.abspath(r_value))

    return r_values


