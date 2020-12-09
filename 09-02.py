find = 22406676 # replace result from p1 here
with open("09-input.txt", "r") as file:
    inp = file.read().strip().split('\n')
    numbers = [int(elem) for elem in inp]
    lower = 0
    upper = 1
    count = sum(numbers[0:2])
    while count != find:
# thanks bunny and cog
        while count < find:
            upper += 1
            count += numbers[upper]
        while count > find:
            count -= numbers[lower]
            lower += 1
    sublist = numbers[lower:upper+1]
    print(min(sublist) + max(sublist))
