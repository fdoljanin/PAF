from particle import *

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


air = Air(1.225, 0.47)
particle_1 = Particle(np.array([2, 3, 0], dtype=np.float64),
                      np.array([10, 80, 0], dtype=np.float64), 10, 10)
particle_2, particle_3 = deepcopy(particle_1), deepcopy(particle_1)

p_1, v_1, t_1 = particle_1.get_euler_graph(air, 0.01, 5)
p_2, v_2, t_2 = particle_2.get_euler_graph(air, 0.005, 5)
p_3, v_3, t_3 = particle_3.get_runge_kutta_graph(air, 0.01, 5)

x_1, x_2, x_3 = [p[0] for p in p_1], [p[0] for p in p_2], [p[0] for p in p_3]
y_1, y_2, y_3 = [p[1] for p in p_1], [p[1] for p in p_2], [p[1] for p in p_3]
vy_1, vy_2, vy_3 = [v[1] for v in v_1], [v[1]
                                         for v in v_2], [v[1] for v in v_3]

fig, axes = plt.subplots(1, 3, figsize=(14, 4))
axes[0].set_title("x/t")
axes[1].set_title("y/t")
axes[2].set_title("$v_y$/t")

axes[0].plot(t_1, x_1, 'b', label='Euler')
axes[0].plot(t_2, x_2, 'r', label='Euler (0.5dt)')
axes[0].plot(t_3, x_3, 'g', label='Runge-Kutta')
axes[0].legend()

axes[1].plot(t_1, y_1, 'b', label='Euler')
axes[1].plot(t_2, y_2, 'r', label='Euler (0.5dt)')
axes[1].plot(t_3, y_3, 'g', label='Runge-Kutta')
axes[1].legend()

axes[2].plot(t_1, vy_1, 'b', label='Euler')
axes[2].plot(t_2, vy_2, 'r', label='Euler (0.5dt)')
axes[2].plot(t_3, vy_3, 'g', label='Runge-Kutta')
axes[2].legend()

plt.show()
