import numpy as np
import matplotlib.pyplot as plt
from calculus import *

LEFT, RIGHT, SAMPLE_NUMBER = -10, 10, np.logspace(2, 5, 30, dtype=int)
fun = Function(lambda x: x**2+2*x+np.sin(x))


def funIntegralAnalytic(x): return 1/3*x**3 + x**2 + -np.cos(x)


funIntegralValueAnalytic = funIntegralAnalytic(
    RIGHT) - funIntegralAnalytic(LEFT)
funValuesNumericLeft = []
funValuesNumericRight = []
funValuesNumericTrapez = []

for sn in SAMPLE_NUMBER:
    numericLeft, numericRight = fun.integrate_rectangular(LEFT, RIGHT, sn)
    numericTrapez = fun.integrate_trapezoidal(LEFT, RIGHT, sn)

    funValuesNumericLeft.append(numericLeft)
    funValuesNumericRight.append(numericRight)
    funValuesNumericTrapez.append(numericTrapez)

plt.setp(plt.gca(), xscale='log')

plt.plot(SAMPLE_NUMBER, funValuesNumericLeft, 'ro', label='left', )
plt.plot(SAMPLE_NUMBER, funValuesNumericRight, 'bo', label='right')
plt.plot(SAMPLE_NUMBER, funValuesNumericTrapez, 'go', label='trapez')
plt.plot(SAMPLE_NUMBER, [funIntegralValueAnalytic]
         * len(SAMPLE_NUMBER), label='analytic')

plt.show()
