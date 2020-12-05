boolDict = {
    'F': 0,
    'B': 1,
    'R': 1,
    'L': 0
}

with open("05-input.txt", "r") as file:
    locMax = 0
    for line in file:
        string = ''.join(str(boolDict[char]) for char in line[0:-1]) #thanks cog
        locMax = max(locMax, int(string, 2))
    print(locMax)


