import math


def main(n):
    if n == 0:
        return 0.19
    if n >= 1:
        return 1 - math.atan(main(n - 1)) - (main(n - 1)) ** 2 / 18
