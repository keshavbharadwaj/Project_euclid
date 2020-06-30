def fib_4mil(n):
    x, y = 0, 1
    count = 0
    i = 0
    even_sum = 0
    a = []
    # print(0)
    # print(1)

    while count <= n:
        fib = x + y
        x = y
        y = fib
        count += 1
        a.append(fib)

    print(a)

    while i < len(a):
        if i+1 < len(a):
            if a[i] < 4000000:
                even_sum += a[i+1]
                i += 3
                print(even_sum)
            else:
                return even_sum
    return even_sum


def main():
    a = fib_4mil(34)
    print("even sum is", a)


main()
