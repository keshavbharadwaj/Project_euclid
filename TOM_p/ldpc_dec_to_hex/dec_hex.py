import math


def ram_file(k):
    f = open("C:/Users/vivek/Desktop/ldpc14_sram" + k + ".txt", "r")
    dec = []
    for x in f:
        for line in x.split("\n"):
            for val in line.split(" "):
                if val == '':
                    continue
                dec.append(hex(int(val)))

    print(dec)
    f.close()

    i = 0
    f = open("C:/Users/vivek/Desktop/ldpc14_sram" + k + "_hex.txt", "w")
    for hex_str in dec:
        if i == int(k):
            f.write("\n")
            i = 0
        i += 1
        f.write(str(hex_str + ','))
    f.close()


def main():
    ram_file('12')
    ram_file('3')


main()
