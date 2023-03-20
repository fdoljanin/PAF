from arithm import *
import numpy as np

array = [10, 8, 9.33, 10.11, 11, 9.5]
deviationByMe = getStandardDeviation(array)
deviationByNumpy = np.std(array)
meanByMe = getArithmeticMean(array)
meanByNumpy = np.average(array)

print(meanByMe, meanByNumpy)
print(deviationByMe, deviationByNumpy)
