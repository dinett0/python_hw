import math


def f(z, y, x):
    res = 0
    n = len(z) - 2
    for i in range(len(z)):
        res += 95 * math.exp(
            85 * pow(y[n + 1 - i], 3) - pow(x[math.ceil(i // 4)], 2) - z[n + 1 - i]
        )
    return res


print(
    f(
        [-0.63, -0.33, 0.15, 0.92, -0.44],
        [0.3, 0.79, 0.49, 0.17, 0.29],
        [0.05, -0.64, 0.1, 0.31, -0.33],
    )
)
