__all__ = [
    'read_nv21_from_file',
    'nv21_to_rgb',
    'yuv_to_nv21',
]

from pathlib import Path
from typing import Union

import cv2
import numpy as np


def read_nv21_from_file(
        file_path: Union[str, Path],
        width: int,
        height: int,
) -> np.ndarray:
    """Reads the frame stored using the NV21 format from
    the specified file and then converts it into an RGB image.

    NV21 image format contains the flattened image data.
    Therefore the user must specify the dimensions of the target frame.

    Parameters
    ----------
    file_path
        Path to the file containing the YUV data in NV21 image format.
    width
        Width of the image.
    height
        Height of the image.

    Returns
    -------
    :
        A numpy array containing the image data in RGB format.
        The shape of the array is [height, width, 3].
    """
    # Check the path
    file_path = Path(file_path)

    if not file_path.is_file():
        raise FileNotFoundError(
            f'The specified path does not point to a valid file: "{file_path.resolve()}".'
        )

    with file_path.open('rb') as file:
        nv21_frame_data: np.ndarray = np.fromfile(file, dtype=np.uint8)

    return nv21_to_rgb(
        nv21_frame_data,
        width,
        height,
    )


def nv21_to_rgb(
        nv21_data: np.ndarray,
        width: int,
        height: int,
) -> np.ndarray:
    """Converts the provided frame data in the NV21 format into an RGB image.

    NV21 image format contains the flattened image data.
    Therefore the user must specify the dimensions of the target frame.

    Parameters
    ----------
    nv21_data
        Frame data stored using the NV21 format. Must be a numpy array containing np.uint8 data.
    width
        Width of the image.
    height
        Height of the image.

    Returns
    -------
    :
        A numpy array containing the image data in RGB format.
        The shape of the array is [height, width, 3].
    """
    # Check parameters
    if not isinstance(nv21_data, np.ndarray):
        raise TypeError(f'Frames data must be provided using a numpy ndarray, got {type(nv21_data)}.')

    if nv21_data.dtype != np.uint8:
        raise TypeError(f'Frame data must be provided using the np.uint8 data type, got {nv21_data.dtype}.')

    if nv21_data.ndim not in [1, 2]:
        raise ValueError(
            f'Array, containing frame data must be one or two dimensional. Got array with the shape {nv21_data.shape}.'
        )

    if not isinstance(width, int) or not isinstance(height, int):
        raise TypeError(
            f'Width and height are expected to be integer values, '
            f'got {type(width)} and {type(height)} respectively.'
        )

    if width < 2 or height < 2:
        raise ValueError(
            f'Width and height must be at least two pixels, got {width} and {height} respectively.'
        )

    # Process the file data.

    # In NV21 format the data packed in the following way:
    #   Y-data [h, w]
    #   UV-data [h // 2, w]
    # The whole 2D array is a concatenation of these two: [h * 3 // 2, w]
    nv21_height = height * 3 // 2

    if nv21_data.ndim == 1:
        if nv21_data.size < nv21_height * width:
            raise ValueError(
                f'The provided one dimensional frame data array contains {nv21_data.size} bytes, '
                f'but for the specified height ({height}) and width ({width}) '
                f'at least {width * nv21_height} bytes required.\n'
                f'Check if the specified frame data is consistent with the specified dimensions.'
            )
        data_to_convert = nv21_data[:nv21_height * width].reshape((nv21_height, width))
    else:
        if nv21_data.shape != (nv21_height, width):
            raise ValueError(
                f'When a two dimensional array provided, its shape must be exactly (height * 3 //2, width). '
                f'Expected {(nv21_height, width)}, got {nv21_data.shape}.'
            )
        data_to_convert = nv21_data

    rgb_img = cv2.cvtColor(data_to_convert, cv2.COLOR_YUV2RGB_NV21)

    return rgb_img


def yuv_to_nv21(
    image_yuv: np.ndarray,
) -> np.ndarray:
    """Converts YUV image into NV21 format.

    Parameters
    ----------
    image_yuv
        Image data in YUV format with np.uint8 data type.

    Returns
    -------
    :
        A two dimensional numpy array containing the image data in NV21 format
    """

    if not isinstance(image_yuv, np.ndarray):
        raise TypeError(f'Image must be provided using a numpy ndarray, got {type(image_yuv)}')

    if image_yuv.dtype != np.uint8:
        raise TypeError(f'Image data must be provided using the np.uint8 data type, got {image_yuv.dtype}.')

    if image_yuv.ndim != 3:
        raise ValueError(f'Image mus be a three dimensional array, got array of shape {image_yuv.shape}.')

    if image_yuv.size == 0:
        raise ValueError(f'The specified ndarray is empty, got shape {image_yuv.shape}.')

    if image_yuv.shape[2] != 3:
        raise ValueError(f'The specified image must have exactly three channels, got {image_yuv.shape[2]}.')

    if image_yuv.shape[0] % 2 != 0 or image_yuv.shape[1] % 2 != 0:
        raise ValueError(f'Spatial dimensions of the image cannot be odd, got shape {image_yuv.shape}.')

    h, w = image_yuv.shape[:2]

    nv21_data = np.concatenate(
        [image_yuv[..., 0], image_yuv[::2, ::2, 2:0:-1].reshape(h // 2, w)],
        axis=0,
    )

    return nv21_data
