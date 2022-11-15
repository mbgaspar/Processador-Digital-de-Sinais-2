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
    
    audio = x*(2**15 - 1) / np.max(np.abs(x))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()
    return x

fs,x = wavfile.read('voz.wav')

plt.plot(x)
plt.show()

def halfsp(array):
    hs = array[0::2]
    return hs

result=halfsp(x)
plt.plot(x)
plt.show()






np.fliplr(x)
plt.plot(x)
plt.show()

np.flipud(x)
plt.plot(x)
plt.show()


def doublesp(x):
    ds = np.array([])
    for i in range(0,x.size-1):
        mean = (x[i]+x[i+1])/2
        ds = np.append(ds,[x[i],mean])
    ds = np.append(ds,x[i+1]) 
    return ds
result=doublesp(x)
plt.plot(x)
plt.show()