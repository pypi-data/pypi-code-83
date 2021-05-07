# -*- coding:utf-8 -*-
from __future__ import print_function

import os
import time
import wave
import numpy as np
import alsaaudio


class Audio(object):
    def __init__(self):
        self.CHANNELS = 1  # 通道数
        self.RATE = 16000  # 采样率
        self.THRESHOLD = 800  # 录音阈值

    def start_record(self, file_name):
        device = 'default'

        f = wave.open(file_name, 'wb')
        f.setnchannels(self.CHANNELS)
        f.setsampwidth(2)  # PCM_FORMAT_S16_LE
        f.setframerate(self.RATE)

        inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, device=device,
                            format=alsaaudio.PCM_FORMAT_S16_LE, channels=self.CHANNELS, rate=self.RATE, periodsize=160)

        print('%d channels, %d sampling rate\n' % (f.getnchannels(), f.getframerate()))
        recording = False
        frames = []
        # 遗弃前12帧
        for i in range(0, 8):
            l, data = inp.read()
            time.sleep(.051)

        while (True):
            if not recording:
                print('检测中... ')
                # 采集小段声音
                frames = []
                for i in range(0, 4):
                    l, data = inp.read()
                    if l > 0:
                        time.sleep(.001)
                        frames.append(data)
                audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
                large_sample_count = np.sum(audio_data >= self.THRESHOLD * 0.6)
                time.sleep(.051)
                # 如果有符合条件的声音，则开始录制
                if large_sample_count >= self.THRESHOLD * 0.8:
                    print("检测到信号")
                    recording = True
                print(large_sample_count)
            else:
                nowavenum = 0
                while True:
                    print("持续录音中...")
                    subframes = []
                    for i in range(0, 5):
                        l, data = inp.read()
                        if l > 0:
                            time.sleep(.001)
                            subframes.append(data)
                            frames.append(data)
                    audio_data = np.frombuffer(b''.join(subframes), dtype=np.int16)
                    if audio_data.size != 0:
                        temp = np.max(audio_data)
                        if temp <= self.THRESHOLD * 0.8:
                            nowavenum += 1
                        else:
                            nowavenum = 0

                        if nowavenum >= 2:
                            print("等待超时，开始保存")
                            frames.pop()
                            f.writeframes(b''.join(frames))
                            f.close()
                            return file_name

    def play_wav(self, file_name):
        # 只读方式打开wav文件
        wf = wave.open(file_name, 'rb')

        print('%d channels, %d sampling rate\n' % (wf.getnchannels(),
                                                   wf.getframerate()))
        periodsize = int(wf.getframerate() / 8)
        # 8bit is unsigned in wav files
        if wf.getsampwidth() == 1:
            device = alsaaudio.PCM(device="default", channels=wf.getnchannels(), rate=wf.getframerate(),
                                   format=alsaaudio.PCM_FORMAT_U8, periodsize=periodsize)
        # Otherwise we assume signed data, little endian
        elif wf.getsampwidth() == 2:
            device = alsaaudio.PCM(device="default", channels=wf.getnchannels(), rate=wf.getframerate(),
                                   format=alsaaudio.PCM_FORMAT_S16_LE,  periodsize=periodsize)
        elif wf.getsampwidth() == 3:
            device = alsaaudio.PCM(device="default", channels=wf.getnchannels(), rate=wf.getframerate(),
                                   format=alsaaudio.PCM_FORMAT_S24_LE, periodsize=periodsize)
        elif wf.getsampwidth() == 4:
            device = alsaaudio.PCM(device="default", channels=wf.getnchannels(), rate=wf.getframerate(),
                                   format=alsaaudio.PCM_FORMAT_S32_LE,  periodsize=periodsize)
        else:
            raise ValueError('Unsupported format')

        data = wf.readframes(int(periodsize))
        while data:
            # Read data from stdin
            device.write(data)
            data = wf.readframes(int(periodsize))
        wf.close()
        return

    def wav_to_pcm(self, wav_file):
        pcm_file = "%s.pcm" % (wav_file.split(".")[0])
        os.system("ffmpeg -y  -i %s  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s" % (
            wav_file, pcm_file))
        return pcm_file

    def play_pcm(self, pcm_file):
        # os.close(sys.stderr.fileno())
        with open(pcm_file, 'rb') as pcmfile:
            pcmdata = pcmfile.read()
        with wave.open('speach.wav', 'wb') as wavfile:
            wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
            wavfile.writeframes(pcmdata)
        self.play_wav('speach.wav')


if __name__ == "__main__":
    audio = Audio()
    filename = audio.start_record("speach.wav")
    time.sleep(1)
    audio.wav_to_pcm(filename)
