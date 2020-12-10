with open("10-input.txt", "r") as file:
    inp = [0] # the outlet
    inp += sorted([int(elem) for elem in file.read().strip().split('\n')]) # all of the adapters
    inp.append(inp[-1] + 3) # your device
#    print(inp)
    differences = [inp[index+1]-inp[index] for index in range(len(inp[:-1]))]
    # difference between every consecutive pair of adapters
    print(differences.count(1)*differences.count(3))
