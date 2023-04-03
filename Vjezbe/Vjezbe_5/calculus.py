from enum import Enum
import numpy as np


__all__ = ["MethodType", "Function"]


class MethodType(Enum):
    CENTER = 'center'
    UPPER = 'upper'
    LOWER = 'lower'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Function:
    def __init__(self, f):
        self.f = f

    def derivate(self, x, h, method=MethodType.CENTER):
        if method == MethodType.CENTER:
            return self.__derivate_center(x, h)
        if method == MethodType.UPPER:
            return self.__derivate_upper(x, h)
        if method == MethodType.LOWER:
            return self.__derivate_lower(x, h)

    def derivate_range(self, left, right, h, samples=1000, method=MethodType.CENTER):
        return [Point(x, self.derivate(x, h, method)) for x in np.linspace(left, right, samples)]

    def integrate_rectangular(self, left, right, samples=1000):
        space = np.linspace(left, right, samples+1)
        dx = (right-left)/samples

        leftSum = 0
        rightSum = 0

        for i in space[:-1]:  # 2 loops can be 1, but this is just a demo
            leftSum += self.f(i)

        for i in space[1:]:
            rightSum += self.f(i)

        return (leftSum*dx, rightSum*dx)

    def integrate_trapezoidal(self, left, right, samples=1000):
        space = np.linspace(left, right, samples+1)
        dx = (right-left)/samples
        sum = 0

        for x in space[1:-1]:
            sum += self.f(x)
        sum += (self.f(left) + self.f(right))/2

        return sum*dx

    def __derivate_upper(self, x, h):
        return (self.f(x + h) - self.f(x)) / h

    def __derivate_lower(self, x, h):
        return (self.f(x) - self.f(x - h)) / h

    def __derivate_center(self, x, h):
        return (self.f(x + h) - self.f(x - h)) / (2 * h)
