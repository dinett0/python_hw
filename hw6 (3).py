def ATS(x):
    if x[4] == "ATS":
        if x[3] == "LESS":
            return 0
        if x[3] == "ATS":
            return FANCY(x, 1, 2)
        return 3
    if x[4] == "HLSL":
        return l991(x, 4, FANCY(x, 5, 6))
    return l991(x, FANCY(x, 7, 8), 9)


def FANCY(x, high, low):
    if x[0] == "FANCY":
        return high
    return low


def l991(x, high, low):
    if x[2] == 1991:
        return high
    return low


def main(x):
    if x[1] == "AGDA":
        return ATS(x)
    if x[1] == "LESS":
        return 10
    return 11
