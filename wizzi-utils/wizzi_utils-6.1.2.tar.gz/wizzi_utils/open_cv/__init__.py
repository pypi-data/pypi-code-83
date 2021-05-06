"""
:requires: cv2
:sub_package: wizzi_utils.pyplot
"""
try:
    from wizzi_utils.open_cv.open_cv_tools import *
except ModuleNotFoundError as e:
    pass

from wizzi_utils.open_cv import test
