from pygame import mixer
import cv2
from threading import  Timer
import os
from pathlib import  Path






class sound_manager:
    __font = cv2.FONT_HERSHEY_COMPLEX_SMALL

    def __init__(self):
        mixer.init()
        self.__sound = mixer.Sound(os.path.join(Path(__file__).parent , "alarm.wav" ))
        self.__timer = None # used to play audio after certain time
        self.__lastState = None # used to filter out the events




    def handle_sound(self,open_eyes):
         # check if state of eyes are not changed then exit
          if open_eyes == self.__lastState:
              return
          # state is changed so cache the state
          self.__lastState = open_eyes

          if  open_eyes:
              # here we are logically revoking the timer by cancelling it if any timer was set
              # who  can play sound  after its timeout triggers
              print("revoked")
              if self.__timer:
                  self.__timer.cancel()
              self.stop_sound()

          else:
              # here state of eyes is closed but we will wait for sone time maybe he will open his eyes
              # then timer will be revoked by upper if condition
              # else it will play sound after that time interval
              print("drowsy chances")
              self.__timer = Timer(1,function=self.handle_delayed)
              self.__timer.start()



    def handle_delayed(self):
          self.__sound.play(loops=-1)


    def stop_sound(self):
        self.__sound.stop()





