find = 22406676 # replace result from p1 here
with open("09-input.txt", "r") as file:
    inp = file.read().strip().split('\n')
    numbers = [int(elem) for elem in inp]
    sublist = list()
    for lower in range(len(numbers)):
        sublist.clear()
        sublist.append(numbers[lower])
        for upper in range(lower + 1, len(numbers)):
            sublist.append(numbers[upper])
            check = sum(sublist)
            if check == find:
                print(min(sublist) + max(sublist))
                break
            if check > find:
                break
