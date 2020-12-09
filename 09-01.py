with open("09-input.txt", "r") as file:
    inp = file.read().strip().split('\n')
    preamble = [int(elem) for elem in inp[0:25]]
    nums = [int(elem) for elem in inp[25:]]
    for num in nums:
        if not num in [j + k for j in preamble for k in preamble if j != k]:
            print(num)
        preamble.pop(0)
        preamble.append(num)
