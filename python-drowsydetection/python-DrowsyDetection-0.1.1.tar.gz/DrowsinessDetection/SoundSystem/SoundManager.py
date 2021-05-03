from pygame import mixer
from threading import  Timer
import os
from pathlib import  Path






class sound_manager:
    SENSITIVITY_LOW = 20
    SENSITIVITY_MEDIUM = 10
    SENSITIVITY_HIGH = 5

    def __init__(self,audio):
        mixer.init()
        if audio is None:
            self.__sound = mixer.Sound(os.path.join(Path(__file__).parent , "alarm.wav" ))
        else:
            self.__sound = mixer.Sound(audio)
        self.__sensitivity = self.__class__.SENSITIVITY_HIGH
        self.AlarmPlaying = False
        self.score = 0
        self.Interrupt = False
        self.ScoreChecker = Timer(interval=1,function=self.check_score)
        self.ScoreChecker.start()

    def check_score(self):
        print(self.score)
        if self.score == self.__sensitivity and not self.AlarmPlaying:
            self.play_sound()
        elif self.score < self.__sensitivity:
            self.stop_sound()
        if not self.Interrupt:
            self.ScoreChecker = Timer(interval=1, function=self.check_score)
            self.ScoreChecker.start()

    def setSensitivity(self,sensitivity):
        if isinstance(sensitivity,int):
            self.__sensitivity = sensitivity

    def handle_sound(self,open_eyes):
        if open_eyes == 0:
            self.score  = min(self.__sensitivity,self.score + 1)
        else:
            self.score = max(0,self.score - 1)


    def play_sound(self):
          self.__sound.play(loops=-1)
          self.AlarmPlaying = True


    def stop_sound(self):
        self.__sound.stop()
        self.AlarmPlaying = False


    def interrupt(self):
        self.Interrupt = True




