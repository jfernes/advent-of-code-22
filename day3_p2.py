def get_ascii(c):
    if ord(c) > 96:
        return ord(c) - 96
    else:
        return ord(c) - 64 + 26


if __name__ == "__main__":
    prio_sum = 0
    file = open("day3input.txt", "r")
    lines = file.readlines()
    for index in range(0, len(lines), 3):
        used = []
        line1 = lines[index].strip()
        line2 = lines[index+1].strip()
        line3 = lines[index+2].strip()
        for i in range(0, len(line1)):
            for j in range(0, len(line2)):
                for k in range(0, len(line3)):
                    if line1[i] == line2[j] == line3[k] and used.count(line1[i]) == 0:
                        used.append(line1[i])
                        prio_sum += get_ascii(line1[i])

    print(prio_sum)
