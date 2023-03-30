import numpy as np
from particle import *

p = Particle(np.array([0, 0, 0], dtype='float64'), 10, 60)
dt_list = np.logspace(-4, 1, 1000)
plot_error_for_dt(p, dt_list, xscale='log', yscale='log')
