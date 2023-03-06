def getUpdater(accDifferentialEq, initialConditions):
    """"
    Returns function that will update a,v,x for dt. Argument is lambda contaning a,v,x dependency and initial conditions
    """
    conditions = initialConditions

    def updater(dt):
        nonlocal conditions
        a, v, x = conditions
        a = accDifferentialEq(a, v, x)
        v = v + dt * a
        x = x + dt * v

        conditions = (a, v, x)
        return conditions
    return updater
