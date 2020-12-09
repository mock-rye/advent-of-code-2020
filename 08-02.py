class instruction:
    cmd = str()
    arg = int()
    def __init__(self, cmd, arg):
        self.cmd = cmd
        self.arg = arg

def checkthrough(instructions):
    accumulator = int()
    visited = set()
    index = 0
    while index < len(instructions):
        inst = instructions[index]
        cmd = inst.cmd
        arg = inst.arg
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
        lines.append(instruction(line.split()[0], int(line.split()[1])))

holder = [line for line in lines]
for index in range(len(lines)):
    if(lines[index].cmd == "jmp"):
        holder[index] = instruction("nop", lines[index].arg)
    elif(lines[index].cmd == "nop"):
        holder[index] = instruction("jmp", lines[index].arg)
    else:
        continue
#    print(lines[index].cmd, holder[index].cmd)
    thing = checkthrough(holder)
    holder[index] = lines[index]
    if thing:
        print(thing)

