##############################################
#                                            #
#    Jan Kwinta                02.01.2023    #
#                                            #
#    Metody Numeryczne                       #
#                                            #
#    Zadanie 11. Wzór trapezów               #
#                                            #
##############################################

import numpy as np

def f(x):
    return (np.sin( np.pi * ((1 + np.sqrt(x))/(1 + x**2) )) * np.exp(-x))

def metodaTrapezow():
    increment = (20 / (2**18))
    trapezy = f(0) + f(20)
    j = increment
    while j < 20:
        trapezy += 2 * f(j)
        j += increment
    trapezy *= increment
    trapezy /= 2
    return trapezy

print(metodaTrapezow())