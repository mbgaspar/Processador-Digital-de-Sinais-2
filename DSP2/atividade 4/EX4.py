######################################################
##  Created on: Abril 26, 2022
##      Author: Marcelo Brancalhão Gaspar
##      Instituto Federal de Santa Catarina
##      DSP 2 - Fernando Santana Pacheco
##
######################################################
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
x = [10,3,-3,3,8,1,-2]
array = np.array(x)
a = [1]
b = [0.5,0.5]
y = signal.lfilter(b, a, array)
f2w = 2*np.pi
fs,h = signal.freqz(b, fs=f2w*44100)
k = np.linspace(0,1,44100)
tom = 1.5*(np.sin(f2w*17000*k))
plt.xlim(0,0.0001)
plt.plot(k,tom,'*r')
plt.plot(k,tom,'--k')
plt.xlabel('Angle [rad]')
plt.ylabel('sin(k)')
plt.show()
y = signal.lfilter(b,a,tom)
ffty = np.fft.fft(y)
n = ffty.size
freq = np.fft.fftfreq(n, 1/44100)
plt.xlim(0,20000)
plt.plot(freq,abs(ffty)*2/44100)
plt.show()
