from abc import ABC, abstractmethod

__all__ = ['MovableObject']


class MovableObject(ABC):
    def __init__(self, initial_position, initial_velocity, initial_time=0):
        self.position = initial_position
        self.velocity = initial_velocity
        self.time = initial_time

    @abstractmethod
    def get_acceleration(self, **kwargs):
        pass

    def move_euler(self, dt, **kwargs):
        self.velocity += self.get_acceleration(**kwargs) * dt
        self.position += self.velocity * dt
        self.time += dt

    def move_runge_kutta(self, dt, **kwargs):
        order_weight = [1/6, 2/6, 2/6, 1/6]
        k_v, k_p = self.get_acceleration(**kwargs) * dt, self.velocity * dt
        diff_v, diff_p = k_v * order_weight[0], k_p * order_weight[0]

        for i in range(1, 4):
            k_v, k_p = self.get_acceleration(
                position=self.position + k_p / 2, velocity=self.velocity + k_v / 2, time=self.time + dt / 2, **kwargs) * dt, (self.velocity + k_v / 2) * dt

            diff_v += k_v * order_weight[i]
            diff_p += k_p * order_weight[i]

        self.velocity += diff_v
        self.position += diff_p
        self.time += dt
