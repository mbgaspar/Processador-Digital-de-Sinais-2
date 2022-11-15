######################################################
##
##  Created on: Abril 26, 2022
##      Author: Marcelo Brancalhão Gaspar
##      Instituto Federal de Santa Catarina
##      DSP 2 - Fernando Santana Pacheco
##
######################################################
import simpleaudio as sa
import numpy as np
import matplotlib.pyplot as plt

def tonegen(freq,duration=0.1,amp=1, fs=8000):
    t = np.linspace(0., duration, int(fs*duration))
    x = amp*(np.sin(2*np.pi*freq*t))
    
    audio = x*(2**15 - 1) / np.max(np.abs(x))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()
    return x
 
s220 =tonegen(80, 0.1, 0.8, 8000)   
    


     
def doublesp(s220):
    ds = np.array([])
    for i in range(0,s220.size-1):
        mean = (s220[i]+s220[i+1])/2
        ds = np.append(ds,[s220[i],mean])
    ds = np.append(ds,s220[i+1]) 
    return ds

 
h220 = doublesp(s220)


plt.plot(s220,'bo', s220, 'k')
plt.grid()
plt.show()

plt.plot(h220,'bo', h220, 'k')
plt.grid()
plt.show()

plt.xlim(0,400)
plt.plot(s220,'k', h220, 'r')
plt.grid()
plt.show()

s220fft=np.fft.fft(s220)
ns=s220fft.size
fs=np.fft.fftfreq(ns,1/8000)
plt.xlim(0,500)
plt.plot(fs,abs(s220fft)/4000)
plt.show()
h220fft=np.fft.fft(h220)
nh=h220fft.size
fh=np.fft.fftfreq(nh,1/8000)
plt.plot(fh,abs(h220fft)/4000)
plt.show()

