import numpy as np
import matplotlib.pyplot as plt

from lib import *

__all__ = ["jednoliko_gibanje", "kosi_hitac"]

DEFAULT_FILE_TYPE = "png"
def getFilePath(name, extension): return f"{name}.{extension}"


def jednoliko_gibanje(force, mass, time, approximationCount, fileName, fileType=DEFAULT_FILE_TYPE):
    acc = force/mass
    getBodyStateUpdate = getUpdater(lambda a, v, x: acc, (0, 0))

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    axes[0].set_title("a/t")
    axes[1].set_title("v/t")
    axes[2].set_title("s/t")

    dt = time/approximationCount
    for currentTime in np.linspace(0, time, approximationCount):
        a, v, x = getBodyStateUpdate(dt)
        axes[0].plot(currentTime, a, 'bo', ms=3)
        axes[1].plot(currentTime, v, 'bo', ms=3)
        axes[2].plot(currentTime, x, 'bo', ms=3)

    fig.savefig(getFilePath(fileName, fileType))


def kosi_hitac(velocity, degAngle, time, approximationCount, fileName, fileType=DEFAULT_FILE_TYPE):
    G = np.array([0, -9.81, 0])
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

    dt = time/approximationCount
    for currentTime in np.linspace(0, time, approximationCount):
        a, v, r = getBodyStateUpdate(dt)
        axes[0].plot(r[0], r[1], 'bo', ms=3)
        axes[1].plot(currentTime, r[0], 'bo', ms=3)
        axes[2].plot(currentTime, r[1], 'bo', ms=3)

    fig.savefig(getFilePath(fileName, fileType))
