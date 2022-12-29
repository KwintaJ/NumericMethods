##############################################
#                                            #
#    Jan Kwinta                02.01.2023    #
#                                            #
#    Metody Numeryczne                       #
#                                            #
#    Zadanie 11. Metoda Romberga             #
#                                            #
##############################################

import numpy as np

def f(x):
    return (np.sin( np.pi * ((1 + np.sqrt(x))/(1 + x**2) )) * np.exp(-x))

def R0(i):
    increment = (20 / (2**i))
    trapezy = f(0) + f(20)
    j = increment
    while j < 20:
        trapezy += 2 * f(j)
        j += increment
    trapezy *= increment
    trapezy /= 2
    return trapezy

tablicaRomberga = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def R(m, i):
    if m == 0:
        return R0(i)
    R1 = 0
    R2 = 0
    
    if tablicaRomberga[m - 1][i + 1] != 0:
        R1 = tablicaRomberga[m - 1][i + 1]
    else:
        R1 = R(m - 1, i + 1)
        tablicaRomberga[m - 1][i + 1] = R1
        
    if tablicaRomberga[m - 1][i] != 0:
        R2 = tablicaRomberga[m - 1][i]
    else:
        R2 = R(m - 1, i)
        tablicaRomberga[m - 1][i] = R1

    return ((4**m * R1 - R2) / (4**m - 1))


print(R(5, 18))