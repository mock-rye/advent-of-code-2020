with open("08-input.txt","r") as file:
    inp = file.read().split('\n')
    visited = set()
    accumulator = int()
    index = 0
    while not index in visited:
        instruction = inp[index]
        visited.add(index)
#        print(index, instruction)
        cmd = instruction.split()[0]
        arg = int(instruction.split()[1])
        if(cmd == "jmp"):
            index += arg
            continue
        elif(cmd == "acc"):
            accumulator += arg
        elif(cmd == "nop"):
            pass
        index += 1

print(accumulator)
#print(visited)
