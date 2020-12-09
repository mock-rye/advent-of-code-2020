def part1(preamble, nums):
    for num in nums:
        if not num in [j + k for j in preamble for k in preamble if j != k]:
            return num
        preamble.pop(0)
        preamble.append(num)

def part2(numbers, find):
# thanks bunny and cog
    lower = 0
    upper = 1
    count = sum(numbers[0:2])
    while count != find:
        while count < find:
            upper += 1
            count += numbers[upper]
        while count > find:
            count -= numbers[lower]
            lower += 1
    sublist = numbers[lower:upper+1]
    return min(sublist) + max(sublist)


with open("09-input.txt", "r") as file:
    inp = file.read().strip().split('\n')
    preamble = [int(elem) for elem in inp[0:25]]
    nums = [int(elem) for elem in inp[25:]]
    # for p1
    numbers = [int(elem) for elem in inp]
    # for p2

print(invalid := part1(preamble, nums))
print(part2(numbers, invalid))
