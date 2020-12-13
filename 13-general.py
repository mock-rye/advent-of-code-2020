def part1(startTime, busses):
    # uses complimentary modulo to find the waiting time for each bus
    waitTimes = [(-startTime) % bus for bus in busses]
    mnWait = min(waitTimes)
    shortBus = busses[waitTimes.index(mnWait)]
    return mnWait * shortBus

def part2(busses, columns):
    # uses modular multiplication iteratively
    # assumes all the bus IDs are prime because why wouldn't you
    # eric don't you-
    time = 0
    timeIncrement = 1
    for busID, column in zip(busses, columns):
#        print(bus, timeIncrement)
        while (time + column) % busID != 0:
            time += timeIncrement
#        print(time)
        timeIncrement *= busID
    return time

with open("13-input.txt", "r") as file:
    # holy fuck this was some sneaky math wtf eric
    inp = file.readlines()
    startTime = int(inp[0])
    busses = inp[1].split(',')
    columns = [index for index in range(len(busses)) if busses[index] != 'x']
    busses = [int(elem) for elem in busses if elem != 'x']
    print(part1(startTime, busses))
    print(part2(busses, columns))
