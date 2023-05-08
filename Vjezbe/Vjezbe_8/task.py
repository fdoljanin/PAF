from particle import *

import numpy as np
import matplotlib.pyplot as plt

electron = ChargedParticle(-1, 2, np.array(
    [3, 4, 2], dtype=np.float64), np.array([3, 4, 2], dtype=np.float64))
positron = ChargedParticle(1, 2, np.array(
    [3, 4, 2], dtype=np.float64), np.array([3, 4, 2], dtype=np.float64))
electric_field = (0, 0, 0)
magnetic_field = (0, 0, 3)

p_el, v_el, t_el = electron.get_graph(0.001, 5, magnetic_field, electric_field)
p_po, v_po, t_po = positron.get_graph(0.001, 5, magnetic_field, electric_field)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_e, y_e, z_e = [p[0] for p in p_el], [p[1]
                                       for p in p_el], [p[2] for p in p_el]
x_p, y_p, z_p = [p[0] for p in p_po], [p[1]
                                       for p in p_po], [p[2] for p in p_po]

ax.plot(x_e, y_e, z_e, '-', label='electron')
ax.plot(x_p, y_p, z_p, '-', label='positron')

ax.set(xlabel='X', ylabel='Y', zlabel='Z', title='Path in EM field')
ax.legend()

plt.show()
