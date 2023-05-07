from lib import MovableObject
import numpy as np

__all__ = ['Air', 'Particle']

G = np.array([0, -9.81, 0])


class Air:
    def __init__(self, density, drag_coefficient):
        self.density = density
        self.drag_coefficient = drag_coefficient


class Particle(MovableObject):
    def __init__(self, initial_position, initial_velocity, mass, area):
        self.mass = mass
        self.area = area
        super().__init__(initial_position, initial_velocity)

    def get_acceleration(self, air, velocity=None, **_):
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
