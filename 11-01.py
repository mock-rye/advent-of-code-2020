import copy
dct = {
    '.': 0,
    'L': 1,
    '#': 1
}

def between(num, lower, upper):
    return (num >= lower and num <= upper)

def iteration(aliveMat, seatMat, debug=False):
    returnMat = list()
    rowQty = len(seatMat)
    colQty = len(seatMat[0])
    adjMat = list()
    for row in range(rowQty):
        rowLst = list()
        adjRow = list()
        for col in range(colQty):
            if not seatMat[row][col]:
                rowLst.append(0)
                continue
            adjacent = 0
            for rowOffset in [-1,0,+1]:
                for colOffset in [-1,0,+1]:
                    if (row + rowOffset) in range(rowQty) and (col + colOffset) in range(colQty) and ((rowOffset != 0) or (colOffset != 0)):
                        if(aliveMat[row + rowOffset][col + colOffset]):
                            adjacent += 1
            adjRow.append(adjacent)
            if adjacent == 0:
                rowLst.append(1)
            elif adjacent >= 4:
                rowLst.append(0)
            else:
                rowLst.append(aliveMat[row][col])
            
        adjMat.append(adjRow)
        returnMat.append(rowLst)
    if debug:
        print(prettify(aliveMat))
        print(prettify(returnMat))
    return returnMat

def coerceInt(bol):
    if(bol):
        return 1
    return 0

def prettify(inMat, coerce=True):
    if coerce:
        return ''.join([''.join([str(coerceInt(elem)) for elem in row])+'\n' for row in inMat])
    return ''.join([''.join([str(elem) for elem in row])+'\n' for row in inMat])

with open("11-input.txt", "r") as file:
    rows = file.read().strip().split('\n')
    seatMat = list()
    rowBool = list()
    for row in rows:
#        print(row)
        rowBool = [dct[elem] for elem in row]
#        print(''.join([str(elem) for elem in rowBool]))
        seatMat.append(rowBool)
    aliveMat = [[0 for elem2 in elem1] for elem1 in seatMat]
    trackMat = []
#    print(prettify(seatMat))
#    aliveMat = iteration(trackMat, seatMat)
    while trackMat != aliveMat:
        trackMat = copy.deepcopy(aliveMat)
        aliveMat = iteration(trackMat, seatMat)
#    print(prettify(aliveMat))
    print(sum([row.count(1) for row in aliveMat]))
#    print(prettify(aliveMat))
