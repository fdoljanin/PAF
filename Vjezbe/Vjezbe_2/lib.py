def getUpdater(accDifferentialEq, conditions):
    """
    Returns function that will update a,v,x for dt.

    Parameters
    ----------
    accDifferentialEq
        Lambda contaning a,v,x dependency that calculates acceleration.
    conditions
        Initial conditions (v, x)
    """
    conditions = None, *conditions

    def updater(dt):
        nonlocal conditions
        a, v, x = conditions
        a = accDifferentialEq(a, v, x)
        v = v + dt * a
        x = x + dt * v

        conditions = (a, v, x)
        return conditions
    return updater
