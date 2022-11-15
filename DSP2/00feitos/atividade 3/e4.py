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


def doublesp(x):
    ds = np.array([])
    for i in range(0,x.size-1):
        mean = (x[i]+x[i+1])/2
        ds = np.append(ds,[x[i],mean])
    ds = np.append(ds,x[i+1]) 
    return ds
x=np.array([7, 3, 9, 1, 0, 4])
result=doublesp(x)
print(result)
