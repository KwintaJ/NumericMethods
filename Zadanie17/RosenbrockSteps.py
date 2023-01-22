##############################################
#                                            #
#    Jan Kwinta                16.01.2023    #
#                                            #
#    Metody Numeryczne                       #
#                                            #
#    Zadanie 17. Liczenie krokow             #
#                wykonywanych przez metode   #
#                Levenberga–Marquardta       #
#                                            #
##############################################

import numpy as np

minX = -2.0
maxX = 2.0

minY = -1.0
maxY = 3.0

def Rosenbrock(x, y):
    return (1.0 - x) ** 2 + 100 * (y - x ** 2) ** 2


def Hessian(x, y, L):
    H_11 = (1 + L) * (2.0 - 400.0 * y + 1200.0 * x ** 2)
    H_12 = -400.0 * x
    H_21 = -400.0 * x
    H_22 = (1 + L) * 200.0
    return [[H_11, H_12], [H_21, H_22]]


def gradient(x, y):
    gradientX = -2.0 * (1.0 - x) - 400.0 * (y - x ** 2) * x
    gradientY = 200.0 * (y - x ** 2)
    return [gradientX, gradientY]


def LevenbergMarquardt(X, Y):
    l = 2 ** (-10)
    print("Punkt poczatkowy: " + str(X) + ", " + str(Y))
   
    numOfSteps = 0
    error = 1
    
    while(error > (10 ** (-7))):
        S = np.linalg.solve(Hessian(X, Y, l), gradient(X, Y))
        estimationX = X - S[0]
        estimationY = Y - S[1]
        if(Rosenbrock(estimationX, estimationY) > Rosenbrock(X, Y)):
            l *= 8
        else:
            numOfSteps += 1
            l /= 8
            
            error = np.linalg.norm([X - estimationX, Y - estimationY])
            X = estimationX
            Y = estimationY
            
    print("Liczba krokow potrzebna do oszacowania minimum: " + str(numOfSteps) + "\n")
    return numOfSteps
    
allSteps = 0 
numOfLoops = 20

for i in range(numOfLoops):
    randomX = np.random.uniform(minX, maxX)
    randomY = np.random.uniform(minY, maxY)
    
    allSteps += LevenbergMarquardt(randomX, randomY)
    
print("Srednia liczba krokow: " + str(allSteps / numOfLoops))
