import matplotlib.pyplot as plt
import numpy as np
from harmonic_oscillator import *

oscillator = HarmonicOscillator(1, 0.45, 1.1, 1.2)
real_period = 2*np.pi*np.sqrt(oscillator.m/oscillator.k)
dt_axe = np.logspace(-4, 1, 100)
err_axe = [np.abs(oscillator.get_period(dt)/real_period - 1) for dt in dt_axe]


plt.setp(plt.gca(), yscale="log", xscale="log", xlabel="dt", ylabel="error")
plt.plot(dt_axe, err_axe)
plt.show()
