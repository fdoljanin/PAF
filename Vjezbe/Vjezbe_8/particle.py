from lib import MovableObject
import numpy as np

__all__ = ['ChargedParticle']


class ChargedParticle(MovableObject):
    def __init__(self, mass, charge, initial_position, initial_velocity):
        self.mass = mass
        self.charge = charge

        super().__init__(initial_position, initial_velocity)

    def _get_acceleration(self, electric_field, magnetic_field, **_):
        return self.charge * (electric_field + np.cross(self.velocity, magnetic_field)) / self.mass

    def get_graph(self, dt, time_observed, magnetic_field, electric_field):
        p = []
        v = []
        t = []
        time_max = self.time + time_observed
        while self.time < time_max:
            self._move_runge_kutta(
                dt, electric_field=electric_field, magnetic_field=magnetic_field)
            p.append(self.position.copy())
            v.append(self.velocity.copy())
            t.append(self.time)

        return p, v, t
