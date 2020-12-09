def part1(preamble, nums):
    for num in nums:
        if not sumIn(preamble, num):
            return num
        preamble.pop(0)
        preamble.append(num)

def sumIn(lst, number):
    for l in lst:
        for j in lst:
            if l + j == number:
                return True
    return False

def part2(numbers, find):
    sublist = list()
    for lower in range(len(numbers)):
        sublist.clear()
        sublist.append(numbers[lower])
        for upper in range(lower + 1, len(numbers)):
            sublist.append(numbers[upper])
            check = sum(sublist)
            if check == find:
                return min(sublist) + max(sublist)
                break
            if check > find:
                break


with open("09-input.txt", "r") as file:
    inp = file.read().strip().split('\n')
    preamble = [int(elem) for elem in inp[0:25]]
    nums = [int(elem) for elem in inp[25:]]
    # for p1
    numbers = [int(elem) for elem in inp]
    # for p2

print(invalid := part1(preamble, nums))
print(part2(numbers, invalid))
