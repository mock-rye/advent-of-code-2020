def checkthrough(insts):
    accumulator = int()
    visited = set()
    index = 0
    while index < len(insts):
        instruction = insts[index]
        cmd = instruction[0]
        arg = instruction[1]
        if(index in visited):
            return False
        visited.add(index)
        if(cmd == "jmp"):
            index += arg
            continue
        elif(cmd == "acc"):
            accumulator += arg
            index += 1
            continue
        elif(cmd == "nop"):
            index += 1
            continue
    return accumulator

with open("08-input.txt","r") as file:
    inp = file.read().strip().split('\n')
    lines = list()
    for line in inp:
#        print(line)
        lines.append([line.split()[0], int(line.split()[1])])

holder = [line for line in lines]
for index in range(len(lines)):
    if(lines[index][0] == "jmp"):
        holder[index] = ["nop", holder[index][1]]
    elif(lines[index][0] == "nop"):
        holder[index] = ["jmp", holder[index][1]]
    else:
        continue
#    print(lines[index], holder[index])
    thing = checkthrough(holder)
    holder[index] = lines[index]
    if thing:
        print(thing)

