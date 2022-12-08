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

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

points = np.array([-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
f = np.array([1.13092041015625, 2.3203125, 1.92840576171875, 1, 0.05548095703125, -0.6015625, -0.75250244140625, 0])
L0 = np.array([0, 0, 0, 0, 0, 0, 0, 0])

def polynomial(x):
    result = 0
    for i in range(8):
        nominator = 1
        denominator = 1
        for j in range(8):
            if j != i:
                nominator *= x - points[j]
                denominator *= points[i] - points[j]
        if(isinstance(x, int)):
            L0[i] = (nominator / denominator)
        result += f[i] * (nominator / denominator)
    return result  
    
x = np.linspace(-1.25, 1.25, 200)

plt.plot(x, polynomial(x), "g")
plt.scatter(points, f)

print(polynomial(0))
print(L0)

plt.show()