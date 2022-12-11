if __name__ == "__main__":
    dic_win = {
        "A": "Y",
        "B": "Z",
        "C": "X"
    }

    dic_draw = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }

    dic_loss = {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }

    dic_points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    file = open("day2input.txt", "r")
    score = 0
    for line in file:
        line = line.strip()
        if line[2] == "Z":
            score += 6 + dic_points[dic_win[line[0]]]
        elif line[2] == "Y":
            score += 3 + dic_points[dic_draw[line[0]]]
        else:
            c = dic_loss[line[0]]
            score += dic_points[c]
    print(score)
