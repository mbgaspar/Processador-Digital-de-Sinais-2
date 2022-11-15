######################################################
##  Created on: Abril 26, 2022
##      Author: Marcelo Brancalhão Gaspar
##      Instituto Federal de Santa Catarina
##      DSP 2 - Fernando Santana Pacheco
##
######################################################
import numpy as np
from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.signal import chirp
x = [10,3,-3,3,8,1,-2]
array = np.array(x)
a = [1]
b = [0.5,0.5]
y = signal.lfilter(b, a, array)
print('x = ', array)
b4 = [0.25,0.25,0.25,0.25]
a4 = [1]
y4 = signal.lfilter(b4,a4,array)
print('y2 = ', y)
print('y4 = ', y4)
fs = 44100
t = np.linspace(0,1,fs)
sweep = chirp(t,100,1,1000)
plt.plot(t,sweep)
plt.show()
wavfile.write("sweep.wav",fs , sweep)
filtered=signal.lfilter(b4,a4,sweep)
wavfile.write("sweepfilter.wav",fs , filtered)