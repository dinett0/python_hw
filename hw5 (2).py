import math


def main(y, x):
    result = 0
    n = len(x)
    y = [0] + y
    x = [0] + x
    for i in range(1, n + 1):
        a = 13 * x[n + 1 - math.ceil(i / 3)] ** 3
        b = y[n + 1 - math.ceil(i / 4)] ** 2
        result += 95 * (a - b - 0.01) ** 4
    return result
