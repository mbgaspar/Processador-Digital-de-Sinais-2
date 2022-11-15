######################################################
##
##  Created on: Abril 26, 2022
##      Author: Marcelo Brancalhão Gaspar
##      Instituto Federal de Santa Catarina
##      DSP 2 - Fernando Santana Pacheco
##
######################################################
import numpy as np
import matplotlib.pyplot as plt
import simpleaudio as sa
import math as math

from scipy.io import wavfile

def tonegen(freq,duration=0.1,amp=1, fs=8000):
    t = np.linspace(0., duration, int(fs*duration))
    x = amp*(np.sin(2*np.pi*freq*t))
    
    audio =x*(2**15 - 1) / np.max(np.abs(x))
    audio =audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()
    return x

s440 = tonegen(80, 0.1, 0.8, 8000)
plt.plot(s440)
plt.show()

def echo(signal, attenuation, delay, fs):
     delayer = np.zeros(math.ceil (delay * fs))
     attSig = attenuation*signal
     delSin = np.append(delayer,attSig)
     sig = np.append(signal,delayer)
     return sig+delSin
  
fs,voz = wavfile.read('voz.wav')
  
echo1 = echo(voz, 0.65, 0.25, 8000)
plt.plot(echo1)
plt.show()

echo2 = echo(voz, 0.5, 0.4, 8000)
plt.plot(echo2)
plt.show()

echo3 = echo(voz, 0.9, 1, 4000)
plt.plot(echo1)
plt.show()