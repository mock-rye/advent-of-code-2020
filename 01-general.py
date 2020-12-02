def part1(inputList):
    for line in inputList:
        if (2020-line) in inputList:
            return line*(2020-line)

def part2(inputList):
    twoSumList = []
    for iter1 in inputList:
        for iter2 in inputList:
            for first, second in twoSumList:
                if (iter1 + first == 2020):
                   return iter1 * second
            twoSumList.append([iter1+iter2, iter1*iter2])

argList = []
with open("01-input.txt", "r") as file:
    for line in file:
        argList.append(int(line))

print(part1(argList))
print(part2(argList))
