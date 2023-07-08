import math


def main(n, a, x):
    result = 0
    for c in range(1, a + 1):
        for k in range(1, n + 1):
            result += (x**2 / 11 - k) ** 3 + 82 * (c**2 / 53 - 1) ** 6 + 1
    return result
