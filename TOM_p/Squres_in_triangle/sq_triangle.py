import math

from pandas.core.dtypes.inference import is_integer


def sq_tri(a, b, c):
    x = (pow(a, 2) + pow(b, 2) - pow(c, 2)) / 2
    y = (pow(a, 2) + pow(c, 2) - pow(b, 2)) / 2
    z = (pow(b, 2) + pow(c, 2) - pow(a, 2)) / 2

    if x.is_integer():
        if y.is_integer():
            if z.is_integer():
                if x > 0 and y > 0 and z > 0:
                    return x, y, z
                else:
                    return 0, 0, 0

    else:
        return 0, 0, 0


def main():
    for i in range(1, 20):
        a = i
        for j in range(1, 20):
            b = j
            for k in range(1, 20):
                c = k
                if a != b and b != c and a != c:
                    m, n, o = sq_tri(a, b, c)
                    if m != 0 and n != 0 and o != 0:
                        print(m, n, o)


main()
