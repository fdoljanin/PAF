import numpy as np
import matplotlib.pyplot as plt

from lib import *

# TASK 1
force, mass = map(int, input("Unesi silu i masu odvojene razmakom:\t").split())
acc = force/mass
getBodyStateUpdate = getUpdater(lambda a, v, x: acc, (0, 0))

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
axes[0].set_title("a/t")
axes[1].set_title("v/t")
axes[2].set_title("s/t")

TIME, APPROXIS = 10, 200
dt = TIME/APPROXIS
for currentTime in np.linspace(0, TIME, APPROXIS):
    a, v, x = getBodyStateUpdate(dt)
    axes[0].plot(currentTime, a, 'bo', ms=3)
    axes[1].plot(currentTime, v, 'bo', ms=3)
    axes[2].plot(currentTime, x, 'bo', ms=3)

fig.savefig('plots/plot_1.pdf')
