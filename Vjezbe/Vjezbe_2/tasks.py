from lib import *
import matplotlib
import matplotlib.pyplot as plt

# TASK 1
force, mass = 10, 10  # map(int, input().split())
acc = force/mass
bodyStateUpdate = getUpdater(lambda a, v, x: acc, (0, 0, 0))

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
axes[0].set_title("a/t")
axes[1].set_title("v/t")
axes[2].set_title("s/t")

TIME, APPROXIS = 10, 100
dt = TIME/APPROXIS
for i in range(APPROXIS):
    currentTime = dt * i
    a, v, x = bodyStateUpdate(dt)
    axes[0].plot(currentTime, a, 'bo', ms=3)
    axes[1].plot(currentTime, v, 'bo', ms=3)
    axes[2].plot(currentTime, x, 'bo', ms=3)

fig.savefig('plot.pdf')
