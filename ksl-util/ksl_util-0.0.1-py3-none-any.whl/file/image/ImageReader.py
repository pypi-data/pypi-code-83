import os
import shutil
from multiprocessing import Process, Queue
from pathlib import Path

import cv2
import numpy as np
from ksl_util.file.directory.directory_manager import mkdir
from ksl_util.log import printlog
from ksl_util.time.time_check import TimeCheck


class ImageReader:

    def __init__(self, directory, number=1, grayscale=False, reverse=False):

        self.directory                      = directory
        self.index                          = -1
        self.grayscale                      = grayscale
        self.nameList                       = os.listdir(directory)
        self.indexes                        = [i for i in range(0, number)]
        self.max_length                     = number
        self.reverse                        = reverse

        self.nameList.sort()
        if reverse:
            self.nameList.reverse()
        np.random.shuffle(self.indexes)

    def setOrder(self, numberList):

        assert len(numberList) == len(self.indexes)

        self.indexes = numberList


    def changeDirectory(self, directory):
        self.directory                      = directory
        self.nameList                       = os.listdir(directory)
        self.nameList.sort()
        if self.reverse: self.nameList.reverse()



    def read(self, callback=None, withName=False):

        self.index = (self.index + 1) % self.max_length
        # printlog("::::: %d" % self.max_length)
        index = self.indexes[self.index] % len(self.nameList)

        image = None
        while image is None or len(image.shape) != 3:
            image = cv2.imread('%s/%s' % (self.directory, self.nameList[index]), cv2.IMREAD_COLOR)
            # print('%s/%s' % (self.directory, self.nameList[index]))

        if self.grayscale:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if callback is not None:
            image = callback(image)


        if withName:
            return image, '%s/%s' % (self.directory, self.nameList[index])
        else:
            return image


class ImagePairReader:

    def __init__(self, directory1, directory2, reverse=False):

        assert len(directory1) == 3 and len(directory2) == 3
        assert os.path.exists(directory1[0]), directory1[0]
        assert os.path.exists(directory2[0]), directory2[0]
        assert isinstance(directory1[1], int) and isinstance(directory2[1], int)
        assert isinstance(directory1[2], bool) and isinstance(directory2[2], bool)
        assert directory1[1] == directory2[1]

        self.iR1 = ImageReader(directory=directory1[0], number=directory1[1], grayscale=directory1[2], reverse=reverse)
        self.iR2 = ImageReader(directory=directory2[0], number=directory2[1], grayscale=directory2[2], reverse=reverse)

        self.indexes = [i for i in range(0, directory1[1])]
        np.random.shuffle(self.indexes)

        self.iR1.setOrder(self.indexes)
        self.iR2.setOrder(self.indexes)


    def changeDirectory(self, directory1, directory2):
        self.iR1.changeDirectory(directory1)
        self.iR2.changeDirectory(directory2)


    def changeOrder(self):
        np.random.shuffle(self.indexes)

        self.iR1.setOrder(self.indexes)
        self.iR2.setOrder(self.indexes)



    def read(self, callback=None, withName=False):

        img1, name1 = self.iR1.read(callback=callback, withName=True)
        img2, name2 = self.iR2.read(callback=callback, withName=True)
        # printlog(name1, name2)

        tmp1, tmp2 = name1, name2
        name1 = name1.split('/')
        name1 = name1[len(name1)-1].replace('.jpeg', '.png').replace('.jpg', '.png')
        name2 = name2.split('/')
        name2 = name2[len(name2)-1]
        assert name1 == name2, '%s :: %s' % (tmp1, tmp2)

        if withName:
            return (img1, name1), (img2, name2)
        else:
            return img1, img2


