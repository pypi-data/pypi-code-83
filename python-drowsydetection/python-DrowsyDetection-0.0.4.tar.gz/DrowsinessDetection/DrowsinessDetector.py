import cv2
import numpy as np
import threading
from .Models.predict  import predict
from .SoundSystem.SoundManager import sound_manager
from pathlib import  Path
import os


class drowsiness_detector(threading.Thread):
    __haar_files = os.path.join(Path(__file__).parent , "haar cascade files" )
    __Face = cv2.CascadeClassifier(os.path.join(__haar_files,'haarcascade_frontalface_alt.xml'))
    __LeftEye = cv2.CascadeClassifier(os.path.join(__haar_files,'haarcascade_lefteye_2splits.xml'))
    __RightEye = cv2.CascadeClassifier(os.path.join(__haar_files,'haarcascade_righteye_2splits.xml'))

    def __init__(self):
        super().__init__()

        self.__stream = cv2.VideoCapture(0)
        self.__StopInterrupt = False
        self.MySoundManager = sound_manager()








    def __getFrame(self):
        retrieved , frame = self.__stream.read()
        if not retrieved:
            print("error occurred while capturing video stream")
            return None
        return frame

    def __getLeftEye_RightEye(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.__class__.__Face.detectMultiScale(gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))
        left_eyes = self.__class__.__LeftEye.detectMultiScale(gray)
        right_eyes = self.__class__.__RightEye.detectMultiScale(gray)

        # highlighting face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 1)

        #highliting right eye
        for (x, y, w, h) in right_eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 1)
            # cropping and converting to gray scale
            r_eye = frame[y:y + h, x:x + w]
            right_eyes = cv2.cvtColor(r_eye, cv2.COLOR_BGR2GRAY)
            break

        # highlighting left eye
        for (x, y, w, h) in left_eyes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 1)
            # cropping and converting to gray scale
            l_eye = frame[y:y + h, x:x + w]
            left_eyes = cv2.cvtColor(l_eye, cv2.COLOR_BGR2GRAY)
            break

        return left_eyes,right_eyes

    def __processSingleEye(self,eye):
        # resizing the image
        try:
            eye = cv2.resize(eye,(24,24))
            # having values of every element between 0 and 1
            eye = eye/255
            eye = eye.reshape(24, 24, -1)
            eye = np.expand_dims(eye, axis=0)
            return eye
        except :
            pass


    def __display_frame(self,frame):
        # (number of rows , number of columns , 3 for colored and 0 for grayscale)
        # so we take rows as height and columns as width
        #height, width = frame.shape[:2]
        # creating area where to show score
        # and we have left
        # we have  start point as (0,height -50)
        # end point as (200,height)
        # color as (0,0,0) black
        # thickness as -1 fill the rectangle
        #cv2.rectangle(frame, (0, height - 50), (200, height), (0, 0, 0), thickness=cv2.FILLED)
        # displaying the frame
        cv2.imshow('frame', frame)
        # waiting for 1ms before proceeding further
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False
        return True




    def run(self):
        while True:
            # retrieving frame from cv2
            frame = self.__getFrame()
            if frame is None :
                continue
            l_eye,r_eye = self.__getLeftEye_RightEye(frame)
            left_eye_open = predict(self.__processSingleEye(l_eye))
            right_eye_open = predict(self.__processSingleEye(r_eye))
            self.MySoundManager.handle_sound(left_eye_open and right_eye_open)
            if not self.__display_frame(frame):
                break
        self.__stream.release()
        cv2.destroyAllWindows()

