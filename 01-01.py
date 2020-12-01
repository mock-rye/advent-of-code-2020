inputList = []
solution = 0

with open("01-input.txt", "r") as file:
    for line in file:
        line = int(line)
        inputList.append(line)
        if (2020-line) in inputList:
            solution = line*(2020-line)


print(solution)