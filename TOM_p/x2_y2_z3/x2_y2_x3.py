import math


def sq_cube(x, y, z):
    if math.pow(x, 2) + math.pow(y, 2) == math.pow(z, 3):
        print((x, y, z))


def main():
    for i in range(1, 100):
        a = i
        for j in range(1, 100):
            b = j
            for k in range(1, 100):
                c = k
                sq_cube(a, b, c)


main()
