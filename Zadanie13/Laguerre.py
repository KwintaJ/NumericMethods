##############################################
#                                            #
#    Jan Kwinta                22.01.2023    #
#                                            #
#    Metody Numeryczne                       #
#                                            #
#    Zadanie 13. Szukanie miejsc zerowych    #
#                wielomianow                 #
#                                            #
##############################################

import numpy as np
import cmath

p_a = np.poly1d([243, -486, 783, -990, 558, -28, -72, 16])
p_b = np.poly1d([1, 1, 3, 2, -1, -3, -11, -8, -12, -4, -4])
p_c = np.poly1d([1, 0 + 1j, -1, 0 - 1j, 1])


def fG(P, x):
    der = np.polyder(P, m=1)
    return der(x) / P(x)
    

def fH(P, x):
    der = np.polyder(P, m=2)
    G = fG(P, x)
    Gsquared = np.polymul(G, G)
    return Gsquared - (der(x) / P(x))


def laguerre(p, x, error):
    n = p.order
    xk = x
    while abs(p(xk)) > error:
        G = fG(p, xk)
        H = fH(p, xk)
        denominatorMinus = G - cmath.sqrt((n - 1) * (n * H - G ** 2))
        denominatorPlus = G + cmath.sqrt((n - 1) * (n * H - G ** 2))
        denom = max([denominatorMinus, denominatorPlus], key=abs)
        a = (n / denom)
        xk -= a
    return xk


def smoothing(poly, x):
    newPoly = []
    n = poly.order
    oldPoly = poly.coeffs
    newPoly = np.append(newPoly, oldPoly[0])
    for i in range(1, n):
        newPoly = np.append(newPoly, oldPoly[i] + x * newPoly[i - 1])
    return newPoly


def roots(p):
    pRoots = []
    p_k = p
    while (p_k.order > 0):
        x_k = laguerre(p_k, 0, 1e-12)
        pRoots = np.append(pRoots, x_k)
        newP = np.poly1d(smoothing(p_k, x_k))
        p_k = newP
    return pRoots


print(p_a)
print(roots(p_a))
print("\n")

print(p_b)
print(roots(p_b))
print("\n")

print(p_c)
print(roots(p_c))
print("\n")

