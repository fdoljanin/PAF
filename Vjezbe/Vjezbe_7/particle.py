from lib import MovableObject
import matplotlib.pyplot as plt
import numpy as np

G = np.array([0, -9.81, 0])


class Air:
    def __init__(self, density, drag_coefficient):
        self.density = density
        self.drag_coefficient = drag_coefficient


class Particle(MovableObject):
    def __init__(self, initialPosition, initialVelocity, mass, area):
        self.mass = mass
        self.area = area
        super().__init__(initialPosition, initialVelocity)

    def get_acceleration(self, **kwargs):
        air, velocity = kwargs.get('air'), kwargs.get('velocity')

        if velocity is None:
            velocity = self.velocity

        air_resistance = -0.5 * air.density * air.drag_coefficient * \
            self.area * np.linalg.norm(velocity) * velocity / self.mass

        return G + air_resistance

    def get_graph(self, time_observed, move_method):
        p = []
        v = []
        t = []
        time_max = self.time + time_observed

        while self.time < time_max:
            move_method()
            p.append(self.position.copy())
            v.append(self.velocity.copy())
            t.append(self.time)

        return p, v, t

    def get_euler_graph(self, air, dt, time_observed):
        return self.get_graph(time_observed, lambda: self.move_euler(dt, air=air))

    def get_runge_kutta_graph(self, air, dt, time_observed):
        return self.get_graph(time_observed, lambda: self.move_runge_kutta(dt, air=air))


air = Air(1.225, 0.47)
p1 = Particle(np.array([0, 0, 0], dtype=np.float64),
              np.array([10, 100, 0], dtype=np.float64), 1, 1)

p2 = Particle(np.array([0, 0, 0], dtype=np.float64),
              np.array([10, 100, 0], dtype=np.float64), 1, 1)

x1, v1, t1 = p1.get_euler_graph(air, 0.01, 10)
x2, v2, t2 = p2.get_runge_kutta_graph(air, 0.01, 10)

plt.plot(t1, list(map(lambda x: x[0], x1)), 'r', label="Euler")
plt.plot(t2, list(map(lambda x: x[0], x2)), 'b', label="Runge-Kutta")
plt.show()
