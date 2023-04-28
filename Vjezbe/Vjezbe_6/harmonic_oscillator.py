from numpy import sign

__all__ = ["HarmonicOscillator"]


class HarmonicOscillator:
    def __init__(self, m, k, x0, v0):
        self.m = m
        self.k = k
        self.x = x0
        self.v = v0

    def step(self, dt):
        acceleration = -self.k/self.m*self.x
        self.x += self.v*dt
        self.v += acceleration*dt

    def get_graph(self, dt, t_max):
        x = []
        v = []
        a = []
        t = []
        t_curr = 0

        while t_curr < t_max:
            self.step(dt)
            x.append(self.x)
            v.append(self.v)
            a.append(-self.k/self.m*self.x)
            t.append(t_curr)

            t_curr += dt

        return x, v, a, t

    def get_period(self, dt):
        t = 0
        sign_change_counter = 0

        while True:
            prev = self.x
            self.step(dt)
            t += dt

            if sign(self.x) != sign(prev) and self.x:
                sign_change_counter += 1
                if sign_change_counter == 1:
                    t = 0

            if sign_change_counter == 2:
                return t*2
