##############################################
#                                            #
#    Jan Kwinta                12.12.2022    #
#                                            #
#    Metody Numeryczne                       #
#                                            #
#    Zadanie 7. Wzor interpolacyjny          #
#               Lagrange'a                   #
#                                            #
##############################################

import matplotlib.pyplot as plt
import numpy as np

points = np.array([-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
f = np.array([1.13092041015625, 2.3203125, 1.92840576171875, 1, 0.05548095703125, -0.6015625, -0.75250244140625, 0])

# interpolacja wzorem Lagrange'a
def lagrange(x):
    result = 0
    for i in range(8):
        nominator = 1
        denominator = 1
        for j in range(8):
            if j != i:
                nominator *= x - points[j]
                denominator *= points[i] - points[j]
        result += f[i] * (nominator / denominator)
    return result  

# wielomian wprost
def polynomial(x):
    return x**7 - x**6 + x**5 - 2*x**4 + 4*x**3 - 4*x + 1
    
x = np.linspace(-1.25, 1.25, 200)

plt.plot(x, lagrange(x), "g")
plt.scatter(points, f)
plt.title("Wielomian interpolacyjny")
plt.show()