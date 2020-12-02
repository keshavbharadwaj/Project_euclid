import math

num_list = []
num_list2 = []


def mod_fill(p):
    if p % 4 == 3 and (p - 1) % 2 == 0:
        val1 = math.pow(math.factorial((p - 1) / 2), 2)
        if val1 % p == 1:
            num_list.append(p)

    return num_list


def mod_fill2(q):
    if q % 4 == 3 and (q - 1) % 2 == 0:
        val1 = math.factorial((q - 1) / 2)
        if val1 % q == (q - 1):
            num_list2.append(q)

    return num_list2


def main():
    res_list = []
    res_list2 = []

    for i in range(1, 100):
        res_list = mod_fill(i)
    for j in range(1, 5000):
        res_list2 = mod_fill2(j)

    print(res_list)
    print(res_list2)
    print(len(res_list2))


main()
