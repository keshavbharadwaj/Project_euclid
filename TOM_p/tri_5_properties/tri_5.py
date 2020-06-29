import math
from pandas.core.dtypes.inference import is_integer


def tri_5(a, b, c):
    semi_p = (a + b + c) / 2
    try:
        area = math.sqrt(semi_p * (semi_p - a) * (semi_p - b) * (semi_p - c))
        x = (a, b, c)
        y = sorted(x)

        if abs(y[0] - y[1]) == 1 and abs(y[2] - semi_p) == 1 and area.is_integer() and a + b + c < 2020:
            return a, b, c
        else:
            return 0, 0, 0
    except:
        return 9, 9, 9


def main():
    old_set = (0, 0, 0)
    for i in range(1, 1000):
        a = i
        for j in range(201, 400):
            b = j
            for k in range(801, 1000):
                c = k
                m, n, o = tri_5(a, b, c)
                if m != 0 and m != 9 and n != 0 and n != 9 and 0 != 9 and o != 0:
                    x = (m, n, o)
                    y = sorted(x)
                    if old_set != y:
                        print((m, n, o))
                    old_set = y


main()
