import cv2
import threading
from .SoundSystem.SoundManager import sound_manager
from .SoundSystem.AudioCommands import CommandListener
from multiprocessing import  Queue
from .Models.ParallelProcessing import Worker
import time



class drowsiness_detector(threading.Thread):

        def __init__(self,audio=None,UseAssistant = False):
            super().__init__()
            self.__stream = cv2.VideoCapture(0)
            self.MySoundManager = sound_manager(audio=audio)
            self.Assistant = None
            self.input_queue = Queue()
            self.result_queue = Queue()
            self.worker = Worker(input_frames=self.input_queue,result_queue=self.result_queue)
            self.worker.start()
            if UseAssistant:
                self.Assistant = CommandListener(self)
                self.Assistant.start()
            self.LastTime = time.perf_counter()

        def setSensitivity(self, sensitivity):
            self.MySoundManager.setSensitivity(sensitivity)

        def __getFrame(self):
            retrieved, frame = self.__stream.read()
            if not retrieved:
                print("error occurred while capturing video stream")
                return None
            return frame



        def __display_frame(self, frame):
            cv2.imshow('frame', frame)
            # waiting for 1ms before proceeding further
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return False
            return True

        def run(self):
            while True:
                frame = self.__getFrame()
                if frame is None:
                    continue

                #l_eye, r_eye = self.__getLeftEye_RightEye(frame)
                #left_eye_open = predict(self.__processSingleEye(l_eye))
                #right_eye_open = predict(self.__processSingleEye(r_eye))
                #self.MySoundManager.handle_sound(left_eye_open and right_eye_open)
                if self.input_queue.empty():
                    print("submitting",time.perf_counter() - self.LastTime)
                    self.LastTime = time.perf_counter()
                    self.input_queue.put(frame)

                if  not  self.result_queue.empty():
                    result = self.result_queue.get()
                    self.MySoundManager.handle_sound(result)



                if not self.__display_frame(frame):
                    break
            self.__stream.release()
            if self.Assistant is not None:
                self.Assistant.stop()
            self.worker.kill()
            cv2.destroyAllWindows()



if __name__=="__main__":
    d = drowsiness_detector(UseAssistant=True)
    d.start()
    d.join()

