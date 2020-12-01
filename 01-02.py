inputList = []
twoSumList = []
solution = 0

with open("01-input.txt", "r") as file:
    for line in file:
        line = int(line)

        for i in inputList:
            twoSumList.append([line+i, line*i])
        inputList.append(line)
#        print("\t"+str(line))
#   print debugging is *fun*
        for a, b in twoSumList:
#            print("\t\t" + str(line + a))
#   print debugging is *really* fun
            if (line+a == 2020):
                solution = line*b


print(solution)