class ImageCopier:


    def __init__(self, src, dst, number, callback=None, arg=None, reverse=False):

        assert os.path.exists(src)
        assert os.path.exists(dst)
        assert isinstance(number, int) or isinstance(number, np.int32)

        self.src                            = src
        self.dst                            = dst
        self.number                         = number

        self.callback                       = callback
        self.arg                            = arg
        self.reverse                        = reverse

    def __copyProcess__(self):

        # get file names
        file_names = os.listdir(self.src)
        file_names.sort()
        if self.reverse: file_names.reverse()
        file_names = file_names[0:min(self.number, len(file_names))]

        # copies
        for file_name in file_names:
            file_name = file_name.replace('jpg', 'png')
            shutil.copy('%s/%s' % (self.src, file_name), '%s/%s' % (self.dst, file_name))

        if self.callback is not None:
            self.callback(self.arg)


    def build(self):
        self.process = Process(target=self.__copyProcess__)
        self.process.daemon = True
        self.process.start()


    def join(self):
        self.process.join()



class ImageQueue:

    def __init__(self, dir1, dir2, totalNum, capacity, batch=1, grayscale=(False, True), callback=None, reverse=False):

        assert len(grayscale) == 2

        self.queue                              = Queue()
        self.pathQueue                          = Queue()

        self.dir1                               = (dir1, totalNum, grayscale[0])
        self.dir2                               = (dir2, totalNum, grayscale[1])
        self.totalNum                           = totalNum

        self.capacity                           = capacity
        self.batch                              = batch

        self.callback                           = callback

        self.process                            = Process(target=self.__Process__, args=[self.queue, self.pathQueue, self.dir1, self.dir2, callback, reverse])
        self.process.daemon                     = True
        self.process                            .start()

    def changeDirectories(self, dir1, dir2):
        self.pathQueue.put((dir1, dir2))


    def stop(self):
        self.process.kill()


    def get(self, callback=None):

        imgs, gnds = list(), list()

        while len(imgs) != self.batch:
            img, gnd = self.queue.get()
            if callback is not None:
                img, gnd = callback(img, gnd)

            imgs.append(img)
            gnds.append(gnd)

        return np.asarray(imgs), np.asarray(gnds)


    def currentSize(self):
        return self.queue.qsize()


    def __Process__(self, queue, pathQueue, info1, info2, callback, reverse):

        IPL = ImagePairReader(directory1=info1, directory2=info2, reverse=reverse)
        number = 0

        while True:

            if pathQueue.qsize() > 0:
                path1, path2 = pathQueue.get()
                IPL.changeDirectory(path1, path2)

            if queue.qsize() > self.capacity: continue

            queue.put(IPL.read(callback=callback))
            number += 1

            if number >= self.totalNum:
                number = 0
                IPL.changeOrder()

    def __len__(self):
        return self.queue.qsize()




class ImageBatchLoader:

    def __init__(self, dir1, dir2, totalNum, capacity, batch=1, grayscale=(False, True), callback=None, save_flag=True, save_dir='.', reverse=False):

        # make tmp directory
        self.tmpPath                        = '%s/Desktop/.tf_tmp' % Path.home()
        self.tmpPath                        = mkdir(self.tmpPath)
        self.tmpPath                        = '%s/%s' % (self.tmpPath, save_dir)

        if os.path.exists(self.tmpPath): shutil.rmtree(self.tmpPath, ignore_errors=True)

        self.queue                          = Queue()
        self.imgPath                        = mkdir('%s/img' % self.tmpPath)
        self.gndPath                        = mkdir('%s/gnd' % self.tmpPath)

        self.imageQueue                     = ImageQueue(dir1, dir2, totalNum, capacity, batch, grayscale, callback, reverse)
        self.imgCopier                      = ImageCopier(dir1, self.imgPath, totalNum, callback=self.__copyCallback__, arg=self.queue, reverse=reverse)
        self.gndCopier                      = ImageCopier(dir2, self.gndPath, totalNum, callback=self.__copyCallback__, arg=self.queue, reverse=reverse)

        if save_flag:
            self.imgCopier.build()
            self.gndCopier.build()

            thread                              = Process(target=self.__checkThread__, args=(self.queue,))
            thread.daemon                       = True
            thread                              .start()

    def deleteDir(self):
        shutil.rmtree(self.tmpPath, ignore_errors=True)


    def get(self, callback=None):
        return self.imageQueue.get(callback=callback)

    # run in another process
    def __copyCallback__(self, queue):
        queue.put('1')


    def __checkThread__(self, queue):

        while queue.qsize() < 2:
            continue

        self.imageQueue.changeDirectories(self.imgPath, self.gndPath)