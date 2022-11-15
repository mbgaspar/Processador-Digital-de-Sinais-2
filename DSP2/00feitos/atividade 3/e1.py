######################################################
##  Created on: Abril 26, 2022
##      Author: Marcelo Brancalhão Gaspar
##      Instituto Federal de Santa Catarina
##      DSP 2 - Fernando Santana Pacheco
##
######################################################

import numpy as np
import matplotlib.pyplot as plt
import simpleaudio as sa


def tonegen(freq,duration=0.1,amp=1, fs=8000):
    t = np.linspace(0., duration, int(fs*duration))
    x = amp*(np.sin(2*np.pi*freq*t))
    audio = x*(2**15 - 1) / np.max(np.abs(x))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()
    return x


s440 = tonegen(80, 0.1, 0.8, 8000)

plt.plot(s440)
plt.show()

