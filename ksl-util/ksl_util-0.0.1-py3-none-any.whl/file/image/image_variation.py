import numpy as np


def random_crop(image, new_shape=None, fh=1., fw=1., onlyIndex=True):

    # assert len(image.shape) == 3
    assert new_shape is None or len(new_shape) == 2

    image_width, image_height = image.shape[:2]

    if (fw != 1. or fh != 1.) and new_shape is None:
        new_shape = (int(image_width * fh), int(image_height * fw))

    if new_shape is None:
        new_shape = (image_width, image_height)


    new_width, new_height = new_shape
    sub_width, sub_height = image_width - new_width, image_height - new_height
    width_range, height_range = np.asarray(range(0, sub_width + 1)), np.asarray(range(0, sub_height + 1))

    width, height = np.random.choice(width_range, size=1, replace=False)[0], np.random.choice(height_range, size=1, replace=False)[0]

    if onlyIndex:
        return CropObject((width, width + new_width, height, height + new_height))
    else:
        if len(image.shape) == 3:
            return image[width:width+new_width, height:new_height, :]
        else:
            return image[width:width+new_width, height:new_height + height]




class CropObject:

    def __init__(self, point):
        self.point = point

    def crop(self, image):
        assert len(image.shape) == 3 or len(image.shape) == 2

        point = self.point
        
        if len(image.shape) == 3:
            return image[point[0]:point[1], point[2]:point[3], :]
        else:
            return image[point[0]:point[1], point[2]:point[3]]

    def __repr__(self):
        return '(%d, %d, %d, %d)' % (self.point[0], self.point[1], self.point[2], self.point[3])

