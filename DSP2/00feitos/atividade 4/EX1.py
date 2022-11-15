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
print(y)
plt.plot(y,'-',y,'ok',x,'r',x,'*k')
plt.show()