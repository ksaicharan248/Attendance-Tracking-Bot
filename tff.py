import math
import re

pi = math.pi
j = 1j
i = 1j


def parse_complex(s):
    if 'j' not in s:
        return float(s)
    else:
        parts = re.split(r"([-+]?\d+(?:\.\d+)?j?)", s)
        if 'j' in s and len(parts) == 3:
            real_part = '0'
            imag_par = parts[1]
            imag_part = imag_par.replace('j', '')
        elif len(parts) == 5:
            real_part = parts[1]
            imag_part = parts[2] + parts[3]
            imag_part = imag_part.replace('j', '')
        return complex(float(real_part), float(imag_part))


def dft(x):
    N = len(x)
    X = []
    V = []
    for k in range(0, N):
        xk = 0
        for n in range(N):
            sl = x[n] * complex_exponential(k, n, N)
            xk = sl + xk

        X.append(xk)

    for i in range(0, len(X)):
        x = complex(chop(round_number(X[i].real)), chop(round_number(X[i].imag)))
        V.append(x)
    return V


def round_number(num):
    l = float(num) - int(num)
    if round(l, 5) == 0.999999:
        return int(num) + 1
    else:
        return round(num, 5)


def complex_exponential(k, n, N):
    if k == 0 and n == 0:
        return 1
    elif k == 0:
        return 1
    elif n == 0:
        return 1
    else:
        angle = 2 * pi * k * n / N
        real_part = math.cos(angle)
        imag_part = -math.sin(angle)
        if abs(imag_part) < 1e-10:
            imag_part = 0
        return real_part + j * imag_part


def chop(n):
    if "e" in str(n):
        n = 0
    else:
        n = n
    return n


def idft(x):
    N = len(x)
    X = [0]
    V = []
    O = []
    for k in range(N):
        xk = 0
        for n in range(N):
            X = x[n] * complex_exponentiali(k, n, N)
            xk = X + xk

        n = xk / N
        V.append(n)

    for i in range(0, len(V)):
        y = complex(round_number(chop(V[i].real)), round_number(chop(V[i].imag)))
        O.append(y)

    return O


def complex_exponentiali(k, n, N):
    if k == 0 and n == 0:
        return 1
    elif k == 0:
        return 1
    elif n == 0:
        return 1
    else:
        angle = 2 * pi * k * n / N
        real_part = math.cos(angle)
        imag_part = math.sin(angle)
        if abs(real_part) < 1e-5:
            real_part = 0
        if abs(imag_part) < 1e-4:
            imag_part = 0
        if "e" in str(real_part):
            real_part = 0
        if "e" in str(imag_part):
            imag_part = 0

        return real_part + j * imag_part
