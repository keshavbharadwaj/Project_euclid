def ram_file(k):
    f = open("C:/Users/vivek/Desktop/ldpc14_sram" + k + ".txt", "r")
    hexa = []
    bina = []

    for x in f:
        for line in x.split("\n"):
            for val in line.split(" "):
                if val == '':
                    continue
                hexa.append(hex(int(val)))
                bina.append(bin(int(val)))

    print(hexa)
    print(bina)
    f.close()

    i = 0
    f = open("C:/Users/vivek/Desktop/ldpc14_sram" + k + "_hex.txt", "w")
    for hex_str in hexa:
        if i == int(k):
            f.write("\n")
            i = 0
        i += 1
        f.write(str(hex_str + ','))
    f.close()

    j = 0
    f = open("C:/Users/vivek/Desktop/ldpc14_sram" + k + "_bin.txt", "w")
    for bin_str in bina:
        if j == int(k):
            f.write("\n")
            j = 0
        j += 1
        f.write(str(bin_str + ','))
    f.close()


def main():
    ram_file('12')
    ram_file('3')


main()
