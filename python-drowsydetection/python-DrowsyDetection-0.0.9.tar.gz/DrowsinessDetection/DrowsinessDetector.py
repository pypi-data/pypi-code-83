import cv2
import threading
from .SoundSystem.SoundManager import sound_manager
from .SoundSystem.AudioCommands import CommandListener
from multiprocessing import Queue
from .Models.ParallelProcessing import Worker


class drowsiness_detector(threading.Thread):

    __FONT =  cv2.FONT_HERSHEY_COMPLEX_SMALL

    def __init__(self, audio=None, UseAssistant=False):
        super().__init__()
        self.__stream = cv2.VideoCapture(0)
        self.__MySoundManager = sound_manager(audio=audio)
        self.__Assistant = None
        self.__input_queue = Queue()
        self.__result_queue = Queue()
        self.__worker = Worker(input_frames=self.__input_queue, result_queue=self.__result_queue)
        self.__worker.start()
        self.__LastWorkerResult = None
        self.__Interrupt = False
        if UseAssistant:
            self.__Assistant = CommandListener(self)
            self.__Assistant.start()

    def setSensitivity(self, sensitivity):
        self.__MySoundManager.setSensitivity(sensitivity)

    def __getFrame(self):
        retrieved, frame = self.__stream.read()
        if not retrieved:
            print("error occurred while capturing video stream")
            return None
        return frame

    def __display_frame(self, frame):

        if self.__LastWorkerResult is not None:
            for eye in [self.__LastWorkerResult.LeftEye, self.__LastWorkerResult.RightEye]:
                 if eye is not None:
                     x, y, w, h = eye
                     cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 1)
                     message = "closed" if self.__LastWorkerResult.OpenProbability == 0 else "open"
                     self.__putMessage(message, frame)
                 else:
                     self.__putMessage("Eyes not detected", frame)
        else:
            self.__putMessage("Initializing .......",frame=frame)

        cv2.imshow('frame', frame)
        # waiting for 1ms before proceeding further
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False
        return True

    def __putMessage(self,message,frame):
        cv2.putText(frame, message, (10, frame.shape[:2][0] - 20), self.__class__.__FONT, 1, (255, 255, 255), 1,
                    cv2.LINE_AA)

    def run(self):
        while True:
            frame = self.__getFrame()
            if frame is None:
                continue

            if self.__input_queue.empty():
                print("sended frame")
                self.__input_queue.put(frame)

            if not self.__result_queue.empty():
                self.__LastWorkerResult = self.__result_queue.get()
                self.__MySoundManager.handle_sound(self.__LastWorkerResult.OpenProbability)

            if not self.__display_frame(frame)  or self.__Interrupt:
                break
        self.__stream.release()
        if self.__Assistant is not None:
            self.__Assistant.stop()
        self.__worker.kill()
        cv2.destroyAllWindows()

    def quit(self):
        self.__Interrupt = True


if __name__ == "__main__":
    d = drowsiness_detector(UseAssistant=True)
    d.start()
    d.join()
