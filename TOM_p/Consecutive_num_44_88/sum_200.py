def con_sum200(x, y, z):
    a1 = x + y + 44
    a2 = y + 44 + z
    a3 = 44 + z + 88

    if a1 == 200 and a2 == 200 and a3 == 200:
        print(x, y, z)


def main():
    for i in range(1, 200):
        a = i
        for j in range(1, 200):
            b = j
            for k in range(1, 200):
                c = k
                con_sum200(a, b, c)


main()
