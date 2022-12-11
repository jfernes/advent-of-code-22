if __name__ == "__main__":
    file = open("day1input.txt", "r")
    suma = 0
    suma_max = 0
    for line in file:
        if (line == '\n'):
            if (suma > suma_max):
                suma_max = suma
            suma = 0
        else:
            suma += int(line.strip())
    
    print(suma_max)    
    file.close()