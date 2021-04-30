import speech_recognition as sr
from threading import Thread
import pyttsx3
from .SoundManager import sound_manager


class CommandListener(Thread):

    def __init__(self, drowsiness_detector=None):
        super().__init__()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.drowsiness_detector = drowsiness_detector
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 200)
        self.engine.setProperty('volume', 1)
        self.engine.startLoop(False)
        self.interrupt = False

    def run(self):
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
        print("started")
        self.stop_listening = self.r.listen_in_background(self.m, self.callback)
        while not self.interrupt:
            continue
        self.engine.endLoop()

    def stop(self):
        self.stop_listening(wait_for_stop=False)
        self.interrupt = True

    def callback(self, recognizer, audio):
        try:
            text = recognizer.recognize_google(audio).split()
            print(text)
            if "sensitivity" and "low" in text:
                self.drowsiness_detector.setSensitivity(sound_manager.SENSITIVITY_LOW)
                self.speak("Ok low sensitivity set successfully")
            elif "sensitivity" and "medium" in text:
                self.drowsiness_detector.setSensitivity(sound_manager.SENSITIVITY_MEDIUM)
                self.speak("Ok medium sensitivity set successfully")
            elif "sensitivity" and "high" in text:
                self.drowsiness_detector.setSensitivity(sound_manager.SENSITIVITY_HIGH)
                self.speak("Ok high sensitivity set successfully")
            else:
                self.speak("Sorry could not understand you")
        except Exception as e:
            print(e)

    def speak(self, message):
        self.engine.say(message)
        self.engine.iterate()
        self.engine.endLoop()
        self.engine.startLoop(False)
        print("freed", self.engine.isBusy())
