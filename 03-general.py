matList = []

def checkSlope(inMat, vertical, horizontal, height, width):
    x = 0
    y = 0
    counter = 0
    while x in range(height):
        if(inMat[x][y]):
            counter = counter + 1
        y = (y + horizontal) % width
        x = x + vertical
    return counter

def part1(inList):
    height = len(inList)
    width = len(inList[0])
    return checkSlope(inList, 1, 3, height, width)

def part2(inList):
    result = 1
    slopeList = [
        [1, 1],
        [1, 3],
        [1, 5],
        [1, 7],
        [2, 1]
    ]
    height = len(inList)
    width = len(inList[0])
    for hor, ver in slopeList:
        result = result * checkSlope(inList, hor, ver, height, width)
    return result

def boolify(char):
    if(char == '#'):
        return True
    if(char == '.'):
        return False

with open("03-input.txt", "r") as file:
    for line in file:
        boolLine = [boolify(char) for char in line.strip()]
        matList.append(boolLine)

height = len(matList)
width = len(matList[0])

print(part1(matList))
print(part2(matList))
