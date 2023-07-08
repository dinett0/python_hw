import math


def main(y, x):
    numerator = 95 * (13 * x**3 - y**2 - 0.01) ** 4
    denominator = (1 + y**3 / 87) ** 3 + 54 * (y**3 - 43 * x - 26 * y**2) ** 2
    result = (numerator / denominator) - math.sqrt(
        (11 * x**2 + 43 * y**3) ** 6 - y**7
    )
    return result
