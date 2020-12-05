def checkSlope(inMat, vertical, horizontal, width, height):
    x = 0
    y = 0
    counter = 0
    while x in range(height):
        if(inMat[x][y]):
            counter = counter + 1
        y = (y + horizontal) % width
        x = x + vertical
    return counter

def solve(inList):
    height = len(inList)
    width = len(inList[0])
    return checkSlope(inList, 1, 3, width, height)

def boolify(char):
#   True if there's a tree, False otherwise
    if(char == '#'):
        return True
    if(char == '.'):
        return False

with open("03-input.txt", "r") as file:
    matList = []
    for line in file:
        boolLine = [boolify(char) for char in line.strip()]
        matList.append(boolLine)

print(solve(matList))
