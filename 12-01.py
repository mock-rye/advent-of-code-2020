dirNums = {
    'E': [+1,0],
    'S': [0,-1],
    'W': [-1,0],
    'N': [0,+1]
    }
turningLR = {
    'L': +1,
    'R': -1
    }
dirs = ['E','N','W','S']

with open("12-input.txt", "r") as file:
    inp = file.read().strip().split('\n')
    heading = 0
    ns = 0
    ew = 0
    for instruction in inp:
        cmd = instruction[0]
        arg = int(instruction[1:])
#        print(cmd, arg)
        if cmd == 'F':
            cmd = dirs[heading]
        elif cmd in ['L','R']:
            heading = (heading + turningLR[cmd]*int(arg/90)) % 4
#            print(dirs[heading])
        if cmd in dirs:
#            print(ew, ns, cmd, arg)
            ew += dirNums[cmd][0]*arg
            ns += dirNums[cmd][1]*arg
    print(abs(ns) + abs(ew))
