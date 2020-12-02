def part1(inputList):
    counter = 0
    for args, letter, password in inputList:
        if password.count(letter) in range(args[0], args[1]+1):
            counter = counter + 1
    return counter

def part2(inputList):
    counter = 0
    for args, letter, password in inputList:
        first = args[0] - 1
        second = args[1] - 1
        if (password[first] == letter) != (password[second] == letter):
            counter = counter + 1
    return counter

argList = []
with open("02-input.txt", "r") as file:
    for line in file:
        temp_list = line.split()
        args = [int(i) for i in temp_list[0].split('-')]
        letter = temp_list[1].replace(':','')
        password = temp_list[2]
        argList.append([args, letter, password])

print(part1(argList))
print(part2(argList))
