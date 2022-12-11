if __name__ == "__main__":
    dic = {
        "A": "Y",
        "B": "Z",
        "C": "X",
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    dic2 = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    file = open("day2input.txt", "r")
    score = 0
    for line in file:
        line = line.strip()
        if line[2] == dic[line[0]]:
            score += 6 + dic[line[2]]
        elif dic2[line[0]] == line[2]:
            score += 3 + dic[line[2]]
        else:
            score += dic[line[2]]
    print(score)
