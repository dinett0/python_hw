import math


def main(y):
    if y < -63:
        result = 44 * y**3 + y - y**4 / 77 - math.atan(y) ** 3
    elif y < -17:
        result = 96 * y + 86 * y**3
    else:
        result = y**2
    return result
