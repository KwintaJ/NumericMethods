##############################################
#                                            #
#    Jan Kwinta                18.12.2022    #
#                                            #
#    Metody Numeryczne                       #
#                                            #
#    Zadanie 9. Interpolacja splajnem        #
#               kubicznym                    #
#                                            #
##############################################

from scipy import interpolate 
from matplotlib import pyplot as plt
import numpy as np

points = np.array([-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
f = np.array([1.13092041015625, 2.3203125, 1.92840576171875, 1, 0.05548095703125, -0.6015625, -0.75250244140625, 0])

tck = interpolate.CubicSpline(points, f)

for i in range(7):
    print("W przedziale [" + str(tck.x[i]) + ", " + str(tck.x[i + 1]) +"]:")
    print("    " + str(tck.c[0, i]) + " * (x - " + str(tck.x[i]) + ")^3 + " + str(tck.c[1, i]) + " * (x - " + str(tck.x[i]) + ")^2 + " + str(tck.c[2, i]) + " * (x - " + str(tck.x[i]) + ") + " + str(tck.c[3, i]) + "\n")

def spline(x):
    return tck(x)

x = np.linspace(-0.75, 1, 200)

plt.plot(x, spline(x), "g")
plt.scatter(points, f)
plt.title("Interpolacja splajnem kubicznym")
plt.show()