
import math
TARGET = 97
INITIAL = 10
TIMES = 6


def calcRoot(target, initial, times):
    x = initial
    for _ in range(times):
        x = (x + target / x) / 2
        print(x)
    return x


print('root of ', TARGET, 'may be', calcRoot(
    TARGET, INITIAL, TIMES), 'in fact', math.sqrt(TARGET))
