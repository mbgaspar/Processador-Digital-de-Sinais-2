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

def halfsp(array):
    hs = array[0::2]
    return hs


x=np.array([7, 3, 9, 1, 0, 4])
result=halfsp(x)
print(result)
 