import numpy as np
import matplotlib.pyplot as plt
from calculus import *

LEFT, RIGHT, DX, SAMPLES = -10, 10, 0.01, 100


def decomposePoints(points):
    return [p.x for p in points], [p.y for p in points]


functionCubic = Function(lambda x: x**3 - 2*x**2 + 4*x - 8)
functionTrigonometric = Function(lambda x: np.sin(x))

functionCubicDerivateNumeric = functionCubic.derivate_range(
    LEFT, RIGHT, DX, SAMPLES, MethodType.CENTER)
functionTrigonometricDerivateNumeric = functionTrigonometric.derivate_range(
    LEFT, RIGHT, DX, SAMPLES, MethodType.CENTER)
cubicDerivateNumericX, cubicDerivateNumericY = decomposePoints(
    functionCubicDerivateNumeric)
trigonometricDerivateNumericX, trigonometricDerivateNumericY = decomposePoints(
    functionTrigonometricDerivateNumeric)


def functionCubicDerivate(x): return 3*x**2 - 4*x + 4
def functionTrigonometricDerivate(x): return np.cos(x)


plot_range = np.linspace(LEFT, RIGHT, SAMPLES)
cubicDerivateAnalytic = functionCubicDerivate(plot_range)
trigonometricDerivateAnalytic = functionTrigonometricDerivate(plot_range)

fig, axes = plt.subplots(1, 2, figsize=(14, 4))
axes[0].set_title("d(x^3-2x^2+4^x-8)/dx")
axes[1].set_title("d(sin(x))/dx")

axes[0].plot(plot_range, cubicDerivateAnalytic, 'r', label='analytic')
axes[0].plot(cubicDerivateNumericX,
             cubicDerivateNumericY, 'ro', label='numeric')
axes[1].plot(plot_range, trigonometricDerivateAnalytic, 'b', label='analytic')
axes[1].plot(trigonometricDerivateNumericX,
             trigonometricDerivateNumericY, 'bo', label='numeric')

plt.show()
