storage = dict()
def waysFrom(number, adapters):
    # DFS through "adapters", return how many ways to get to the device from an adapter ("number")
    sm = 0
    if storage.get(number):
        # DP for *speed*
        return storage[number]
    if number == adapters[-1]:
        # base case
        return 1
    for num in [elem for elem in [number+1, number+2, number+3] if elem in adapters]:
        # recursion for all numbers in (number+1,number+3) also in "adapters"
        sm += waysFrom(num, adapters[1:])
    storage[number] = sm
    # cache for DP
    return sm

with open("10-input.txt", "r") as file:
    inp = [0] # the outlet
    inp += sorted([int(elem) for elem in file.read().strip().split('\n')]) # all of the adapters
    inp.append(inp[-1]+3) # your device
#    print(inp)
    print(waysFrom(0, inp))
