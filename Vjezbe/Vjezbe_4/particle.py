import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

__all__ = ["Particle", "plot_error_for_dt"]


class Particle:
    def __init__(self, position, speed, deg_angle):
        self.position = position
        self.velocity = self.__get_velocity_from_speed(speed, deg_angle)
        self.dt = 0.01

    def reset(self):
        self.position = np.zeros(3, dtype='float64')
        self.velocity = np.zeros(3, dtype='float64')

    def range(self):
        self_copy = deepcopy(self)
        self_copy.move_till_ground()

        x_diff = self_copy.position[0] - self.position[0]
        return x_diff

    def move_till_ground(self, position_snapshots=False):
        g = np.array([0, -9.81, 0])
        position_list = []

        while self.position[1] >= 0:
            self.__move(self.dt, g)

            if position_snapshots:
                position_list.append(self.position.copy())

        return position_list or None

    def plot_trajectory(self):
        position_list = self.move_till_ground(position_snapshots=True)
        x_list = [p[0] for p in position_list]
        y_list = [p[1] for p in position_list]

        plt.setp(plt.gca(), xlabel='x', ylabel='y', title='Trajectory')
        plt.plot(x_list, y_list)
        plt.show()

    def get_analytical_range(self):
        g = 9.81
        y, vx, vy = self.position[1], self.velocity[0], self.velocity[1]
        return vx * (vy/g + np.sqrt(2*(y+vy**2/(2*g))/g))

    def __move(self, dt, acceleration=np.zeros(3)):
        self.velocity += dt * acceleration
        self.position += dt * self.velocity

    @staticmethod
    def __get_velocity_from_speed(speed, deg_angle):
        rad_angle = np.deg2rad(deg_angle)
        return speed * np.array([np.cos(rad_angle), np.sin(rad_angle), 0])


def plot_error_for_dt(p, dt_list, **kwargs):
    error_list = []

    for dt in dt_list:
        p.dt = dt

        analytical_range = p.get_analytical_range()
        numerical_range = p.range()

        error = abs(analytical_range - numerical_range)
        error_list.append(error)

    plt.setp(plt.gca(), xlabel='dt', ylabel='error',
             title='Error for dt', **kwargs)
    plt.plot(dt_list, error_list)
    plt.show()
