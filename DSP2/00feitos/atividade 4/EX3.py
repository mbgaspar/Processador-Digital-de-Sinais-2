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
fig, ax = plt.subplots()
ax.set_title('Resposta em frequência')
ax.plot(fs/(f2w), 20*np.log10(abs(h)))
ax.set_ylabel('Amplitude [dB]')
ax.set_xlabel('Frequency [Hz]')
plt.grid()
plt.show() 