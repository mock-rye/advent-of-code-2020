matList = []
counter = 0
x = 0
y = 0

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

print(width, height)

for row in matList:
#    print(x, y)
    if(row[y]):
        counter = counter + 1
    y = (y + 3) % width
    x = x + 1

print(counter)
