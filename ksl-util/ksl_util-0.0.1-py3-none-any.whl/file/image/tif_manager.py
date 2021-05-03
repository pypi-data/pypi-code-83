from skimage import io
import cv2
import numpy as np

def read_tif(file_name, alpha=0.3):

    images = io.imread(file_name)
    tmp = []
    for image in images:
        tmp.append(cv2.convertScaleAbs(image, alpha=alpha))
    return np.asarray(tmp)

