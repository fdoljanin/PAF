import numpy as np

G = 6.67 * 10**(-11)


class Body:
    def __init__(self, m, r0, v0):
        self.m = m
        self.r = r0
        self.v = v0

    def step(self, acceleration, dt):
        self.v += acceleration*dt
        self.r += self.v*dt


class BodySystem:
    def __init__(self, bodies):
        self.bodies = bodies

    def get_graph(self, dt, t_max):
        r_bodies = [[] for _ in self.bodies]
        time = 0
        timestamps = []

        while time < t_max:
            self.step(dt)

            for i, b in enumerate(self.bodies):
                r_bodies[i].append(b.r.copy())

            timestamps.append(time)
            time += dt

        return timestamps, r_bodies

    def step(self, dt):
        accelerations = [self.__getFieldForBody(b) for b in self.bodies]

        for b, a in zip(self.bodies, accelerations):
            b.step(a, dt)

    def __getFieldForBody(self, observed):
        otherBodies = filter(lambda b: b != observed, self.bodies)
        totalField = np.zeros(3, dtype=np.float64)

        for body in otherBodies:
            totalField += -G * body.m * \
                (observed.r - body.r) / np.linalg.norm(observed.r - body.r)**3

        return totalField
