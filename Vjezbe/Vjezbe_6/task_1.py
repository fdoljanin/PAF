import matplotlib.pyplot as plt
from harmonic_oscillator import *

oscillator = HarmonicOscillator(1, 1, 1.1, 0.0)

x_graph, v_graph, a_graph, t_graph = oscillator.get_graph(0.01, 10)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
axes[0].set_title("a/t")
axes[1].set_title("v/t")
axes[2].set_title("x/t")

axes[0].plot(t_graph, a_graph)
axes[1].plot(t_graph, v_graph)
axes[2].plot(t_graph, x_graph)
plt.show()
