if __name__ == "__main__":
    file = open("day1input.txt", "r")
    count = 0
    count_first = 0
    count_second = 0
    count_third = 0
    for line in file:
        if line == '\n':
            if count > count_first:
                count_third = count_second
                count_second = count_first
                count_first = count
            elif count > count_second:
                count_third = count_second
                count_second = count
            elif count > count_third:
                count_third = count
            count = 0
        else:
            count += int(line.strip())
    
    print(count_first + count_second + count_third)    
    file.close()