if __name__ == "__main__":
    file = open("day1input.txt", "r")
    count = 0
    count_max = 0
    for line in file:
        if line == '\n':
            if count > count_max:
                count_max = count
            count = 0
        else:
            count += int(line.strip())
    
    print(count_max)    
    file.close()