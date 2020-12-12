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

def rotate(tup, degs):
    qters = int(degs/90) % 4
    if qters == 0:
        return tup
    elif qters == 1:
        return [-tup[1], tup[0]]
    elif qters == 2:
        return [-tup[0], -tup[1]]
    elif qters == 3:
        return [tup[1], -tup[0]]

with open("12-input.txt", "r") as file:
    inp = file.read().strip().split('\n')
    waypoint = [10,1]
    ew = 0
    ns = 0
    for instruction in inp:
        cmd = instruction[0]
        arg = int(instruction[1:])
#        print(cmd, arg)
        if cmd == 'F':
            # only time the ship moves
            ew += waypoint[0]*arg
            ns += waypoint[1]*arg
        elif cmd in ['L','R']:
            waypoint = rotate(waypoint, turningLR[cmd]*arg)
#            print(waypoint)
        elif cmd in dirs:
#            print(ew, ns, cmd, arg)
            waypoint = [waypoint[0] + dirNums[cmd][0]*arg,
                        waypoint[1] + dirNums[cmd][1]*arg]
print(abs(ns) + abs(ew))
