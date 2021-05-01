import os
from pathlib import Path
import cv2
import numpy as np
from multiprocessing import  Process

class WorkerResult():

    def __init__(self,leftEye,RightEye,openProbability):
        self.LeftEye = leftEye
        self.RightEye = RightEye
        self.OpenProbability = openProbability

    def __str__(self):
        return f"open -- > {self.OpenProbability}  left --> {self.LeftEye}   , right -> {self.RightEye}"


class Worker(Process):
    haar_files = os.path.join(Path(__file__).parent.parent, "haar cascade files")
    LeftEye = cv2.CascadeClassifier(os.path.join(haar_files, 'haarcascade_lefteye_2splits.xml'))
    RightEye = cv2.CascadeClassifier(os.path.join(haar_files, 'haarcascade_righteye_2splits.xml'))

    def __init__(self,input_frames,result_queue):
        super().__init__()
        self.input_queue = input_frames
        self.result_queue = result_queue
        self.model_loaded = False
        self.model = None

    def predict(self,Eye):
        if not self.model_loaded:
            from keras.models import load_model
            self.model = load_model(os.path.join(Path(__file__).parent, 'cnnCat2.h5'))
            self.model_loaded = True

        if Eye is None:
            # eyes are not detected so effectively we can consider this case as drowsy
            return 0
        ans = self.model.predict(Eye)[0]
        if ans[0] > ans[1]:
            return 0
        else:
            return 1

    def run(self):
        while True:
            if not self.input_queue.empty():
                frame = self.input_queue.get()
                worker_result = self.process(frame)
                print(worker_result)
                self.result_queue.put(worker_result)


    def process(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        left_eyes = self.__class__.LeftEye.detectMultiScale(gray)
        right_eyes = self.__class__.RightEye.detectMultiScale(gray)

        result = WorkerResult(leftEye=None,RightEye=None,openProbability=None)

        for (x, y, w, h) in right_eyes:
            result.RightEye = (x,y,w,h)
            r_eye = frame[y:y + h, x:x + w]
            right_eyes = cv2.cvtColor(r_eye, cv2.COLOR_BGR2GRAY)
            break

        for (x, y, w, h) in left_eyes:
            result.LeftEye = (x,y,w,h)
            l_eye = frame[y:y + h, x:x + w]
            left_eyes = cv2.cvtColor(l_eye, cv2.COLOR_BGR2GRAY)
            break

        l = self.process_single_eye(right_eyes)
        r = self.process_single_eye(left_eyes)
        result.OpenProbability = self.predict(l) and self.predict(r)
        return result

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
