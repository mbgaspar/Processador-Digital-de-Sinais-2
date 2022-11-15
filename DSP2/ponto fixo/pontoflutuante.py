######################################################
##  Created on: maio 1, 2022
##      Author: Marcelo Brancalhão Gaspar
##      Instituto Federal de Santa Catarina
##      DSP 2 - Fernando Santana Pacheco
##
######################################################
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def soma(a, b):
    resultado = a + b
    return resultado

print(" xf\n yf\n rf\n")
print(" x15\n y15\n r15\n")

xf=0
print(float(xf))
yf=0
print(float(yf))
rf=0
print(float(rf))

x15=0
print(int(x15))
y15=0
print(int(y15))
r15=0
print(int(r15))

print("----")

##convertendo para ponto fixo
x15 = (int(xf*32768)); print(x15)

y15 = (int(xf*32768)); print(x15)

##fazendo as operações em ponto fixo
r15 = soma(x15,y15)
print(r15)

##voltando para o mundo float
rf = r15/float(32768)
print(rf)

