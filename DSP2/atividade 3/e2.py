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
from scipy.io import wavfile

def tonegen(freq,duration=0.1,amp=1, fs=8000):
    t = np.linspace(0., duration, int(fs*duration))
    x = amp*(np.sin(2*np.pi*freq*t))
    
    audio =x*(2**15 - 1) / np.max(np.abs(x))
    audio =audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()
    return x
  
def dtmfgen (seq_fone, tempo, intervalo, maxima):
    y = seq_fone[0]
    fs = 8000
    dtmf = {0: {'dtmf1': 941, 'dtmf2': 1336},
            1: {'dtmf1': 697, 'dtmf2': 1209},
            2: {'dtmf1': 697, 'dtmf2': 1336},
            3: {'dtmf1': 693, 'dtmf2': 1477},
            
            
            4: {'dtmf1': 770, 'dtmf2': 1209},
            5: {'dtmf1': 770, 'dtmf2': 1336},
            6: {'dtmf1': 770, 'dtmf2': 1477},
          
            7: {'dtmf1': 852, 'dtmf2': 1209},
            8: {'dtmf1': 852, 'dtmf2': 1336},
            9: {'dtmf1': 852, 'dtmf2': 1477},
           
            
            0: {'dtmf1': 941, 'dtmf2': 1336},
           
            }
    x = [0]
    for idx in range (len(seq_fone)):
        fr_1 = dtmf[int(seq_fone[idx])]['dtmf1']
        fr_2 = dtmf[int(seq_fone[idx])]['dtmf2']
        x_dtmf = tonegen(fr_1, tempo, maxima/2, fs) + tonegen(fr_2, tempo, maxima/2, fs)
        x_dtmf = np.concatenate((x_dtmf, np.zeros(int(intervalo*fs))))
        x = np.concatenate((x, x_dtmf))
    audio = x * (2**15 - 1) / np.max(np.abs(x))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()
    
    return x

s981 = dtmfgen(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 0.1, 40e-3, 0.7)
plt.plot(s981, 'bo', s981, 'k')