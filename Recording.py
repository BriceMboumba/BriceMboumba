import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import serial
import math
import os.path
from threading import Timer
import os # contient la méthode startfile() pour lancer un exécutable
import win32com.client, pythoncom # pour utiliser les objets COM
#import win32api # contient la méthode PostQuitMessage() permettant d'envoyer le message WM_QUIT
                # pour arrêter le script (existe aussi dans le module win32gui)
import pyaudio
import wave
from scipy import signal
from scipy.signal import filtfilt
import librosa
import librosa.display
from matplotlib.pyplot import *
from numpy.fft import fft
import scipy.io.wavfile



#GlobalNameFile Function
def GlobalNameFile():
    global WAVE_OUTPUT_FILENAME
    WAVE_OUTPUT_FILENAME = str(input("Veuillez entrer le nom du fichier, ex: toto.wav\n"))


GlobalNameFile()

#GlobalTime Function
def GlobalTime():
    global RECORD_SECONDS
    RECORD_SECONDS = int(input("Veuillez entrer la durée d'enregistrement (en secondes)\n"))


GlobalTime()

    #Recording
def Rec():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16  # paInt8
    CHANNELS = 2
    RATE = 44100  # sample rate
    record_seconds = RECORD_SECONDS
    wave_file_output_file_name = WAVE_OUTPUT_FILENAME

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)  # buffer

    print("Enregistrement en cours...")

    frames = []

    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)  # 2 bytes(16 bits) per channel

    print("Enregistrement fait!")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(wave_file_output_file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    verified = wf.close()

    #Temporal Spectrum
def Temporal():
    audio_wave_file = WAVE_OUTPUT_FILENAME
    sample_rate, data = librosa.load(audio_wave_file, sr=None)

    print('Audio signal shape:', sample_rate.shape)
    print('Sampling rate: {} Hz'.format(data))
    librosa.display.waveplot(sample_rate, sr=data)
    plt.grid(True)

    plt.ylabel('Pression acoustique [Pa]')
    plt.xlabel('t(s)')
    plt.grid(True)
    plt.show()

    # Fast Fourier Transform
def Spectrum():
    rate, data = scipy.io.wavfile.read(WAVE_OUTPUT_FILENAME)
    n = data.size
    duree = 1.0 * n / rate
    def tracerSpectre(data, rate, debut, duree):
        start = int(debut * rate)
        stop = int((debut + duree) * rate)
        spectre = np.absolute(fft(data[start:stop]))
        spectre = spectre / spectre.max()
        n = spectre.size
        freq = np.zeros(n)
        for k in range(n):
            freq[k] = 1.0 / n * rate * k
        plt.vlines(freq, [0], spectre, 'r')
        plt.xlabel('fréquence (Hz)')
        plt.ylabel('Amplitude')
        plt.axis([0, 0.5 * rate, 0, 1])
        plt.grid(True)

    plt.figure(figsize=(12, 4))
    tracerSpectre(data, rate, 0.0, RECORD_SECONDS)
    plt.axis([5000, 16000, 0, 1])
    show()


    #LowPass Filter Function

def LowPass():
    import matplotlib.pyplot as plt
    from scipy.io.wavfile import read
    from math import pi
    from scipy.io.wavfile import read as read_wav
    from thinkdsp import read_wave
    from thinkdsp import Wave
   # from thinkdsp import decorate

    # LowPass Filter Function definition
    def sample(wave, factor):
        ys = np.zeros(len(wave))
        ys[::factor] = wave.ys[::factor]
        return Wave(ys, framerate=wave.framerate)

    wave = read_wave(WAVE_OUTPUT_FILENAME)
    sampled = sample(wave, 4)  # filter order : 4
    # Plot LowPass Filter
    spectrum = sampled.make_spectrum(full=True)
    spectrum.low_pass(10000, 5)
    #spectrum.make_audio()
    spectrum.plot()
    grid(True)
    show()
    #decorate(xlabel='Frequency (Hz')


#Band_Stop or BandPass
def Band_Pass():
    from scipy.io import wavfile
    from scipy import signal
    import numpy as np
    from scipy.signal import butter, lfilter

    lo, hi = 188.5, 1635.6
    sr, y = wavfile.read(WAVE_OUTPUT_FILENAME)
    b, a = butter(N=6, Wn=[2 * lo / sr, 2 * hi / sr], btype='band')
    x = lfilter(b, a, y)
   # sounddevice.play(x, sr)
    wavfile.write('test2.wav', sr, x.astype(np.int16))

    audio_wave_file = 'test2.wav'
    sample_rate, data = librosa.load(audio_wave_file, sr=None)

    print('Audio signal shape:', sample_rate.shape)
    print('Sampling rate: {} Hz'.format(data))
    librosa.display.waveplot(sample_rate, sr=data)
    plt.grid(True)
    plt.ylabel('Pression acoustique [Pa]')
    plt.xlabel('t(s)')
    plt.grid(True)
    plt.show()


