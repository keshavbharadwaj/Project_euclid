def main():
    y = 9
    for i in range(0, 10):
        a = i
        for j in range(0, 10):
            b = j
            if a == 0 or b == 0:
                print(a, b)
            else:
                y += 1
                print((y, a, b))

    for i in range(1, 10):
        a = i
        for j in range(0, 10):
            b = j
            for k in range(0, 10):
                c = k
                if a == 0 or b == 0 or c == 0:
                    print(a, b, c)
                else:
                    y += 1
                    print((y, a, b, c))

    for i in range(1, 10):
        a = i
        for j in range(0, 10):
            b = j
            for k in range(0, 10):
                c = k
                for u in range(0, 10):
                    d = u
                    if a == 0 or b == 0 or c == 0 or d == 0:
                        print(a, b, c, d)
                    else:
                        y += 1
                        print((y, a, b, c, d))


main()
