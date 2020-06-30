def main():
    sum_3_5 = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            # print(i)
            sum_3_5 += i
    print(sum_3_5)


def div_by_n(multiple, end_no):
    end_no = end_no // multiple                             # p = floor(p,n)
    return multiple * end_no * (end_no + 1) / 2            # n*p*(p+1)/2


def main1():
    print(div_by_n(3, 999999999) + div_by_n(5, 999999999) - div_by_n(15, 999999999))   # div (n,p) n: multiples, p: target number


#main()
main1()
