import multiprocessing
import os

import cv2
import numpy as np

from ksl_util.log import printlog
from ksl_util.multiprocessing.mp_class import SingleProcess, Processes
from ksl_util.time.time_check import TimeCheck

import ctypes

import platform


class Loader:

    def __init__(self):
        self.path = None
        self.names = None
        self.index = 0
        self.index_random = 0
        self.random_indexes = None
        self.current_images = list()


        ###### for testing
        self.flagg = False


    def load_path(self, path):

        assert os.path.exists(path)

        self.path = path
        self.names = os.listdir(path)
        self.random_indexes = np.asarray(range(0, len(self.names)))

        np.random.shuffle(self.random_indexes)

        return self


    def load_images(self, numImages=None, grayscale=False, printable=True, random=False, callbacks=None):

        if self.flagg:
            return self.current_images

        self.current_images.clear()
        if numImages is None:
            numImages = self.__len__()

        while len(self.current_images) != numImages:
            if random:
                image = cv2.imread('%s/%s' % (self.path, self.names[self.random_indexes[self.index_random]]))
            else:
                image = cv2.imread('%s/%s' % (self.path, self.names[self.index]))

            if grayscale:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                image = np.expand_dims(image, axis=3)
            if printable: print('%s' % self.names[self.random_indexes[self.index_random]], end=', ')

            self.current_images.append(image)

            if random:
                self.index_random = (self.index_random + 1) % self.__len__()
                if self.index_random == 0:
                    np.random.shuffle(self.random_indexes)
            else:
                self.index = (self.index + 1) % self.__len__()

        if printable: print('')

        if callbacks is not None:
            self.current_images = callbacks(self.current_images)

        self.flagg = True
        return self.current_images



    def __len__(self):
        return len(self.names)


    def __getitem__(self, item):
        return self.current_images[item]



class PairLoader:

    def __init__(self):
        self.path1                                      = None
        self.path2                                      = None
        self.names1                                     = None
        self.names2                                     = None
        self.random_indexes                             = None
        self.current_images                             = list()

        self.index                                      = 0
        self.index_random                               = 0


    def load_path(self, path1, path2):

        assert os.path.exists(path1)
        assert os.path.exists(path2)

        self.path1                                      = path1
        self.path2                                      = path2

        self.names1                                     = os.listdir(path1)
        self.names2                                     = os.listdir(path2)
        
        self.names1                                     .sort()
        self.names2                                     .sort()

        self.random_indexes                             = np.asarray(range(0, len(self.names1)))

        assert len(self.names1) == len(self.names2)
        np.random.shuffle(self.random_indexes)


        return self


    def load_images(self, numImages=None, grayscales=(False, True), printable=True, random=False, callbacks=None):

        assert len(grayscales) == 2

        self.current_images.clear()

        if numImages is None:
            numImages = len(self.names1)

        while len(self.current_images) != numImages:
            if random:
                image1 = cv2.imread('%s/%s' % (self.path1, self.names1[self.random_indexes[self.index_random]]))
                image2 = cv2.imread('%s/%s' % (self.path2, self.names2[self.random_indexes[self.index_random]]))
            else:
                image1 = cv2.imread('%s/%s' % (self.path1, self.names1[self.index]))
                image2 = cv2.imread('%s/%s' % (self.path2, self.names2[self.index]))


            if grayscales[0]:
                image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
                image1 = np.expand_dims(image1, axis=3)
            if grayscales[1]:
                image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
                image2 = np.expand_dims(image2, axis=3)


            if printable:
                if random:
                    print('%s, %s' % (self.names1[self.random_indexes[self.index_random]], self.names2[self.index]), end='| ')
                else:
                    print('%s, %s' % (self.names1[self.index], self.names2[self.index]), end='| ')

            self.current_images.append((image1, image2))


            if random:
                self.index_random = (self.index_random + 1) % self.__len__()
                if self.index_random == 0:
                    np.random.shuffle(self.random_indexes)
            else:
                self.index = (self.index + 1) % self.__len__()

        if printable: print('')

        if callbacks is not None:
            self.current_images = callbacks(self.current_images)

        return self.current_images


    def __len__(self):
        assert len(self.names2) == len(self.names1)
        return len(self.names1)


    def __getitem__(self, item):
        return self.current_images[item]


