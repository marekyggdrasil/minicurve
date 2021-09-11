import numpy as np


def extendedEuclideanAlgorithm(x1, x2):
    # base case
    if x1 == 0:
        return x2, 0, 1
    # recursive call
    gcd, x_, y_ = extendedEuclideanAlgorithm(x2 % x1, x1)
    x = y_ - (x2 // x1) * x_
    y = x_
    return gcd, x, y


# modular multiplicative inverse
def inverse(n, p):
    if n == 0:
        raise ZeroDivisionError('Stahp dividing by zero you!!!')
    if n < 0:
        # k ** -1 = p - (-k) ** -1  (mod p)
        return p - inverse(-n, p)
    gcd, x, _ = extendedEuclideanAlgorithm(n, p)
    assert gcd == 1
    assert np.mod(n*x, p) == 1
    return np.mod(x, p)
