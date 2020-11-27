

def main():
    sum_1 = 0
    k = 0
    for i in range(1, 2021):
        if (pow(i, 2) % 25 == 14) and (pow(i, 3) % 25 == 13):
            k += 1
            print(i)
            sum_1 += i

    print(sum_1)
    print(k)


main()