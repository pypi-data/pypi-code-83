import os
from pathlib import Path
import cv2
import numpy as np
from .predict import predict
from multiprocessing import  Process



class Worker(Process):

    haar_files = os.path.join(Path(__file__).parent.parent, "haar cascade files")
    LeftEye = cv2.CascadeClassifier(os.path.join(haar_files, 'haarcascade_lefteye_2splits.xml'))
    RightEye = cv2.CascadeClassifier(os.path.join(haar_files, 'haarcascade_righteye_2splits.xml'))

    def __init__(self,input_frames,result_queue):
        super().__init__()
        self.input_queue = input_frames
        self.result_queue = result_queue


    def run(self):
        while True:
            if not self.input_queue.empty():
                frame = self.input_queue.get()
                open_closed = self.process(frame)
                self.result_queue.put(open_closed)


    def process(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        left_eyes = self.__class__.LeftEye.detectMultiScale(gray)
        right_eyes = self.__class__.RightEye.detectMultiScale(gray)

        for (x, y, w, h) in right_eyes:
            r_eye = frame[y:y + h, x:x + w]
            right_eyes = cv2.cvtColor(r_eye, cv2.COLOR_BGR2GRAY)
            break

        for (x, y, w, h) in left_eyes:
            l_eye = frame[y:y + h, x:x + w]
            left_eyes = cv2.cvtColor(l_eye, cv2.COLOR_BGR2GRAY)
            break

        l = self.process_single_eye(right_eyes)
        r = self.process_single_eye(left_eyes)

        return predict(l) and predict(r)

    def process_single_eye(self,eye):
        try:
            eye = cv2.resize(eye, (24, 24))
            # having values of every element between 0 and 1
            eye = eye / 255
            eye = eye.reshape(24, 24, -1)
            eye = np.expand_dims(eye, axis=0)
            return eye
        except:
            pass
