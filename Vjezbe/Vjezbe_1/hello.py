import numpy as np
import matplotlib.pyplot as plt


def tryParse(parser, object):
    try:
        return (True, parser(object))
    except:
        return (False, None)


def lmap(m, o): return list(map(m, o))


def getLineEq(p1, p2):
    a = (p2["y"] - p1["y"]) / (p2["x"]-p1["x"])
    b = p1["y"] - p1["x"]*a

    return (a, b)


def plotGraph(function=None, title=None, dots=[], decision='PDF'):
    if function:
        minX = min(map(lambda e: e['x'], dots))
        maxX = max(map(lambda e: e['x'], dots))

        x = np.linspace(min(-5, minX-1), max(5, maxX+1), 100)
        y = function(x)
        plt.plot(x, y)

    for dot in dots:
        plt.plot(dot['x'], dot['y'], 'bo')

    if title:
        plt.title(title)

    if decision == 'PDF':
        plt.savefig('plot.pdf')
    elif decision == 'SHOW':
        plt.show()
    else:
        raise Exception('Invalid show option')


def getFunctionName(a, b):
    return f"{a}x {'+' if b>=0 else '-'} {abs(b)}"


coords = None
while True:
    userInput = input("Unesi koordinate u obliku x1,y1 x2,y2")
    isSuccess, coords = tryParse(lambda i: lmap(lambda c: dict(
        x=float(c.split(',')[0]), y=float(c.split(',')[1])), i.split()), userInput)
    if isSuccess:
        break
    print("Unos neispravan!")

a, b = getLineEq(*coords)
# print(getFunctionName(a, b))
plotGraph(lambda x: a*x+b, getFunctionName(a, b), coords, 'PDF')
