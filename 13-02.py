with open("13-input.txt", "r") as file:
    # holy fuck this was some sneaky math wtf eric
    inp = file.readlines()
    busses = inp[1].split(',')
    columns = [index for index in range(len(busses)) if busses[index] != 'x']
    busses = [int(elem) for elem in busses if elem != 'x']
#    print(times)
#    print(busses)
    time = 0
    timeIncrement = 1
    for busID, column in zip(busses, columns):
#        print(bus, timeIncrement)
        while (time + column) % busID != 0:
            time += timeIncrement
#        print(time)
        timeIncrement *= busID
    print(time)