class __ImageHolder__(SingleProcess):

    def __init__(self):
        super().__init__()
        self.loader                                     = None
        self.holder                                     = multiprocessing.Queue()

        self.buffer_size                                = 100
        self.capacity                                   = 5
        self.grayscale                                  = False
        self.random                                     = False


    def setBufferSize(self, size):
        self.buffer_size                                = size
        return self

    def setCapacity(self, capacity):
        self.capacity                                   = capacity
        return self

    def setGrayScale(self, grayscale):
        self.grayscale                                  = grayscale
        return self

    def setPath(self, *path):
        pass

    def setRandom(self, random):
        self.random                                     = random
        return self


    def __job__(self, queue):
        while queue.qsize() < self.buffer_size:
            images = self.__load__images__()
            for image in images:
                queue.put(image)


    def __routine__(self, queue):
        while True:
            if queue.qsize() >= self.buffer_size: continue
            self.__job__(queue)


    def __init__process__(self):
        p = multiprocessing.Process(target=self.__routine__, args=[self.holder])
        p.daemon = True
        return p

    def load(self):
        Processes()\
        .append(self.build())\
        .start()

        while self.holder.qsize() < self.capacity:
            pass

    def get(self):
        item = self.holder.get()
        return item

    def get_items(self, numImages=1):

        while self.holder.qsize() <= self.capacity:
            pass
        tmp = list()
        image = self.get()
        while len(tmp) != numImages:
            tmp.append(image)
            del image
            image = self.get()
        del image

        return tmp

    def clear(self):
        self.holder.close()

    def __load__images__(self):
        pass

    def __len__(self):
        return self.holder.qsize()


class ImageHolder(__ImageHolder__):

    def __init__(self):
        super().__init__()
        self.loader = Loader()

    def setPath(self, *path):
        assert len(path) == 1
        self.loader.load_path(path[0])
        return self

    def __load__images__(self):
        return self.loader.load_images(numImages=self.capacity, grayscale=self.grayscale, printable=False, random=self.random)


class ImagePairHolder(__ImageHolder__):

    def __init__(self):
        super().__init__()
        self.loader = PairLoader()
        self.grayscale = (False, True)

    def setPath(self, *path):
        assert len(path) == 2
        assert os.path.exists(path[0]) and os.path.exists(path[1]), '%s %s' % (path[0], path[1])
        self.loader.load_path(path[0], path[1])
        return self

    def setGrayScale(self, grayscale):
        assert len(grayscale) == 2
        self.grayscale = grayscale
        return self

    @TimeCheck
    def __load__images__(self):
        return self.loader.load_images(numImages=self.capacity, grayscales=self.grayscale, printable=False, random=self.random)




def imread3(paths, flags=None):
    
    assert flags is None or len(paths) == len(flags) or len(flags) == 1
    
    tmp = list()
    
    for i in range(0, len(paths)):
        if flags is None:
            tmp.append(cv2.imread(paths[i], cv2.IMREAD_COLOR))
        elif len(flags) == 1:
            tmp.append(cv2.imread(paths[i], flags[0]))
        else:
            tmp.append(cv2.imread(paths[i], flags[i]))
    
    return tuple(tmp)


if platform.system() == 'Darwin':
    from AppKit import NSScreen

elif platform.system() != 'Windows':
    from Xlib.display import Display
    MAX_X = Display(':0').screen().width_in_pixels


def imshow2(images, nameflag='img', windowFlag=None, x=0, y=0, margin=10):

    if windowFlag is not None:
        assert len(images) == len(windowFlag)

    currentX = x
    currentY = y

    if platform.system() == 'Windows':
        maxX = ctypes.windll.user32.GetSystemMetrics(0)
    elif platform.system() == 'Darwin':
        maxX = NSScreen.mainScreen().frame().size.width
        margin += 120
    else:
        maxX = MAX_X
        margin += 120

    for index, image in enumerate(images):
        if windowFlag is None:
            cv2.imshow('%s%d' % (nameflag, index), image)
            cv2.moveWindow('%s%d' % (nameflag, index), currentX, currentY)
        else:
            cv2.imshow('%s_%s%d' % (windowFlag[index], nameflag, index), image)
            cv2.moveWindow('%s_%s%d' % (windowFlag[index], nameflag, index), currentX, currentY)
            

        currentX += margin + image.shape[1]
        if currentX + image.shape[1] > maxX:
            currentX = 0
            currentY += margin + image.shape[0] + 25



def image_modification(images, function, *args, **kwargs):

    tmp = list()
    
    for image in images:
        tmp.append(np.asarray(function(image, *args, **kwargs), dtype=np.uint8))
        
    return tuple(tmp)
