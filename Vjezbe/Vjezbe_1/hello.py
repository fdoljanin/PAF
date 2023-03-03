def tryParse(parser, object):
    try:
        return (True, parser(object))
    except:
        return (False, None)


def lmap(m, o): return list(map(m, o))


def getLineEq(p1, p2):
    a = (p2["y"] - p1["y"]) / (p2["x"]-p1["x"])
    b = p1["y"] - p1["x"]*a

    return f"{a}x {'+' if b>=0 else '-'} {abs(b)}"


coords = None

while True:
    userInput = input("Unesi koordinate u obliku x1,y1 x2,y2")
    isSuccess, coords = tryParse(lambda i: lmap(lambda c: dict(
        x=float(c.split(',')[0]), y=float(c.split(',')[1])), i.split()), userInput)
    if isSuccess:
        break
    print("Unos neispravan!")

print(getLineEq(*coords))
