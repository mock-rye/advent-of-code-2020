with open("13-input.txt", "r") as file:
    inp = file.readlines()
    startTime = int(inp[0])
    busses = inp[1].split(',')
    busses = [int(bus) for bus in busses if bus != 'x']
    waitTimes = [(-startTime) % bus for bus in busses]
    # uses complimentary modulo to find the waiting time for each bus
    mnWait = min(waitTimes)
    shortBus = busses[waitTimes.index(mnWait)]
    print(mnWait*shortBus)
