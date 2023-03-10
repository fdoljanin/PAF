import numpy as np
import matplotlib.pyplot as plt

from lib import *

G = np.array([0, -9.81, 0])
velocity, degAngle = map(int, input(
    "Unesi brzinu i kut odvojene razmakom:\t").split())
radAngle = np.deg2rad(degAngle)

initialSpeed = velocity * np.array([np.cos(radAngle), np.sin(radAngle), 0])
initialPosition = np.array([0, 0, 0])
initialConditions = (initialSpeed, initialPosition)
getBodyStateUpdate = getUpdater(
    lambda a, v, x: G, initialConditions)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
axes[0].set(title="y/x", xlabel="x[m]", ylabel="y[m]")
axes[1].set(title="x/t", xlabel="t[s]", ylabel="x[m]")
axes[2].set(title="y/t", xlabel="t[s]", ylabel="y[m]")

TIME, APPROXIS = 10, 300
dt = TIME/APPROXIS
for currentTime in np.linspace(0, TIME, APPROXIS):
    a, v, r = getBodyStateUpdate(dt)
    axes[0].plot(r[0], r[1], 'bo', ms=3)
    axes[1].plot(currentTime, r[0], 'bo', ms=3)
    axes[2].plot(currentTime, r[1], 'bo', ms=3)

fig.savefig('plots/plot_2.pdf')
