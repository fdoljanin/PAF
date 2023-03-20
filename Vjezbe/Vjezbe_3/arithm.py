def getArithmeticMean(elements):
    return sum(elements) / len(elements)


def getStandardDeviation(elements: list):
    """
    Returns standard deviation for entered elements.

    Parameters
    ----------
    elements
      list of elements that numeric operations can be performed on
    """
    mean = getArithmeticMean(elements)
    differenceSum = sum([(el-mean)**2 for el in elements])
    card = len(elements)

    deviation = (differenceSum/card)**0.5
    return deviation
