import math

pi = math.pi
i = 1j


def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        xk = 0
        for n in range(N):
            xk += x[n] * complex_exponential(k, n, N)

        X.append(xk)
    return X


def complex_exponential(k, n, N):
    if k == 0 and n == 0:
        return 1
    elif k == 0:
        return 1 if n % N == 0 else 0
    elif n == 0:
        return 1
    else:
        angle = 2 * pi * k * n / N
        real_part = math.cos(angle)
        imag_part = -math.sin(angle)
        if abs(imag_part) < 1e-10:
            imag_part = 0
        return real_part + i * imag_part