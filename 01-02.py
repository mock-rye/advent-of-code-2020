inputList = []
twoSumList = []
solution = 0

with open("01-input.txt", "r") as file:
    for line in file:
        line = int(line)
        for i in inputList:
            twoSumList.append([line+i, line*i])
        inputList.append(line)
        for first, second in twoSumList:
            if (line + first == 2020):
                solution = line * second


print(solution)
