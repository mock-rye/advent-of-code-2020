boolDict = {
    'F': 0,
    'B': 1,
    'R': 1,
    'L': 0
}

storage = set()

with open("05-input.txt", "r") as file:
    locMax = 0
    for line in file:
        string = ''.join(str(boolDict[char]) for char in line.strip()) #thanks cog
        storage.add(int(string, 2))

for i in range(min(storage), max(storage)):
    if i not in storage:
        print(i)
