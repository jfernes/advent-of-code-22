def get_ascii(c):
    if ord(c) > 96:
        return ord(c) - 96
    else:
        return ord(c) - 64 + 26


if __name__ == "__main__":
    prio_sum = 0
    file = open("day3input.txt", "r")
    for line in file:
        used = []
        line = line.strip()
        rs1 = line[:int(len(line)/2)]
        rs2 = line[int(len(line)/2):]
        for i in range(0, int(len(rs1))):
            for j in range(0, int(len(rs2))):
                if rs1[i] == rs2[j] and used.count(rs1[i]) == 0:
                    prio_sum += get_ascii(rs1[i])
                    used.append(rs1[i])

    print(prio_sum)
