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
print('x = ', array)
b4 = [0.25,0.25,0.25,0.25]
a4 = [1]
y4 = signal.lfilter(b4,a4,array)
print('y2 = ', y)
print('y4 = ', y4)
plt.plot(x,'r',x,'or',y4,'--k',y4,'ok')
f2w=2*np.pi
fs4,h4 = signal.freqz(b4, fs=f2w*44100)
fig, ax = plt.subplots()
ax.set_title('Resposta em frequência')
ax.plot(fs4/(f2w), 20 * np.log10(abs(h4)))
ax.plot(fs/(f2w),20*np.log10(abs(h)))
ax.set_ylabel('Amplitude [dB]')
ax.set_xlabel('Frequency [Hz]')
plt.grid()
plt.show() 