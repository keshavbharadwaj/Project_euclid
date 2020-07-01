def perimeter_2020(x, y, z):
    if x + y + z == 2020:
        print(x, y, z)
        return 1
    else:
        return 0


def main():
    sum = 0
    for i in range(1, 1000):
        a = i
        for j in range(1, 1000):
            b = j
            for k in range(1, 1000):
                c = k
                w = perimeter_2020(a, b, c)

                if w == 1:
                    sum += 1

    print(sum)


main()
