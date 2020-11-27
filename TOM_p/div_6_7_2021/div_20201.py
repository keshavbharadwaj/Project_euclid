
def main():
    sum_1 = 0
    k = 0
    for i in range(1, 2100):
        if (i % 5 == 2) and (i % 9 == 3):
            k += 1
            print(i)
            sum_1 += i

    print(sum_1)
    print(k)


main()
