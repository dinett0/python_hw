def main(x):
    S1 = 0b11 & x
    S2 = 0b1111111 & (x >> 2)
    S3 = 0b111111111 & (x >> 9)
    S4 = 1 & (x >> 18)
    S5 = 0b1111111111 & (x >> 19)
    return (str(S1), str(S2), str(S3), str(S4), str(S5))
