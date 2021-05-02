import numpy as np
from imPixelate import pix
import numba

@numba.njit()
def _crook(image, RTL=True):
    [h, w] = image.shape
    fixed_image = image.copy()
    crooked_image = np.zeros((h, w+h-1))
    for i in range(h):
        if RTL:
            crooked_image[i, 0+i:w+i] = image[i, :]
        else:
            crooked_image[i, h-1-i:w+h-1-i] = image[i, :]
    return crooked_image

@numba.njit()
def _decrook(crooked_image, RTL=True):                  
    [h, w] = crooked_image.shape
    fixed_image = np.zeros((h, w-h+1))
    for i in range(h):
        if RTL:
            fixed_image[i, :] = crooked_image[i, 0+i:w-h+1+i]
        else:
            fixed_image[i, :] = crooked_image[i, h-1-i:w-i]
    return fixed_image

def triangle(image, r = None):
    h = image.shape[0]
    w = image.shape[1]
    if not r:
        r = min(h, w)//150
    image_crooked_left = _crook(image, RTL=True)
    image_pix_crooked_left = pix(image_crooked_left, r)
    image_pix_decrooked_left = _decrook(image_pix_crooked_left, RTL=True)
    
    image_crooked_right = _crook(image, RTL=False)
    image_pix_crooked_right = pix(image_crooked_right, r)
    image_pix_decrooked_right = _decrook(image_pix_crooked_right, RTL=False)
    
    return ((image_pix_decrooked_right+image_pix_decrooked_left)/2).astype(image.dtype)




