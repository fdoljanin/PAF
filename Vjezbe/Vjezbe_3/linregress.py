from arithm import getArithmeticMean


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def lmap(m, l): return list(map(m, l))


def getLineCoefficient(pairs):
    meanXY = getArithmeticMean(lmap(lambda p: p.x * p.y, pairs))
    meanX2 = getArithmeticMean(lmap(lambda p: p.x**2, pairs))

    coefficient = meanXY/meanX2
    return coefficient


def getLineDeviation(pairs):
    meanX2 = getArithmeticMean(lmap(lambda p: p.x**2, pairs))
    meanY2 = getArithmeticMean(lmap(lambda p: p.y**2, pairs))
    n = len(pairs)
    a = getLineCoefficient(pairs)

    deviation = (1/n * (meanY2/meanX2 - a**2))**0.5
    return deviation


M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
PHI = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
pairs = [Pair(p[0], p[1]) for p in zip(PHI, M)]

lineCoefficient = getLineCoefficient(pairs)
lineDeviation = getLineDeviation(pairs)
print(f"{lineCoefficient} += {lineDeviation}")
