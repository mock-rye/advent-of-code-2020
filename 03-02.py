matList = []

def checkSlope(inMat, horizontal, vertical, width, height):
    x = 0
    y = 0
    counter = 0
    while x in range(height):
#        print('\t', x, y)
        if(inMat[x][y]):
            counter = counter + 1
        y = (y + horizontal) % width
        x = x + vertical
    return counter


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

s0 = checkSlope(matList, 1, 1, width, height)
s1 = checkSlope(matList, 3, 1, width, height)
s2 = checkSlope(matList, 5, 1, width, height)
s3 = checkSlope(matList, 7, 1, width, height)
s4 = checkSlope(matList, 1, 2, width, height)

print(s0 * s1 * s2 * s3 * s4)
